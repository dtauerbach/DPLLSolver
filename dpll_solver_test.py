#!/usr/bin/python2.6
#
# Copyright 2011
# author: Dan Auerbach (dtauerbach@gmail.com)
#
# Unittest file for dpll_solver.py
#
# Methods of _DPLLSolver which were nicely
# decomposed were combined in an effort towards
# optimization. As a result, the test cases
# are a bit janky and do not provide full coverage.
#
# TODO(dtauerbach): refactor and improve tests

import dpll_solver

_FILE_BASE_DIR = "SATproblems"

# Set up our solver once glocally
_TEST_SOLVER = dpll_solver._DPLLSolver()

_TEST_CLAUSE = [[1], [2,-1], [1,2,3]]
_TEST_CLAUSE_2 = [[3, 4], [5], [1,-1,5], [-3, 2], [-2, -4]]

def _ResetState(clauses, lits):
  """Resets the state of clauses and literals for testing."""
  _TEST_SOLVER.clauses = clauses
  _TEST_SOLVER.lits = lits
  _TEST_SOLVER.lit_dict = {}
  _TEST_SOLVER.underived = []
  for i in xrange(len(lits)):
    _TEST_SOLVER.lit_dict[lits[i]] = True 
    # For our test case, we coerce all literals
    _TEST_SOLVER.underived.append(True)
  _TEST_SOLVER.last_true_index = -1

def _TestReadInCNFFile():
  res = _TEST_SOLVER.ReadInCNFFile(_FILE_BASE_DIR + "/problem1.cnf")
  assert(res[1]==20)
  assert(len(res[0])==91)

def _TestUnitPropagate():
  _ResetState(_TEST_CLAUSE, [])
  res = _TEST_SOLVER.UnitPropagate()
  assert(res == 1)

  _ResetState(_TEST_CLAUSE_2, [])
  res = _TEST_SOLVER.UnitPropagate()
  assert(res == 0)

def _TestFilterClauses():
  _ResetState(_TEST_CLAUSE, [1])
  res = _TEST_SOLVER.FilterClauses()
  assert(len(res)==1 and len(res[0])==1 and res[0][0]==2)

def _TestNaiveBacktrack():
  _ResetState(_TEST_CLAUSE, [1,2,3])
  res = _TEST_SOLVER.NaiveBacktrack()
  assert(not res)

def _TestMomsHeuristic():
  res = _TEST_SOLVER.MomsHeuristic(_TEST_CLAUSE)
  assert(res==1)

def _TestJeroslowWang():
  res = _TEST_SOLVER.JeroslowWang(_TEST_CLAUSE)
  assert(res==1)

_TestReadInCNFFile()
_TestUnitPropagate()
_TestFilterClauses()
_TestNaiveBacktrack()
_TestMomsHeuristic()
_TestJeroslowWang()
