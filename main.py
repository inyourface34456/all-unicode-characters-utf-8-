import random
global x
counter = 0
x = 0
with open('output.txt', 'w') as k:
		k.write('')

with open('pass.txt', 'w') as l:
		l.write('')


def random_chrs(langth):
		with open('example.txt', 'r') as y:
				z = y.read()
		for i in langth:
				c = random.randint(0, 68100)
				print(z[c])
				with open('output.txt', 'a') as k:
						k.write(z[c])

def random2():
		x = str(
				input(
						'what do you want to do (type the num): \n 1. random password (letters caps and lower case and sesel chrs)\n 2. random pass (letters (caps and lower) and nums \n 3. random pass (letters (just caps) nums \n 4. random pass (just lower) and nums\n 5. make pass (just nums) \n 6. make pass just letters (caps)\n 7. make pass just letters (lower) \n 8. random string with all chrs included \n 9. generate a random hex value \n >>>'
				))

		def make_passabcABC123s():
				z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#','$', '%', '^', '&', '*', '(', ')'
				]
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
								k.write(z[c])

		def make_passabcABC123():
				z = [
						'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
						'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
						'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
						'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
						'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
				]
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
								k.write(z[c])

		def make_passABC123():
				z = [
						'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
						'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
						'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
				]
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
								k.write(z[c])

		def make_pass123():
				z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
							k.write(z[c])

		def make_passabc123():
				z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
							k.write(z[c])

		def make_passABC():
				z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
							k.write(z[c])

		def make_passabc():
				z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
				langth = int(input('how log will the string be'))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('pass.txt', 'a') as k:
							k.write(z[c])

		def make_hex():
				z = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
				langth = int(input('how log will the string be '))
				for i in range(0, langth):
						d = len(z)
						c = random.randint(0, d - 1)
						print(z[c])
						with open('output.txt', 'a') as k:
								k.write(z[c])

		def random_chrs():
				langth = int(input('How long'))
				with open('example.txt', 'r') as y:
						z = y.read()
				for i in range(0, langth):
						c = random.randint(0, 68176)
						print(z[c])
						with open('output.txt', 'a') as k:
								k.write(z[c])
		
	

		x = str(x)
		if (x == '1'):
				make_passabcABC123s()
		if (x == '2'):
				make_passabcABC123()
		if (x == '3'):
				make_passABC123()
		if (x == '4'):
				make_passabc123()
		if (x == '5'):
				make_pass123()
		if (x == '6'):
				make_passABC()
		if (x == '7'):
				make_passabc()
		if (x == '8'):
				random_chrs()
		if (x == '9'):
				make_hex()


def small():
		y = int(input('enter the number of reps that this should do \n (each repatation is about 107 KB) '))
		encoding = str(input('what encodigh do you want to use? '))
		file = str(input('what file do you want to use for logging? '))
		KB = y * 0.107
		MB = str(KB)
		promt = 'are you shure that you want to print ' + MB + ' MB of charaters (y or n) '
		r_u_shure = str(input(promt))
		x = 0

		def unicode():
			global x
			while (x != y):
				logging_file = str(file) + '.txt'
				while (x != y):
					with open('small_example.txt', 'r+', -1, encoding)as r:
						global sw
						sw = r.read()					
					with open(logging_file, 'a')as q:
						q.write(sw)
					x = x + 1
					print(x, 'repations done')

		if (r_u_shure == 'y'):
			unicode()
		


def big():
		y = int(input('enter the number of reps that this should do \n (each repatation is about 3.9 MB) '))
		global encoding
		encoding = str(input('what encodigh do you want to use? '))
		file = str(input('what file do you want to use for logging? '))
		KB = y * 3.9
		MB = str(KB)
		promt = 'are you shure that you want to print' + MB + 'MB of charaters (y or n) '
		r_u_shure = str(input(promt))
		x = 0
		def unicode():
			logging_file = str(file) + '.txt'
			global x
			while (x != y):
				with open('cleanbig8.txt', 'r+')as r:
					global s
					s = r.read()
				with open(logging_file, 'a')as q:
					q.write(s)
				x = x + 1
				print(x, 'repations done')
		if (r_u_shure == 'y'):
			unicode()


big_small = str(input('big  or small or random srring of any langth? '))
if (big_small == 'big'):
		big()
if (big_small == 'small'):
		small()

if (big_small == 'random string'):
		random2()
