#Counting Point Mutations
#https://rosalind.info/problems/hamm/

def HammingDistance(s, t):
    hammingdistance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hammingdistance += 1
    return hammingdistance

HammingDistance(s, t)

