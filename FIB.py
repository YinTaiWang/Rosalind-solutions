#Rabbits and Recurrence Relations
#https://rosalind.info/problems/fib/


def wabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return wabbits(n-1, k) + wabbits(n-2, k) * k

with open('rosalind_fib.txt') as f:
    n, k = f.readline().strip().split(' ')
    
print(wabbits(int(n), int(k)))