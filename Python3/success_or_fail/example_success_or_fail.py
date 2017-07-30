#
# example_success_or_fail.py
#
# This program displays an exaplanation and demonstration of how to use
# success_or_fail.py
#
# Name: Chris Wolf
# E-mail: chriswolfdesign@gmail.com
# Version: July 8, 2017
#

from success_or_fail import *

if __name__ == '__main__':

	print()
	print('-------------------------------------------------------------------')
	print('success_or_fail.py')
	print()
	print('This module allows the user to add functions into their programs')
	print('that will color code their output along with success or fail')
	print('statements that will inform them of how their debugging is going.')
	print()
	print('Warning: These functions needs to be added to conditional')
	print('         in your own code.  This module does not actually debug')
	print('         for you.  It only presents your debugging statements')
	print('         in an organized and easy to follow manner.')
	print('-------------------------------------------------------------------')

	expected_name = 'Chris'

	# Display an example of success() being performed
	test_name = 'Chris'

	print()
	print('-------------------------------------------------------------------')
	print('Example: success()')
	print('Function call: success(\'Chris == Chris\')')
	print('-------------------------------------------------------------------')

	if expected_name == test_name:
		success('Chris == Chris')
	else:
		fail('Chris == Chris', expected_name, test_name)

	# Display an example of fail() being performed
	test_name = 'chris'

	print()
	print('-------------------------------------------------------------------')
	print('Example: fail()')
	print('Function call: fail(\'Chris == chris\'), expected_name, test_name)')
	print('-------------------------------------------------------------------')

	if expected_name == test_name:
		success('Chris == chris')
	else:
		fail('Chris == chris', expected_name, test_name)
