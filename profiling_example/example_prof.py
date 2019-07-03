import time

def sum(n):
	sum = 0
	time.sleep(0.2) # tidstung operation
	for x in xrange(0,n):
		sum += x
	return sum

for x in xrange(1,10):
	print('sum({})={}'.format(x, sum(x)))

