import time

#-------------------------------------------------------------------------------

def timestamp(message, *variables):

	date = time.asctime( time.localtime(time.time()) )

	print( '{}: '.format(date) + message.format(*variables) + '\n' )

#-------------------------------------------------------------------------------

def copyright_notice():

	line1 = 'ExVol Copyright (C) 2022 Tomasz Skóra tskora@ichf.edu.pl'
	line2 = 'This program comes with ABSOLUTELY NO WARRANTY;'
	line3 = 'This is free software, and you are welcome to redistribute it'
	line4 = 'under certain conditions; see https://www.gnu.org/licenses/ for details'
	lines = [line1, line2, line3, line4]

	n = max([len(line) for line in lines]) + 4

	print( '#'*n )
	[ print( '# ' + line + ' '*(n-len(line)-3) + '#' ) for line in lines ]
	print( '#'*n )

#-------------------------------------------------------------------------------