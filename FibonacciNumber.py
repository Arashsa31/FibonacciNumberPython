#Fibonacci sequence: The first 10 Fibonacci numbers are as follows:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

"""The Fibonacci Sequence is the series of numbers. The next number is found by adding 
up the two numbers before it. Write a program that will output the Fibonacci number up to n."""

n1 = 0
n2 = 1
n3 = 0
n = 50
print("0, 1,", end = ' ')

while n3 < n:
    n3 = n1+n2
    if n3 <= n:
        print(n3, end = ', ')
    n1 = n2
    n2 = n3
    
print("...")