n = 1020
rev = 0
while (n > 0):
    dig = n%10
    rev = rev*10 + dig
    n = n/10

n = 10
par = ""
for i in range(n):
    par += "()"

print par

a = [1,3,5,6,8,10]
b = [2,5,6,7,9,15]
k = 12

diff = 1000
an = 0
bn = 0
for i,ai in enumerate(a):
    for j,bi in enumerate(b):
        ab = ai + bi
        if diff > abs(k - ab):
            an = ai
            bn = bi
            diff = abs(k - ab)


print an
print bn

import math
prime = False
n = 101
limit = min(math.sqrt(n),n/2)
for i in [2] + range(3,int(math.ceil(limit+1)),2):
    if (n % i) == 0:
        prime = True
        print i
        break

print prime
