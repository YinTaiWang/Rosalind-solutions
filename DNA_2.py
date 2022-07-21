# Counting DNA Nucleotides
# https://rosalind.info/problems/dna/

def counting(string):
    return string.count('A'), string.count('C'), string.count('G'), string.count('T')

if __name__ == '__main__':
    with open('rosalind_dna.txt', 'r') as f:
        string = f.readline()
    results = f"{string.count('A')} {string.count('C')} {string.count('G')} {string.count('T')}"
    print (results)