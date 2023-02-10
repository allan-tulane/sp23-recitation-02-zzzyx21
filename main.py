"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if (n != 1):
		return a*simple_work_calc(n//b, a, b) + n
	else:
		return n
	pass
	

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36 #TODO
	assert simple_work_calc(20, 3, 2) == 230 #TODO
	assert simple_work_calc(30, 4, 2) == 650 #TODO
	# additional three test
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 65
	assert simple_work_calc(8, 4, 2) == 120

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return n
	else:
		return a * work_calc(n//b, a, b, f) + f(n)
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return n
	else:
		return span_calc(n//b, a, b, f) + f(n)
	pass

def test_work():
	""" done. """
	assert work_calc(10, 2, 2,lambda n: 1) == 15 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO
	# additional three cases
	assert work_calc(8, 2, 2,lambda n: 1) == 15
	assert work_calc(8, 1, 2, lambda n: n*n) == 85
	assert work_calc(8, 3, 2, lambda n: n) == 65
	

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def curry_work_calc(a, b, f):
	# create curry work_calc to create multiple work
	return lambda n: work_calc(n, a, b, f)
	
def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	work_fn1 = curry_work_calc(3, 2, lambda n: 1)
	# create work_fn2
	work_fn2 = curry_work_calc(3, 2, lambda n: n)

	result = compare_work(work_fn1, work_fn2)
	print_results(result)

def curry_span_calc(a, b, f):
	# create curry span_calc to create multiple work
	return lambda n: span_calc(n, a, b, f)

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, span_fn1(n), span_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result

def test_compare_span():
	# TODO
	assert span_calc(10, 2, 2,lambda n: 1) == 4 #TODO
	assert span_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert span_calc(30, 3, 2, lambda n: n) == 56 #TODO
	
	# create span_fn1
	span_fn1 = curry_span_calc(3, 2, lambda n: 1)
	# create span_fn2
	span_fn2 = curry_span_calc(3, 2, lambda n: n)

	res = compare_span(span_fn1, span_fn2)
	print(res)
