# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
for i in range(0,1000):
    if i %5==0 or i%3 == 0:
        sum += i

print("Problem1: The sum of all the multiples of 3 or 5 below 1000 is " + str(sum))


# Problem 2 Euler
# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

first = 0
second = 1
fib =0
while (sum <4000000):
    sum = first + second
    first = second
    second = sum
    if sum%2 ==0:
        fib = fib + sum
        
print("Problem2: The sum of even-valued terms is " + str(fib))
    

# Problem 3 Euler
# The prime factors of 13195 are 5,7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def primefactor(number):
    b = 2
    while b<=number:
        if number%b==0:
            number=number//b
            print("prime factor:", b)
            b = 2
        else:
            b+= 1

primefactor(600851475143)            

class hello:
    kind = 'cat'
    color = 'green'
    
