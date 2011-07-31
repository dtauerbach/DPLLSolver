#!/usr/bin/python2.7
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
import unittest

_FILE_BASE_DIR = "testdata"
_TEST_CLAUSE = [[1], [2,-1], [1,2,3]]
_TEST_CLAUSE_2 = [[3, 4], [5], [1,-1,5], [-3, 2], [-2, -4]]

class TestDPLLSolver(unittest.TestCase):
  
  def setUp(self):
    self.resetState([], [])

  def resetState(self, clauses, lits):
    """Resets the state of clauses and literals for testing."""
    self._TEST_SOLVER = dpll_solver._DPLLSolver()
    self._TEST_SOLVER.clauses = clauses
    self._TEST_SOLVER.lits = lits
    self._TEST_SOLVER.lit_dict = {}
    self._TEST_SOLVER.underived = []
    for i in xrange(len(lits)):
      self._TEST_SOLVER.lit_dict[lits[i]] = True 
      # For our test case, we coerce all literals
      self._TEST_SOLVER.underived.append(True)
    self._TEST_SOLVER.last_true_index = -1

  def tearDown(self):
    pass

  def testReadInCNFFile(self):
    res = self._TEST_SOLVER.ReadInCNFFile(_FILE_BASE_DIR + "/problem1.cnf")
    assert(res[1]==20)
    assert(len(res[0])==91)

  def testUnitPropagate(self):
    self.resetState(_TEST_CLAUSE, [])
    res = self._TEST_SOLVER.UnitPropagate()
    assert(res == 1)

    self.resetState(_TEST_CLAUSE_2, [])
    res = self._TEST_SOLVER.UnitPropagate()
    assert(res == 0)

  def testFilterClauses(self):
    self.resetState(_TEST_CLAUSE, [1])
    res = self._TEST_SOLVER.FilterClauses()
    assert(len(res)==1 and len(res[0])==1 and res[0][0]==2)

  def testNaiveBacktrack(self):
    self.resetState(_TEST_CLAUSE, [1, 2, 3])
    res = self._TEST_SOLVER.NaiveBacktrack()
    assert(not res)

  def testMomsHeuristic(self):
    res = self._TEST_SOLVER.MomsHeuristic(_TEST_CLAUSE)
    assert(res==1)

  def testJeroslowWang(self):
    res = self._TEST_SOLVER.JeroslowWang(_TEST_CLAUSE)
    assert(res==1)

if __name__ == '__main__':
    unittest.main()
