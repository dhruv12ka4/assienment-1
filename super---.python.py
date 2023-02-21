solutoin 1

# Fibonacci sequence seris

num1 = 0
num2 = 1
a = input("print fibonacci series:")
while num1 < 50:
    print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    
solution 3

list = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1

print("Even number in list",even)
print("Odd number in list",odd)

solution 2

a = input("Enter a string:")
for word in a.split():
    print(word[::-1],end=" ")







   
