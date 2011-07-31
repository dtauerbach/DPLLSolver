#!/usr/bin/python2.7
#
# author: Dan Auerbach (dtauerbach@gmail.com)
#
# Example usage:
# 
# python dpll_solver.py FILE=testdata/problem1.cnf
#
# This standalone module defines a DPLL-based SAT solver via the 
# class _DPLLSolver. The solver reads in files in DIMACS CNF format:
#
# Each line that starts with 'c' is a comment.
#
# The first non-comment line must have the form:  
# 'p cnf <NumOfVariables> <NumClauses>'.
#
# All other lines are space-delimited lists of literals with a positive
# value indicating the variable and a negative value indicating its
# negation. Each line is terminated with a '0', a reserved symbol. 
# Let "/\" represent logical conjunction, "\/" logical disjunction. 
# As an example, consider the formula: (x1 \/ ~x2) /\ (x3 \/ ~x4) 
# can be represented in DIMACS format by:
#
# p cnf 4 2
# 1 -2 0
# 3 -4 0
#
# This will print a satisfying assignment if one is found in the
# following format:
#
# A space delimited two-column file with one row per variable, and
# a binary number indicating whether it is set to True or False,
# e.g. 
# 1 0
# 2 1
# 3 0
# This means x1->False; x2->True; x3->False
#
# If the formula is unsatisfiable, UNSAT is printed.


import sys 
import copy
import random
import datetime

# Required flag for filename
_LOAD_FILENAME = None

# Flags for debugging, profiling
_DEBUG = False
_TIMING_DEBUG = False

# Variable branching algorithm flags, in order
# of priority
_RANDOM = False
_JEROSLOW = True
_TWOSIDED = True # only relevant for Jeroslow
_MOMS = False
# (i.e. mixed only kicks in if all the above are false)
_MIXED = True
_JERO_PROB = 0.50
_MOMS_PROB = 0.0

# Turns off printing of satisfying assignment or "UNSAT"
_NOPRINT = False

# Here we manage command-line flags
if not sys.argv:
  print """No command line arguments given. Required argument
is LOAD_FILENAME; for optional arguments look at source code"""
for a in sys.argv:
  if a[:14] == "LOAD_FILENAME=":
    _LOAD_FILENAME = a[14:]
  elif a[:5] == "FILE=":
    _LOAD_FILENAME = a[5:]
  elif a[:7] == "DEBUG=1" or a=="DEBUG":
    _DEBUG = 1
  # Command line flags for var/value ordering Heuristics
  elif a[:4] == "RAND":
    _RANDOM = True
  elif a[:4] == "MOMS":
    _MOMS = True
  elif a[:4] == "JERO":
    _JEROSLOW = True
  elif a == "TWOSIDED":
    _TWOSIDED = True
  elif a == "NOPRINT":
    _NOPRINT = True
  elif a == "TIMING":
    _TIMING_DEBUG = True

def _coin_flip():
  a = random.randint(0,1)
  if a==0: return -1
  else: return 1


class _DPLLSolver:
  """Where the magic happens.

  We implement a simple DPLL algorithm with cascading unit
  propagation, and several variable ordering heuristic options that
  can be toggled via command-line flags. There is naive backtracking
  but no conflict-directed backjumping or clause learning.

  The main class-level variables are:
  self.clauses: keeps track of our clauses at current stage
  self.lits, self.lit_dict: keep track of what literals we've set,
    i.e. where we are currently in the search tree.
  """

  def ReadInCNFFile(self, filename):
    """Reads in the CNF file, returns clauses as list of lists of ints.

    Args:
      file: (str) file path of CNF file
    Returns:
      clauses, num_vars: sorted list of lists of ints, int 
    """
    if _DEBUG:
      print "Opening %s" % filename
    file = open(filename, 'r')
    clauses = []
    num_vars = None
    num_clauses = None
    for l in file.readlines():
      if l[0] == 'p':
        if not l[:5] == 'p cnf':
          raise Exception, "unexpected file format"
        num_vars = int(l.split()[2])
        num_clauses = int(l.split()[3])
        continue
      if l[0] == 'c' or l[0] == '0' or not l.split() or l.split()[-1] != '0':
        continue
      clause = map(int,l.split()[:-1])
      clause.sort()
      clauses.append(clause)
    if _DEBUG:
      print "len: " + str(len(clauses))
      print "num: " + str(num_clauses)
    if num_clauses != len(clauses):
      raise Exception, "error reading in cnf file"
    file.close()
    return clauses, num_vars
  
  def SolveAndOutput(self, problem_str):
    """Wrapper to IterativeDPLL, prints solution.

    Args:
      problem_str: filename
    Returns:
      bool: satisfiable or not?  
    Prints:
      satisfying assignment or "UNSAT"
    """
    sat = False
    start_time = datetime.datetime.now()
    if not problem_str[-4:] == ".cnf":
      problem_str = problem_str + ".cnf"
    clauses, num = self.ReadInCNFFile(problem_str)
    if not self.IterativeDPLL(clauses, num):
      if not _NOPRINT:
        print "UNSAT"
    else:
      sat = True
      if not _NOPRINT:
        for lit in self.lits:
          if lit > 0:
            print "%s 1" % str(lit)
          else:
            print "%s 0" % str(-lit)
    end_time = datetime.datetime.now()
    if _TIMING_DEBUG or _DEBUG:
      print "Total time (seconds): %s" % str(datetime.datetime.now()-start_time)
    return sat

  def IterativeDPLL(self, clauses, num_lits):
    """Iterative implementation of DPLL algorithm; main loop.

    Args:
      clauses: list of tuples
      num_lits: int
    Returns:
      True: if satisfiable
      False: if unsat
    """
    self.num_lits = num_lits
    # lits keeps track of our current tree of assignments
    self.lits = []
    # underived is a list of bool in sync with lits. if True
    # at index i that means we still have to check -lits[i].
    self.underived = []
    # our list of clauses
    self.clauses = clauses
    # dict of assigned literals in our tree for speedy lookup
    self.lit_dict = {}
    # indicates the last index set to True in underived
    self.last_true_index = 0
    while True:
      if len(self.lits) < num_lits:
        # We have not assigned all our literals and can branch
        lit = self.ChooseBranch()
        self.lits.append(lit)
        self.underived.append(True)
        self.last_true_index = len(self.underived) - 1
        self.lit_dict[lit] = True
      val = self.UnitPropagate()
      if val == 0:
        continue
      if val == 1:
        return True
      elif val == -1:
        return False

  def UnitPropagate(self):
    """Our main unit propagator.

    Returns:
      0: keep going, need to choose another branch
      -1: unsatisfiable
      1: satisfying assignment found
    """
    clauses = copy.copy(self.clauses)
    while True:
      full_break = False
      cls = []
      for i in xrange(len(clauses)):
        c = clauses[i]
        if len(c) == 1:
          if -c[0] in self.lits:
            if self.NaiveBacktrack():
              full_break = True
              break
            else: return -1
          if not c[0] in self.lits:
            self.lits.append(c[0])
            self.underived.append(False)
            self.lit_dict[(c[0])] = True
        ccop = copy.copy(c)
        for j in xrange(len(c)):
          if c[j] in self.lit_dict: 
            break
          if -c[j] in self.lit_dict:
            ccop.remove(c[j])
            if not ccop:
              if self.NaiveBacktrack():
                full_break = True
                break
              else: return -1
          if j == len(c)-1:
            cls.append(ccop)
        if full_break:
          break
      if full_break:
        clauses = copy.copy(self.clauses)
      else:
        if len(cls) == 0:
          # Have a satisfying assignment in this case
          return 1
        if len(cls) == len(clauses) and not full_break:
          break
        clauses = cls
    return 0
        
  def NaiveBacktrack(self):
    """This will backtrack to nearest literal and switch it's value.
   
    Returns:
      bool: if False, we have nowhere to backtrack and are UNSAT
    """
    if self.last_true_index == -1:
      # Then we are unsatisfiable
      return False
    # Discard all of our derived literals
    self.lits = self.lits[:self.last_true_index+1]
    lit = self.lits.pop()
    self.lits.append(-lit)
    # This resets our lit_dict
    self.lit_dict = {}
    for i in xrange(len(self.lits)):
      self.lit_dict[self.lits[i]] = True 
    self.underived = self.underived[:self.last_true_index+1]
    # Flip the last index, since we have found a contradiction
    self.underived[self.last_true_index] = False
    self.SetLastTrueIndex()
    return True

  def SetLastTrueIndex(self):
    """Updates the value tracking the last index."""
    for i in xrange(len(self.underived)):
      if self.underived[len(self.underived)-i-1]:
        self.last_true_index = len(self.underived)-i-1
        return
    # This means we are out of True indices
    self.last_true_index = -1
    
  def ChooseBranch(self):
    """Based on what flags are set, choose variable to branch on."""
    cls = self.FilterClauses()
    if _RANDOM:
      return self.ChooseRandomLiteral() 
    elif _JEROSLOW:
      return self.JeroslowWang(cls)
    elif _MOMS:
      return self.MomsHeuristic(cls)
    elif _MIXED:
      rand = random.random()
      if rand < _JERO_PROB:
        return self.JeroslowWang(cls)
      elif rand > (1 - _MOMS_PROB):
        return self.MomsHeuristic(cls)
      else:
        return self.ChooseRandomLiteral()
    else:
      raise Exception, "not yet implemented!"

  def FilterClauses(self):
    """Updates clauses based on our dict of literals we've set."""
    cls = []
    for i in xrange(len(self.clauses)):
      c = self.clauses[i]
      ccop = copy.copy(c)
      for j in xrange(len(c)):
        if c[j] in self.lit_dict: 
          break
        if -c[j] in self.lit_dict:
          ccop.remove(c[j])
        if j == len(c)-1:
          cls.append(ccop)
    return cls

  def MomsHeuristic(self, clauses):
    """MOMS variable ordering heuristic."""
    if not clauses: return None
    moms = {}
    max = 0
    max_lit = 0
    min_len = len(clauses[0])
    for i in xrange(len(clauses)):
      if len(clauses[i]) < min:
        min_len = len(clauses[i])
    for j in xrange(len(clauses)):
      # Increment for clauses with min len
      if len(clauses[j]) == min_len:
        for lit in clauses[j]:
          if lit in moms:
            moms[lit] += 1
          else:
            moms[lit] = 1
          if moms[lit] > max:
            max = moms[lit]
            max_lit = lit
    if max_lit == 0:
      raise Exception, "MOMS algorithm error"
    return max_lit

  def JeroslowWang(self, clauses):
    """JW algorithm for variable ordering."""
    if not clauses: return None
    js = {}
    max = -1
    max_lit = 0
    for i in xrange(len(clauses)):
      for lit in clauses[i]:
        if lit in js: js[lit] += 2**(-len(clauses[i]))
        else: js[lit] = 2**(-len(clauses[i]))
        if _TWOSIDED:
          if -lit not in js: js[-lit] = 0
          if (js[lit]+js[-lit]) > max:
            max = js[lit]+js[-lit]
            if js[lit] > js[-lit]: max_lit = lit
            else: max_lit = -lit
        elif js[lit] > max:
          max = js[lit]
          max_lit = lit
    if max_lit == 0:
      raise Exception, "JW algorithm error, no clauses"
    return max_lit

  def ChooseRandomLiteral(self):
    """Random branching heuristic."""
    fulllits = range(1, self.num_lits+1)
    tochoose = []
    for i in xrange(len(fulllits)):
      if fulllits[i] in self.lit_dict or -fulllits[i] in self.lit_dict:
        continue
      tochoose.append(fulllits[i])
    return tochoose[random.randint(0, len(tochoose)-1)]*_coin_flip()

def main():
  solver = _DPLLSolver()
  if _LOAD_FILENAME:
    solver.SolveAndOutput(_LOAD_FILENAME)
  else:
    print "Please specify input file via FILE=<filename> argument."

if __name__ == "__main__":
  main()

