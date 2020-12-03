import random
global x
counter = 0
x = 0
with open('output.txt', 'w')as k:
				k.write('')
def toHex(dec):
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

def random2():
	input2 = int(input('how long will the string be? '))
	def random_chrs(langth):
		with open('example.txt', 'r') as y:
			z = y.read()
		# a = hex(0x0)
		# b = counter
		for i in langth:
			c = random.randint(0, 68177)
			print(z[c])
			with open('output.txt', 'a')as k:
				k.write(z[c])
	random_chrs(range(0, input2))


def small():
    y = int(
        input(
            'enter the number of reps that this should do \n (each repatation is about 3.65 MB) '
        ))
    encoding = str(input('what encodigh do you want to use? '))
    file = str(input('what file do you want to use for logging? '))
    KB = y * 3.65
    MB = str(KB)
    promt = 'are you shure that you want to print' + MB + 'MB of charaters (y or n) '
    r_u_shure = str(input(promt))
    x = 0

    def unicode():
        global x
        while (x != y):
            for i in range(0x0, 0xd800):
                print(chr(i))
                f = open(logging, "a", -1, encoding)
                f.write(chr(i))
                f.close()
            x = x + 1
            print(x, 'repations done')

    file = str(file)
    logging_file = file + '.txt'
    logging = str(logging_file)
    if (r_u_shure == 'y'):
        unicode()


def big():
    y = int(
        input(
            'enter the number of reps that this should do \n (each repatation is about 3.65 MB) '
        ))
    global encoding
    encoding = str(input('what encodigh do you want to use? '))
    file = str(input('what file do you want to use for logging? '))
    KB = y * 3.65
    MB = str(KB)
    promt = 'are you shure that you want to print' + MB + 'MB of charaters (y or n) '
    r_u_shure = str(input(promt))
    x = 0

    def unicode():
        global x
        while (x != y):
            for i in range(0x0, 0xd800):
                print(chr(i))
                f = open(logging, "a", -1, encoding)
                f.write(chr(i))
                f.close()
            for i in range(0xe000, 0xfffff):
                j = chr(i)
                print(j)
                f = open(logging, "a")
                f.write(j)
                f.close()
            x = x + 1
            print(x, 'repations done')

    logging_file = file, '.txt'
    logging = str(logging_file)
    if (r_u_shure == 'y'):
        unicode()


big_small = str(input('big  or small or random srring of any langth? '))
if (big_small == 'big'):
    big()
if (big_small == 'small'):
    small()

if (big_small == 'random string'):
	random2()
