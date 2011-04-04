dan@ubuntu:~/aiclass/hw3/problem1$ python FORSHARE_solver.py SATproblems/problem1.cnf
Please specify input file via FILE=<filename> argument.
dan@ubuntu:~/aiclass/hw3/problem1$ python FORSHARE_solver.py FILE=SATproblems/problem1.cnf
dan@ubuntu:~/aiclass/hw3/problem1$ python FORSHARE_solver.py FILE=SATproblems/problem1.cnf
15 1
5 0
12 0
7 0
17 1
20 1
16 0
19 0
1 1
11 0
3 0
14 1
18 0
2 0
10 0
6 1
8 0
13 1
9 0
dan@ubuntu:~/aiclass/hw3/problem1$ python verifier/verify.py SATproblems/problem1.cnf hhh.out 
len clauses is 91
SUCCESS: Formula satisfied.
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver.py FILE=SATproblems/problem1.cnf
15 1
5 0
12 0
7 0
17 1
20 1
16 0
19 0
1 1
11 0
3 0
14 1
18 0
2 0
10 0
6 1
8 0
13 1
9 0
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver.py FILE=SATproblems/problem2.cnf
7 1
22 1
27 0
43 1
50 0
38 1
34 1
41 0
46 0
17 0
6 0
4 0
16 1
40 1
19 1
29 1
45 1
36 0
15 0
2 0
30 1
35 1
8 0
47 0
28 0
33 1
37 1
21 0
14 0
44 1
9 0
13 0
31 1
42 1
18 0
12 0
48 0
1 0
49 0
32 0
11 0
3 1
5 1
20 0
25 0
23 1
39 0
10 1
26 0
24 1
dan@ubuntu:~/aiclass/hw3/problem1$ cd ..
dan@ubuntu:~/aiclass/hw3$ ls
dauerbac_0.txt                tenn_district2.py
dauerbac_almost.txt           tenn_district2.py~
dauerbac_final.txt            tenn_district3.py
dauerbach.txt~                tenn_district3.py~
dauerbac@unix.andrew.cmu.edu  tenn_district4.py
hillclimb.py                  tenn_district_p3_2.py
hillclimb.py~                 tenn_district_p3_2.py~
hillclimbresults.txt          tenn_district_p3_3.py
jump1.txt                     tenn_district_p3_3.py~
jump_prom0.txt                tenn_district_p3.py
jump_prom1.txt                tenn_district_p3.py~
modstart_0.txt                tenn_district.py
modstart_0.txt~               tenn_district.py~
neighbors.txt                 tennessee_dauerbac.txt
over7_69.csv                  test.py
over7_74.csv                  tmp_jump.txt
over7_74.csv~                 tmp_jump.txt~
[0m[01;34mproblem1[0m                      tracts.txt
start_jump.txt                vis.txt
start_jump.txt~               vis.txt~
[mdan@ubuntu:~/aiclass/hw3$ cd problem1
dan@ubuntu:~/aiclass/hw3/problem1$ ls
box25.jpg                     problem6.out
box50.jpg                     problem8.out
box_clause.png                QQQ11.out
box_confs.png                 QQQ1.out
box_dpll.jpg                  qqq_2.out
box_dpll.png                  QQQ2.out
[0m[01;32mbuild.sh[0m                      QQQ3.out
[01;32mbuild.sh~[0m                     [01;34mQtestn25[0m
cdb_expanded_solver.py        [01;34mQtestn50[0m
cdb_solver.py                 randomcdf.py
clauselearningsolver.py       randomcdf.py~
clauselearningsolver.py~      randtimes
clauselearningsolver.pyc      randtimes~
clause.txt                    RealSRcdf.jpg
clause.txt~                   results_pruned.txt
conf2.txt                     results_pruned.txt~
conf2.txt~                    results.txt
confdirbacksolver.py          results.txt~
confdirbacksolver.py~         run_debug.txt
confdirbacksolver.pyc         [01;32mrun.sh[0m
conf.txt                      run.sh~
conf.txt~                     SATgenerator.py
dauerbac@unix.andrew.cmu.edu  SATgenerator.py~
dpll50.txt                    [01;34mSATproblems[0m
dpll50.txt~                   satsolver2.py
dpllsolver_dauerbac.py        satsolver2.py~
dpllsolver_dauerbac.py~       satsolver3a.py
dpllsolver_dauerbac.pyc       satsolver3a.py~
dpll_solver.py                satsolver3b.py
dpll_solver.py~               satsolver3b.py~
dpll_solver_test.py           satsolver3c.py
dpll_solver_test.py~          satsolver3c.py~
example.R                     satsolver3.py
example.R~                    satsolver3.py~
expanded_solver2.py           satsolver4.py
expanded_solver2.py~          satsolver4.py~
expanded_solver.py            satsolver5.py
expanded_solver.py~           satsolver5.py~
expanded_solver_t2.py         satsolver6.py
expanded_solver_t2.py~        satsolver6.py~
FORSHARE_solver.py            satsolver7.py
FORSHARE_solver.py~           satsolver7.py~
hhh.out                       satsolver8.py
hw3_tmp.out                   satsolver8.py~
hw3_tmp.out~                  satsolver.py
IdealSRcdf.jpg                satsolver.py~
mean_vs_beta.png              satsolverrec.py
mmmm.out                      SRcdf.jpg
p3_11.out                     tester.py
p3_11.out~                    tester.py~
p3Rdat25                      testfile.cnf
p3Rdat25~                     [01;34mtestn25[0m
p3Rdat25.dat                  [01;34mtestn50[0m
p3Rdat50.dat                  test.out
p3Rdat50.dat~                 tmp
problem1_rand.out             tmp~
problem1_t2.out               tmp50.jpg
problem1_v3.out               tmp.jpg
problem1_v3.out~              tmpl.out
problem2_2.out                tmp.out
problem2_2.out~               tmp.out~
problem2.out                  tmpout.out
problem2.out~                 tout1.out
problem2_rand.out             tout2.out
problem2_rand.out~            tout3.out
problem2_v3.out               tout4.out
problem3.out                  tout5.out
problem3output.txt            tout6.out
problem3right.txt             tout7.out
problem3right.txt~            [01;34mverifier[0m
problem4.out
[mdan@ubuntu:~/aiclass/hw3/problem1$ ls -l | test
dan@ubuntu:~/aiclass/hw3/problem1$ ls -l | grep test
-rw-r--r-- 1 dan dan       107 2011-04-04 05:19 dpll_solver_test.py
-rw-r--r-- 1 dan dan       106 2011-04-04 05:19 dpll_solver_test.py~
drwxr-xr-x 2 dan dan     20480 2011-03-01 18:47 Qtestn25
drwxr-xr-x 2 dan dan     20480 2011-03-01 18:47 Qtestn50
-rw-r--r-- 1 dan dan      1615 2011-03-03 01:31 tester.py
-rw-r--r-- 1 dan dan      1604 2011-03-03 00:20 tester.py~
-rw-r--r-- 1 dan dan       169 2011-03-01 18:47 testfile.cnf
drwxr-xr-x 2 dan dan     20480 2011-03-01 18:47 testn25
drwxr-xr-x 2 dan dan     20480 2011-03-01 18:47 testn50
-rw-r--r-- 1 dan dan   2043611 2011-03-01 18:47 test.out
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver.py SATproblems/problem1.cnf
Please specify input file via FILE=<filename> argument.
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver.py FILE=SATproblems/problem1.cnf
15 1
5 0
12 0
7 0
17 1
20 1
16 0
19 0
1 1
11 0
3 0
14 1
18 0
2 0
10 0
6 1
8 0
13 1
9 0
dan@ubuntu:~/aiclass/hw3/problem1$ ls
box25.jpg                     problem6.out
box50.jpg                     problem8.out
box_clause.png                QQQ11.out
box_confs.png                 QQQ1.out
box_dpll.jpg                  qqq_2.out
box_dpll.png                  QQQ2.out
[0m[01;32mbuild.sh[0m                      QQQ3.out
[01;32mbuild.sh~[0m                     [01;34mQtestn25[0m
cdb_expanded_solver.py        [01;34mQtestn50[0m
cdb_solver.py                 randomcdf.py
clauselearningsolver.py       randomcdf.py~
clauselearningsolver.py~      randtimes
clauselearningsolver.pyc      randtimes~
clause.txt                    RealSRcdf.jpg
clause.txt~                   results_pruned.txt
conf2.txt                     results_pruned.txt~
conf2.txt~                    results.txt
confdirbacksolver.py          results.txt~
confdirbacksolver.py~         run_debug.txt
confdirbacksolver.pyc         [01;32mrun.sh[0m
conf.txt                      run.sh~
conf.txt~                     SATgenerator.py
dauerbac@unix.andrew.cmu.edu  SATgenerator.py~
dpll50.txt                    [01;34mSATproblems[0m
dpll50.txt~                   satsolver2.py
dpllsolver_dauerbac.py        satsolver2.py~
dpllsolver_dauerbac.py~       satsolver3a.py
dpllsolver_dauerbac.pyc       satsolver3a.py~
dpll_solver.py                satsolver3b.py
dpll_solver.py~               satsolver3b.py~
dpll_solver_test.py           satsolver3c.py
dpll_solver_test.py~          satsolver3c.py~
example.R                     satsolver3.py
example.R~                    satsolver3.py~
expanded_solver2.py           satsolver4.py
expanded_solver2.py~          satsolver4.py~
expanded_solver.py            satsolver5.py
expanded_solver.py~           satsolver5.py~
expanded_solver_t2.py         satsolver6.py
expanded_solver_t2.py~        satsolver6.py~
FORSHARE_solver.py            satsolver7.py
FORSHARE_solver.py~           satsolver7.py~
hhh.out                       satsolver8.py
hw3_tmp.out                   satsolver8.py~
hw3_tmp.out~                  satsolver.py
IdealSRcdf.jpg                satsolver.py~
mean_vs_beta.png              satsolverrec.py
mmmm.out                      SRcdf.jpg
p3_11.out                     tester.py
p3_11.out~                    tester.py~
p3Rdat25                      testfile.cnf
p3Rdat25~                     [01;34mtestn25[0m
p3Rdat25.dat                  [01;34mtestn50[0m
p3Rdat50.dat                  test.out
p3Rdat50.dat~                 tmp
problem1_rand.out             tmp~
problem1_t2.out               tmp50.jpg
problem1_v3.out               tmp.jpg
problem1_v3.out~              tmpl.out
problem2_2.out                tmp.out
problem2_2.out~               tmp.out~
problem2.out                  tmpout.out
problem2.out~                 tout1.out
problem2_rand.out             tout2.out
problem2_rand.out~            tout3.out
problem2_v3.out               tout4.out
problem3.out                  tout5.out
problem3output.txt            tout6.out
problem3right.txt             tout7.out
problem3right.txt~            [01;34mverifier[0m
problem4.out
[mdan@ubuntu:~/aiclass/hw3/problem1$ cat satsolver.py
#!/usr/bin/python2.6
# author: Dan Auerbach (dtauerbach@gmail.com)
# TODO make debugging infrastructure
# any time the set of clauses changes at all
# print the change and the rule that led to it
# when debug flag is on

import sys 
import copy

LOAD_FILENAME = None
DEBUG = False
RANDOM_BRANCH = False
TIMING_DEBUG = False

if not sys.argv:
  print """No command line arguments given. Required argument
is LOAD_FILENAME; optional arguments are DEBUG, FILE_BASE_DIR"""
for a in sys.argv:
  if a[:14] == "LOAD_FILENAME=":
    LOAD_FILENAME = a[14:]
  elif a[:5] == "FILE=":
    LOAD_FILENAME = a[5:]
  if a[:7] == "DEBUG=1" or a=="DEBUG":
    DEBUG = 1
  if a[:4] == "RAND":
    RANDOM_BRANCH = True

# TODO make these flags
FILE_BASE_DIR = "/home/dan/Downloads/PS2/SATproblems/"

# Used as argument for sorting lists of tuples
def _listcomp(a, b):
  if len(a) < len(b): return -1
  if len(b) < len(a): return 1
  return cmp(a, b)


class DPLLSolver:
  """Where the magic happens."""

  literal_clause_dict = {}

  def ReadInCNFFile(self, filename):
    """
    Args:
      file: (str) file path of CNF file
    Returns:
      clauses, num_vars: sorted list of lists of ints, int 
    """
    if DEBUG:
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
    if DEBUG:
      print "len: " + str(len(clauses))
      print "num: " + str(num_clauses)
    if num_clauses != len(clauses):
      raise Exception, "error reading in cnf file"
    file.close()
    return clauses, num_vars
  
  def Dedup(self, clauses):
    """
    Args:
      clauses (sorted list of lists of ints)
    Returns:
      clauses: same as arg
    """
    if not clauses:
      return
    deduped_clauses = [clauses[0]]
    for i in xrange(len(clauses)-1):
      if clauses[i+1]!=clauses[i]:
        deduped_clauses.append(clauses[i+1])
    return deduped_clauses

  def HandleSingleLiterals(self, clauses):
    single_literals = []
    # Check to make sure clauses isn't empty, i.e. we are already
    # satisfiable, and don't have to assign any more variables
    if self.IsSat(clauses): return [], []
    if self.IsUnsat(clauses): return False
    for c in clauses:
      if len(c) == 1:
        # Test to make sure p and -p aren't both single lits
        # If they are, clauses is unsat so return {{},}
        # Note it is ok to only check single_literals in local
        # scope since we below we remove negated literals from
        # all clauses.
        if -c[0] in single_literals:
          if DEBUG:
            print "Unsatisfiable: as {p} and {-p} are both clauses"
          return [[],], []
        single_literals.append(c[0])
      if len(c) > 1:
        # List is sorted so no need to check all
        break
    single_literals = list(set(single_literals))
    clauses = self.RemoveClauses(clauses, single_literals)
    clauses = self.RemoveNegatedLiterals(clauses, single_literals)
    # Clauses are sorted in RemoveNegatedLiterals
    return clauses, single_literals

  def RemoveClausesIter(self, clauses, literals):
    tbr_clauses = []
    if not literals:
      return clauses
    # Remove clauses with that literal
    for c in clauses:
      for lit in literals:
        if lit[0] in c:
          tbr_clauses.append(c)
          break
    tbr_clauses.sort(_listcomp)
    new_clauses = []
    for c in clauses:
      if not c in tbr_clauses:
        new_clauses.append(c)
    return new_clauses
    
  def RemoveClauses(self, clauses, literals):
    tbr_clauses = []
    if not literals:
      return clauses
    # Remove clauses with that literal
    for c in clauses:
      for lit in literals:
        if lit in c:
          tbr_clauses.append(c)
          break
    tbr_clauses.sort(_listcomp)
    new_clauses = []
    for c in clauses:
      if not c in tbr_clauses:
        new_clauses.append(c)
    return new_clauses

  def RemoveNegatedLiteralsIter(self, clauses, literals):
    """Remove the negation of any single literal from clauses."""
    if not clauses: return []
    new_clauses = []
    negated_lits = [-lit[0] for lit in literals]
    # debugging
    #if -7 in negated_lits:
    #  print "YESSIR"
    for c in clauses:
      new_c = list(set(c).difference(set(negated_lits)))
      new_c.sort()
      new_clauses.append(new_c)
      #debugging
      #if 10 in new_c:
      #  print "HERE: %s" % str(new_c)
    new_clauses.sort(_listcomp)
    return self.Dedup(new_clauses)

  
  def RemoveNegatedLiterals(self, clauses, literals):
    """Remove the negation of any single literal from clauses."""
    if not clauses: return []
    new_clauses = []
    negated_lits = [-lit for lit in literals]
    # debugging
    #if -7 in negated_lits:
    #  print "YESSIR"
    for c in clauses:
      new_c = list(set(c).difference(set(negated_lits)))
      new_c.sort()
      new_clauses.append(new_c)
      #debugging
      #if 10 in new_c:
      #  print "HERE: %s" % str(new_c)
    new_clauses.sort(_listcomp)
    return self.Dedup(new_clauses)

  # TODO This function needs testing
  def RemovePureLiteralClauses(self, clauses):
    if not clauses: return clauses, []
    pure_literals = []
    self.UpdateDict(clauses)
    #print "Dict is: %s" % str(self.literal_clause_dict)
    for d in self.literal_clause_dict:
      tmp_dict = self.literal_clause_dict[d]
      if tmp_dict['pos'] == 0:
        pure_literals.append(-d)
      elif tmp_dict['neg'] == 0:
        pure_literals.append(d)
    # Next line unnecessary
    # pure_literals = list(set(pure_literals))
    clauses = self.RemoveClauses(clauses, pure_literals)
    if DEBUG:
      print "After removing pure literals, clauses are: %s" % str(clauses)
    return clauses, pure_literals

  # TODO needs testing. not working, fix!
  def ChooseBestLiteral(self, clauses):
    """Takes best literal from our literal_clause_dict."""
    self.UpdateDict(clauses)
    if not self.literal_clause_dict:
      raise Exception, "Literal clause dict empty"
    max_sum = 0
    max_lit = 0
    value_neg = 0
    for d in self.literal_clause_dict:
      cur = self.literal_clause_dict[d] 
      if max(cur['pos'], cur['neg']) > max_sum:
        max_sum = max(cur['pos'], cur['neg'])
        max_lit = d
        # Maybe set a flag here to turn on value ordering
        if cur['pos'] < cur['neg']:
          value_neg = 1
    return max_lit, value_neg

  def IsSat(self, clauses):
    if not clauses:
      return True

  def IsUnsat(self, clauses):
    for c in clauses:
      if len(c) == 0:
        return True
  
  def SolveAndOutput(self, problem_str):
    """Wrapper to RecursiveDPLL, prints solution"""
    clauses, num = self.ReadInCNFFile(FILE_BASE_DIR + problem_str + ".cnf")
    res = self.IterativeDPLL(clauses)
    if not res:
      print "UNSATISFIABLE"
    else:
      for lit in map(lambda x: x[0], res[1]):
        if lit > 0:
          print "%s 1" % str(lit)
        else:
          print "%s 0" % str(-lit)

  def IterativeDPLL(self, clauses):
    """Iterative implementation."""
    # We keep track of assigned literals as a
    # list of pairs. The first member is the literal
    # and the second is a boolean indicating whether
    # the literal was added as part of a resolution
    # step (False means derived)
    cur_lits = []
    clauses, cur_lits = self.Propagate(clauses, [])
    # After one propagation on full set of clauses, test for sat or unsat
    if not clauses: return True, cur_lits
    if not clauses[0]: return False
    while True:
      tmp = self.ChooseBestLiteralIter(clauses, cur_lits)
      if tmp:
        cur_lits.append((tmp, True))
        if DEBUG:
          print "Resolution on %d. Current state is %s" % (tmp, str(cur_lits))
      cls, cur_lits = self.Propagate(clauses, cur_lits)
      # Test temporary cls to see if we are sat or unsat
      if not cls: return True, cur_lits
      if not cls[0]:
        # Find the last literal we chose via resolution, and flip it
        # As that flipped literal must be that way, set the second of 
        # the pair to False
        cur_lits = self.FlipLastResoLiteral(cur_lits)
        if not cur_lits:
          # Then nothing left to change, we are unsat
          return False

  def ChooseBestLiteralIter(self, clauses, lits):
    """Takes best literal from our literal_clause_dict."""
    literal_clause_dict = self.GenerateDict(clauses, lits)
    if not literal_clause_dict:
      # This means there is no more literals to choose from
      # And we are unsatisfiable
      return None
    max_sum = 0
    max_lit = 0
    value = 1
    for d in literal_clause_dict:
      cur = literal_clause_dict[d] 
      if max(cur['pos'], cur['neg']) > max_sum:
        max_sum = max(cur['pos'], cur['neg'])
        max_lit = d
        # Maybe set a flag here to turn on value ordering
        if cur['pos'] < cur['neg']:
          value = -1
        else:
          value = 1
    return value*max_lit

  def FlipLastResoLiteral(self, literals):
    """Finds last pair in literals of the form (p, True),
    replaces that with (-p, False) and returns sublist up
    to that member.
    Args: 
      literals: list of pairs (lit, bool)
    Returns:
      literals: list of pairs (lit, bool)
    """
    while literals:
      tmp = literals.pop()
      if tmp[1]: 
        literals.append((-tmp[0], False))
        if DEBUG:
          print "Conflict on %d. Flipping. Current state is %s." % (tmp[0], str(literals))
        return literals
    return []

  def Propagate(self, clauses, lits):
    while True: 
      old_clauses = clauses
      clauses, lits = self.HandleSingleLiteralsIter(clauses, lits)
      if clauses and len(clauses) < len(old_clauses):
        continue
      clauses, pure = self.RemovePureLiteralClausesIter(clauses)
      lits.extend(pure)
      if not clauses or not clauses[0]: return clauses, lits
      if len(clauses) == len(old_clauses):
        break
    return clauses, lits

  def HandleSingleLiteralsIter(self, clauses, literals):
    if not clauses or not clauses[0]: return clauses, literals
    new_lits = copy.copy(literals)
    for c in clauses:
      if len(c) == 1:
        # Test to make sure p and -p aren't both single lits
        # If they are, clauses is unsat so return {{},}
        # Note it is ok to only check literals in local
        # scope since we below we remove negated literals from
        # all clauses.
        if -c[0] in map(lambda x: x[0], new_lits):
          if DEBUG:
            print "Conflict reached: %d. Current state is %s" % (c[0], str(literals))
            #print "new lits: %s" % str(new_lits)
            #print "clauses: %s" % str(clauses)
          # Important we return 'literals' here, throw out garbage 'new_lits'
          return [[],], literals
        if not c[0] in map(lambda x: x[0], new_lits):
          new_lits.append((c[0], False))
      if len(c) > 1:
        # List is sorted by len so no need to check all
        break
    #new_lits = list(set(new_lits))
    #print "literals: %s\nnew_lits: %s" % (str(literals), str(new_lits))
    clauses = self.RemoveClausesIter(clauses, new_lits)
    clauses = self.RemoveNegatedLiteralsIter(clauses, new_lits)
    # Clauses are sorted in RemoveNegatedLiterals
    #print "now new_lits %s" % str(new_lits)
    return clauses, new_lits
 
  def RemovePureLiteralClausesIter(self, clauses):
    if not clauses: return clauses, []
    pure_literals = []
    literal_clause_dict = self.GenerateDict(clauses, [])
    #print "Dict is: %s" % str(literal_clause_dict)
    for d in literal_clause_dict:
      tmp_dict = literal_clause_dict[d]
      if tmp_dict['pos'] == 0:
        pure_literals.append((-d, False))
      elif tmp_dict['neg'] == 0:
        pure_literals.append((d, False))
    # Next line unnecessary
    # pure_literals = list(set(pure_literals))
    clauses = self.RemoveClauses(clauses, pure_literals)
    return clauses, pure_literals

  # TODO use fixed lookup table based on num vars
  def GenerateDict(self, clauses, literals):
    """Generates dict of how often lits occur in clauses,
    except those in literals, which are ignored.
    """
    if not clauses: return {}
    literal_clause_dict = {}
    lits = map(lambda x: x[0], literals)
    for c in clauses:
      for lit in c:
        # Skip things in lits
        if lit in lits or -lit in lits:
          continue
        if lit > 0:
          if abs(lit) in literal_clause_dict:
            literal_clause_dict[abs(lit)]['pos'] += 1
          else:
            literal_clause_dict[abs(lit)] = {'pos': 1, 'neg': 0}
        else:
          if abs(lit) in literal_clause_dict:
            literal_clause_dict[abs(lit)]['neg'] += 1
          else:
            literal_clause_dict[abs(lit)] = {'pos': 0, 'neg': 1}
    return literal_clause_dict

  def RecursiveDPLL(self, clauses):
    """The main loop. Recursive DPLL implementation."""
    if self.IsSat(clauses):
      return True, []
    if self.IsUnsat(clauses):
      return False
    old_clauses = []
    # Keeps track of satisfying variables
    satisfying_lits = []
    while True: 
      old_clauses = clauses
      clauses, lits = self.HandleSingleLiterals(clauses)
      # Make sure we log the extending variables
      satisfying_lits.extend(lits)
#      if clauses and len(clauses) < len(old_clauses):
#        continue
      clauses, pure = self.RemovePureLiteralClauses(clauses)
      satisfying_lits.extend(pure)
      #print "After pure: %s" % str(satisfying_lits)
      if self.IsSat(clauses):
        return True, satisfying_lits
      if self.IsUnsat(clauses):
        #print "yes, it's unsat"
        return False
      if len(clauses) == len(old_clauses):
        break
    lit, val = self.ChooseBestLiteral(clauses)
    # Debugging
    # print "lit, val : %s,%s" % (str(lit), str(val))
    clauses1 = copy.copy(clauses)
    clauses.append([lit,])
    clauses.sort(_listcomp)
    clauses1.append([-lit,])
    clauses1.sort(_listcomp)
    all_clauses = [clauses, clauses1]
    # Value ordering based on indexing of all_clauses
    for i in xrange(2):
      #print "Starting resolution split on %d" % lit
      if DEBUG:
        print "Full clauses are: %s." % str(all_clauses[(i+1)%2])
      res = self.RecursiveDPLL(all_clauses[(i+1)%2])
      if not res and DEBUG:
        print "Reso unsat for: %s." % str(all_clauses[(i+1)%2])
      if res:
        satisfying_lits.extend(res[1])
        #print "After resolution: %s" % str(satisfying_lits)
        #if DEBUG:
        #  print "Full clauses are: %s" % str(res[1])
        return True, satisfying_lits
    return False

  def UpdateDict(self, clauses):
    self.literal_clause_dict = {}
    if not clauses: return
    for c in clauses:
      for lit in c:
        if lit > 0:
          if abs(lit) in self.literal_clause_dict:
            self.literal_clause_dict[abs(lit)]['pos'] += 1
          else:
            self.literal_clause_dict[abs(lit)] = {'pos': 1,
                                                  'neg': 0}
        else:
          if abs(lit) in self.literal_clause_dict:
            self.literal_clause_dict[abs(lit)]['neg'] += 1
          else:
            self.literal_clause_dict[abs(lit)] = {'pos': 0,
                                                  'neg': 1}



dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
Traceback (most recent call last):
  File "dpll_solver_test.py", line 48, in <module>
    _TestUnitPropagate()
  File "dpll_solver_test.py", line 37, in _TestUnitPropagate
    res = _TEST_SOLVER.UnitPropagate()
  File "/home/dan/aiclass/hw3/problem1/dpll_solver.py", line 244, in UnitPropagate
    self.underived.append(False)
AttributeError: _DPLLSolver instance has no attribute 'underived'
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
Traceback (most recent call last):
  File "dpll_solver_test.py", line 50, in <module>
    _TestUnitPropagate()
  File "dpll_solver_test.py", line 38, in _TestUnitPropagate
    _ResetState(_TEST_CLAUSE, [])
TypeError: _ResetState() takes exactly 1 argument (2 given)
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
yeah boyee
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
Traceback (most recent call last):
  File "dpll_solver_test.py", line 56, in <module>
    _TestUnitPropagate()
  File "dpll_solver_test.py", line 40, in _TestUnitPropagate
    res = _TEST_SOLVER.UnitPropagate()
  File "/home/dan/aiclass/hw3/problem1/dpll_solver.py", line 244, in UnitPropagate
    self.underived.append(False)
AttributeError: _DPLLSolver instance has no attribute 'underived'
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
Traceback (most recent call last):
  File "dpll_solver_test.py", line 59, in <module>
    _TestFilterClauses()
  File "dpll_solver_test.py", line 52, in _TestFilterClauses
    assert (len(res)==1 and res[0]==1)
AssertionError
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
[[2]]
Traceback (most recent call last):
  File "dpll_solver_test.py", line 60, in <module>
    _TestFilterClauses()
  File "dpll_solver_test.py", line 53, in _TestFilterClauses
    assert (len(res)==1 and res[0]==1)
AssertionError
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
[[2]]
Traceback (most recent call last):
  File "dpll_solver_test.py", line 60, in <module>
    _TestFilterClauses()
  File "dpll_solver_test.py", line 53, in _TestFilterClauses
    assert (len(res)==1 and res[0]==1)
AssertionError
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
[[2]]
Traceback (most recent call last):
  File "dpll_solver_test.py", line 60, in <module>
    _TestFilterClauses()
  File "dpll_solver_test.py", line 53, in _TestFilterClauses
    assert (len(res)==1 and res[0]==2)
AssertionError
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
[[2]]
yeah boyee
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
  File "dpll_solver_test.py", line 56
    res = _TEST_SOLVER.NaiveBacktrack()
      ^
SyntaxError: invalid syntax
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
Traceback (most recent call last):
  File "dpll_solver_test.py", line 62, in <module>
    _TestNaiveBacktrack()
  File "dpll_solver_test.py", line 56, in _TestNaiveBacktrack
    res = _TEST_SOLVER.NaiveBacktrack()
  File "/home/dan/aiclass/hw3/problem1/dpll_solver.py", line 278, in NaiveBacktrack
    if self.last_true_index == -1:
AttributeError: _DPLLSolver instance has no attribute 'last_true_index'
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
1
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Please specify input file via FILE=<filename> argument.
1
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver.py FILE=SATproblems/problem1.cnf
15 1
5 0
12 0
7 0
17 1
20 1
16 0
19 0
1 1
11 0
3 0
14 1
18 0
2 0
10 0
6 1
8 0
13 1
9 0
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
Traceback (most recent call last):
  File "dpll_solver_test.py", line 75, in <module>
    _TestJeroslowWang()
  File "dpll_solver_test.py", line 68, in _TestJeroslowWang
    assert(res==4)
AssertionError
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver_test.py
dan@ubuntu:~/aiclass/hw3/problem1$ python dpll_solver.py FILE=SATproblems/problem1.cnf
15 1
5 0
12 0
7 0
17 1
20 1
16 0
19 0
1 1
11 0
3 0
14 1
18 0
2 0
10 0
6 1
8 0
13 1
9 0
dan@ubuntu:~/aiclass/hw3/problem1$ cp dpll_solver* ~/git/Dan-Code-Sample-for-EFF/
dan@ubuntu:~/aiclass/hw3/problem1$ cp SATproblems/* ~/git/Dan-Code-Sample-for-EFF/
dan@ubuntu:~/aiclass/hw3/problem1$ cd ~/git/Dan-Code-Sample-for-EFF/
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ ls
dantest2.cnf      dpll_solver_test.py   problem4.cnf
dantest2.cnf~     dpll_solver_test.py~  problem5.cnf
dantest.cnf       problem10.cnf         problem6.cnf
dantest.cnf~      problem11.cnf         problem7.cnf
Dan_unsat_1.cnf   problem12.cnf         problem8.cnf
Dan_unsat_1.cnf~  problem1.cnf          problem9.cnf
dpll_solver.py    problem1.cnf~         README
dpll_solver.py~   problem2.cnf          satsolver.py
dpll_solver.pyc   problem3.cnf          satsolver.py~
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ cat README
This repository contains one primary file dpll_solver.py which is a python-bas\
ed
implementation of a SAT solver that uses the DPLL algorithm. The solver
implements cascading unit propagation and allows several variable ordering
heuristics to be used based on command-line flags.

The repository also includes some test SAT problems in DIMACS CNF format.

Example usage:

python dpll_solver.py FILE=testdata/problem1.cnf
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ mkdir testdata
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ mv problem*.cnf testdata/
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ ls
dantest2.cnf      dpll_solver.py        README
dantest2.cnf~     dpll_solver.py~       satsolver.py
dantest.cnf       dpll_solver.pyc       satsolver.py~
dantest.cnf~      dpll_solver_test.py   [0m[01;34mtestdata[0m
Dan_unsat_1.cnf   dpll_solver_test.py~
Dan_unsat_1.cnf~  problem1.cnf~
[mdan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ cd testdata
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ ls
problem10.cnf  problem1.cnf  problem4.cnf  problem7.cnf
problem11.cnf  problem2.cnf  problem5.cnf  problem8.cnf
problem12.cnf  problem3.cnf  problem6.cnf  problem9.cnf
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ rm problem10.cnf
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ rm problem11.cnf
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ rm problem12.cnf
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ ls
problem1.cnf  problem4.cnf  problem7.cnf
problem2.cnf  problem5.cnf  problem8.cnf
problem3.cnf  problem6.cnf  problem9.cnf
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ git add *
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF/testdata$ cd ..
dan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ ls
dantest2.cnf      dpll_solver.py        README
dantest2.cnf~     dpll_solver.py~       satsolver.py
dantest.cnf       dpll_solver.pyc       satsolver.py~
dantest.cnf~      dpll_solver_test.py   [0m[01;34mtestdata[0m
Dan_unsat_1.cnf   dpll_solver_test.py~
Dan_unsat_1.cnf~  problem1.cnf~
[mdan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ ls
dantest2.cnf      dpll_solver.py        README
dantest2.cnf~     dpll_solver.py~       satsolver.py
dantest.cnf       dpll_solver.pyc       satsolver.py~
dantest.cnf~      dpll_solver_test.py   [0m[01;34mtestdata[0m
Dan_unsat_1.cnf   dpll_solver_test.py~
Dan_unsat_1.cnf~  problem1.cnf~
[mdan@ubuntu:~/git/Dan-Code-Sample-for-EFF$ 