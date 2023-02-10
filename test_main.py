from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36 #TODO
	assert simple_work_calc(20, 3, 2) == 230 #TODO
	assert simple_work_calc(30, 4, 2) == 650 #TODO
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 65
	assert simple_work_calc(8, 4, 2) == 120

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO
	assert work_calc(8, 2, 2, lambda n: 1) == 15
	assert work_calc(8, 1, 2, lambda n: n*n) == 85
	assert work_calc(8, 3, 2, lambda n: n) == 65
