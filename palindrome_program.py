"""n = int(input("Enter ThE number :"))
temp = n
new = 0
while temp > 0:
    d = temp % 10
    new = new * 10 + d
    temp = temp //10

if n == new:
    print("Number is palindrome")

else:
    print("Number is not palindrome")

#print(palindrome(101))
"""
var1=str(input("Enter the sequence"))
x=var1[::-1]
if(var1==x):
    print("It is a Palindrome Number")
else:
    print("It is not a Palindrome Number")
