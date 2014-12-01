from __future__ import print_function

def ack(m, n):
	"""Return a result of the Ackermann function based on two inputs."""
	# Check for negative inputs
	if m < 0 or n < 0:
		return None
	# Ackermann series
	if m == 0:
		return n + 1
	elif n == 0:
		return ack(m - 1, 1)
	else:
		return ack(m - 1, ack(m, n - 1))