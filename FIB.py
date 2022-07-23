#Rabbits and Recurrence Relations
#https://rosalind.info/problems/fib/

#ref: https://www.youtube.com/watch?v=Qk0zUZW-U_M

cache = {}

def wabbits(n, k):
    # If we have cached the value, then return it
    if n in cache:
        return cache[n]

    # Compute the Nth term    
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = wabbits(n-1, k) + wabbits(n-2, k) * k
    
    # Cache the value and return it
    cache[n] = value
    return value

with open('rosalind_fib.txt', 'r') as f:
    n, k = f.readline().strip().split(' ')

print(wabbits(int(n), int(k)))