counter = 0 # set the counter to zero
for i in range(0x00000, 0xd800): # covers the first half of the chars
  print("\033[1;32;40m \n") # adds color
  print(chr(i)) # prints the unicode char
  h = hex(i) # grabs the hex value (for convince)
  print(h) # prints the hex value
  counter = counter + 1 # how many chars that the program printed
  print('this is the number of charaters that i printed so far:') # some text
  print(counter) # prints the counter


for j in range(0xe8000, 0xfffff): # covers the chars after high suoragates
  print("\033[1;35;40m \n") # changes the colors (so i know that it works)
  print(chr(j))
  # print(j) for debugging
  h = hex(j)
  print(h) # prints the unicode char
  counter = counter + 1 # how many chars that the program printed
  print('this is the number of charaters that i printed so far:') # some text
  print(counter) # prints the counter

print(chr(0xfffff)) # prints the final char
print(h) # prints the hex value
print('this is the number of charaters that i printed so far:') # some text
counter = counter + 1 # how many chars that the program printed
print(counter) # prints the counter