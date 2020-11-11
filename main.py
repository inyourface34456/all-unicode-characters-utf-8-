def unicode():
  global x
  while(x != y):
    for i in range(0x0, 0xd800):
        print(chr(i))
        f = open(logging, "a")
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
y = int(input('enter the number of reps that this should do \n (each repatation is about 3.65 MB) '))
file = str(input('what file do you want to use for logging? '))
MB = y*3.65
promt = 'are you shure that you want to print', MB, 'MB of charaters (y or n) '
r_u_shure = str(input(promt))
x = 0 
logging_file = file, '.txt'
logging = str(logging_file)
if (r_u_shure == y):
  unicode()