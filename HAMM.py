#Counting Point Mutations
#https://rosalind.info/problems/hamm/

def hammingdistance(s, t):
    hammingdistance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hammingdistance += 1
    return hammingdistance

if __name__ == '__main__':
    with open('rosalind_hamm.txt', 'r') as f:
        s, t = f.readlines()
    print(hammingdistance(s, t))

