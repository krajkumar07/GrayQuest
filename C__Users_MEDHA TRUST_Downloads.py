#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_anagrams(n1, n2):
    return sorted(bin(n1)[2:]) == sorted(bin(n2)[2:])

print(binary_anagrams(9, 6))   
print(binary_anagrams(13, 14)) 


# In[3]:


def pair_sum(arr, t):
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            break
    l, h = (i + 1) % n, i

    while l != h:
        c_sum = arr[l] + arr[h]
        if c_sum == t:
            return True
        elif c_sum < t:
            l = (l + 1) % n
        else:
            h = (h - 1 + n) % n
    return False

n_arr = [11, 15, 6, 8, 9, 10]
t = 16
print(pair_sum(n_arr, t))


# In[4]:


def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File not found."

file_path = "example.txt"
print(count_lines_in_file(file_path))


# In[5]:


class Rectangle:
    def __init__(self, length, breadth):
        if length <= 0 or breadth <= 0:
            raise ValueError("Length and breadth must be positive integers.")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def is_square(self):
        return self.length == self.breadth

try:
    rect = Rectangle(5, 4)
    print(f"Area = {rect.area()}")
    print(f"Perimeter = {rect.perimeter()}")
    print(f"Is Square = {rect.is_square()}")
except ValueError as e:
    print(e)


# In[28]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_numbers(n):
    primes = [x for x in range(2, n + 1) if is_prime(x)]
    result = set()

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            total = primes[i] + primes[j]
            if total <= n and not is_prime(total):
                result.add(total)
    return sorted(result)
print(find_numbers(20))  


# In[ ]:




