#
# colors_example.py
#
# A python executable that demontrates the usages of colors.py
#
# Warning: Color output may fail depending on your OS and the current
#          background of your terminal/command prompt.
# 
# Name: Chris Wolf
# E-mail: chriswolfdesign@gmail.com
# Version: July 8, 2017
#

from colors import *

if __name__ == '__main__':
	
	print
	print '-------------------------------------------------------------------'
	print 'Demonstration of module: colors.py'
	print
	print 'Module attempts to color code text output to aid user in debugging'
	print 'Warning: Some tests may fail depending on your Os and the '
	print '         current background of your terminal/command prompt.'
	print '-------------------------------------------------------------------'
	print

	print red('This text should be red!')
	print blue('This text should be blue!')
	print green('This text should be green!')
	print black('This text should be black!')
	print
