no_of_lines =int(input('Enter the total number of lines planning to enter:'))
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"
    a=input("if u want to continue (y/n)")
    ""
    if(a=='y'):
        continue
    else:
        break
    print (lines)
for i in range (0,len(lines)):

   x=ord(lines[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y,end="")