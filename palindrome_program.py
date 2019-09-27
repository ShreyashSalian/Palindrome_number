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
for i in range(1,1000):
    temp = i
    new = 0
    while temp > 0:
        d = temp % 10
        new = new * 10 + d
        temp = temp //10

    if i == new:
       print(i)

