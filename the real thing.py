counter = 0
for i in range(0x00000, 0xd7ff):
    print("\033[1;32;40m \n")
    print(chr(i)) 
    h = hex(i)
    print(h)
    counter = counter + 1
    print('this is the number of charaters that i printed so far:')
    print(counter)

for i in range(0xe8000, 0xfffff):
  print("\033[1;35;40m \n")
  print(h)
  counter = counter + 1
  print('this is the number of charaters that i printed so far:')
  print(counter)

print(chr(0xfffff))
print(h)
print('this is the number of charaters that i printed so far:')
counter = counter + 1
print(counter)
