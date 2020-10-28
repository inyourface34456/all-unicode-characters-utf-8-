counter = 0
for i in range(0x00000, 0xd800):
    print("\033[1;32;40m Bright Green  \n")
    print(chr(i))
    h = hex(i)
    print(h)
    counter = counter + 1
    print('this is the number of charaters that i printed so far:')
    print(counter)
hello = print ('mê')