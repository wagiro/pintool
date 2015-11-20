#!/usr/bin/env/python
#coding: utf8 
#
#prog_name= 'pintool.py'
#prog_version = '0.2'
#prog_release = '20151028'
#prog_author = 'Eduardo Garcia Melia'
#prog_author_mail = 'wagiro@gmail.com'


import sys
import string as s
import subprocess
import argparse
import re


#configure by the user
PIN = "./pin-2.13-62732-gcc.4.4.7-linux/pin"
INSCOUNT32 = "./pin-2.13-62732-gcc.4.4.7-linux/inscount0.so"
INSCOUNT64 = "./pin-2.13-62732-gcc.4.4.7-linux/source/tools/ManualExamples/obj-intel64/inscount0.so"


def start():
	
	parser = argparse.ArgumentParser(prog='pin_tool.py')
	parser.add_argument('-e', dest='study', action='store_true', default=False, help='Study the password length, for example -e -l 40, with 40 characters')
	parser.add_argument('-l', dest='len', type=str, nargs=1, default='10', help='Length of password (Default: 10 )')
	parser.add_argument('-c', dest='number', type=str, default=1, help="Charset definition for brute force\n (1-Lowercase,\n2-Uppecase,\n3-Numbers,\n4-Hexadecimal,\n5-Punctuation,\n6-All)")
	parser.add_argument('-b', dest='character', type=str, nargs=1, default='', help='Add characters for the charset, example -b _-')
	parser.add_argument('-a', dest='arch', type=str, nargs=1, default='32', help='Program architecture 32 or 64 bits, -b 32 or -b 64 ')
	parser.add_argument('-i', dest='initpass', type=str, nargs=1, default='', help='Inicial password characters, example -i CTF{')
	parser.add_argument('-s', dest='simbol', type=str, nargs=1, default='_', help='Simbol for complete all password (Default: _ )')
	parser.add_argument('-d', dest='expression', type=str, nargs=1, default='!= 0', help="Difference between instructions that are successful or not (Default: != 0, example -d '== -12', -d '=> 900', -d '<= 17' or -d '!= 32')")
	parser.add_argument('Filename',help='Program for playing with Pin Tool')


	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit()
	
	args = parser.parse_args()

	return args


def getCharset(num,addchar):
	char = ""
	charset = { '1': s.ascii_lowercase, 
				'2': s.ascii_uppercase,
				'3': s.digits,
				'4': s.hexdigits,
				'5': s.punctuation,
				'6': s.printable}
	

	if num is 1:
		return charset['1']
	else:
		num = num.split(',')

	for i in num:
		if 1 <= int(i) <= 6:
			i= '%s' % i
			char += charset[i]
		else:
			print "Number %s out of range." % (i)

	return char+''.join(addchar)


def pin(passwd):
	try:
		command = "echo " + passwd + " | " + PIN + " -t " + INSCOUNT + " -- ./"+ args.Filename + " ; cat inscount.out"
		output = subprocess.check_output(command,shell=True,stderr=subprocess.PIPE)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise

	output = re.findall(r"Count ([\w.-]+)", output)

	return int(''.join(output))


def lengthdetect(passlen):
	inicialdifference = 0
	for i in range(1,passlen+1):
		password = "_"*i
		inscount = pin(password)
		
		if inicialdifference == 0:
			inicialdifference = inscount

		print "%s = with %d characters difference %d instructions" %(password, i, inscount-inicialdifference)


def solve(initpass,passlen,symbfill,charset,expression):
	
	initlen = len(initpass)
	
	for i in range(initlen,passlen):
		
		tempassword = initpass + symbfill*(passlen-i)
		inicialdifference = 0

		for char in charset:
			
			password = tempassword[:i] + '\\'+char + tempassword[i+1:]
			inscount = pin(password)
			
			if inicialdifference == 0:
				inicialdifference = inscount

			difference = inscount-inicialdifference

			print "%s = %d difference %d instructions" %(password.replace("\\","",1), inscount, difference)
			sys.stdout.write("\033[F")

			if "!=" in expression:
				if difference != int(number):
					print "%s = %d difference %d instructions" %(password.replace("\\","",1), inscount, difference)
					initpass += char
					break
			elif "==" in expression:
				if difference == int(number):
					print "%s = %d difference %d instructions" %(password.replace("\\","",1), inscount, difference)
					initpass += char
					break
			elif "<=" in expression:
				if difference <= int(number):
					print "%s = %d difference %d instructions" %(password.replace("\\","",1), inscount, difference)
					initpass += char
					break
			elif "=>" in expression:
				if difference >= int(number):
					print "%s = %d difference %d instructions" %(password.replace("\\","",1), inscount, difference)
					initpass += char
					break
			else:
				print "Unknown value for -d option"
				sys.exit()

			if char == charset[-1]:
				print "\n\nPassword not found, try to change charset...\n"
				sys.exit()	
	
	
	return password.replace("\\","",1)


if __name__ == '__main__':

	args = start()

	initpass = ''.join(args.initpass)
	passlen = int(''.join(args.len))
	symbfill = ''.join(args.simbol)
	charset = symbfill+getCharset(args.number,args.character)
	arch = ''.join(args.arch)
	expression = ''.join(args.expression).rstrip()
	number = expression.split()[1]
	study = args.study


	if len(initpass) >= passlen:
		print "The length of init password must be less than password length."
		sys.exit()


	if passlen > 64:
		print "The password must be less than 64 characters."
		sys.exit()


	if len(symbfill) > 1:
		print "Only one symbol is allowed."
		sys.exit()


	if arch == "32":
		INSCOUNT = INSCOUNT32
	elif arch == "64":
		INSCOUNT = INSCOUNT64
	else:
		print "Unknown architecture"
		sys.exit()


	if study is True:
		lengthdetect(passlen)
		sys.exit()


	password = solve(initpass,passlen,symbfill,charset,expression)

	print "Password: ", password