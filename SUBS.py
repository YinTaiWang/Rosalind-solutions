#Finding a Motif in DNA
#https://rosalind.info/problems/subs/

def matching(genome, pattern):
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(i+1)
    return positions

with open('rosalind_subs.txt', 'r') as f:
    genome, pattern= f.read().split('\n')
new_positions = matching(genome, pattern)
result = ' '.join(map(str, new_positions))
print(result)