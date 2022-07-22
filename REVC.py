#Complementing a Strand of DNA
#https://rosalind.info/problems/revc/

def complement(string):
    dna = []
    for i in string:
        if i == 'A':
            dna.append('T')
        elif i == 'T':
            dna.append('A')
        elif i == 'C':
            dna.append('G')
        elif i == 'G':
            dna.append('C')
    dna.reverse()    
    return dna

if __name__ == '__main__':
    with open('rosalind_revc.txt', 'r') as f:
        string = f.readline()
    DNA = ''.join(complement(string))
    print(DNA)