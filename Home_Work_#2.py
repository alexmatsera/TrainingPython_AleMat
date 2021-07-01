# Write a python program to find the sum of all even numbers from 0 to 10
count = 0
for num in range(11):
    if (num % 2 == 0):
        print(f'{num}')
        count += num
print(f'The elements sum: {count}')

# Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address

ip = input("Input IP address:")
import ipaddress
start_ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip))+1)
end_ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip))+6)
for ip_int in range(int(start_ip), int(end_ip)):
    print(ipaddress.IPv4Address(ip_int))

# Write a python program to print the factorial of a given number

n = int(input("Input number for factorial calculation: "))
factorial = 1
for i in range(2, n+1):
    factorial *= i
print(f'Calculated Factorial is equel to:{factorial}')

# Write a python program to print the first 10 numbers Fibonacci series
fib1 = fib2 = 1
n = int(input("Input number for Fibonacci series: "))
print(fib1, fib2, end=' ')
for i in range(2, 10):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
