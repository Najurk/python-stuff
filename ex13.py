# Use the code from last exercise here.
x = 0
a1 = list ()
num = input("How many elements do you want:")
for i in range(int(num)):
  f = input('Enter next number:')
  a1.append(int(f))
print (a1)

print("Enter a number:")
n = int(input("Which number do you want to find?"))
x = (a1.count(n))
print ("there are",x,n,"'s in the array.")
