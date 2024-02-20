#DNA PART
dna = '''
TTATTCTAAT AAGTAATAAT CAACGTAAAA ATTAACAATA TTAATAGAAA
TATAATTGAT TATTTTTATT AATATAGTAT TGTTAAATTG TATTATAGAA
CTGTATGATA AAGTTGTCTG CAT
'''
dna_new = dna.replace("\n", "").replace(" ","")
print(f"\nThe DNA sequence is: \n\n{dna_new}") 

#RNA PART
def my_function(x):
  return x[::-1] #reversed
rna = my_function(dna_new)
rna_map=rna.maketrans({'A':'U', 'T':'A', 'G':'C', 'C': 'G'})
rna_new=rna.translate(rna_map)
print(f"\nThe RNA sequence is: \n\n{rna_new}")

#AMINO ACID
#Dictionary
RNA_Codons = {
    # 'M' - START, '*' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

protein = ""
for i in range(0, len(rna), 3):
    codon = rna_new[i:i+3] #read every 3 letters repeatedly
    protein += RNA_Codons[codon]
print(f"\nThe protein sequence is: \n\n{protein}\n\n")

#Amino Acid Counter
amino_acid = {
  'A': 0,'R': 0,'N': 0,'D': 0,
  'C': 0,'E': 0,'Q': 0,'G': 0,
  'H': 0,'I': 0,'L': 0,'K': 0,          #Start from 0
  'M': 0,'F': 0,'P': 0,'S': 0,
  'T': 0,'W': 0,'Y': 0,'V': 0, '*':0
  }
for codon in protein:
    if codon in [
      'A' ,'R' ,'N' ,'D' ,
      'C' ,'E' ,'Q' ,'G' ,              #increase the number of letters
      'H' ,'I' ,'L' ,'K' ,              #if there are repetitions found
      'M' ,'F' ,'P' ,'S' ,
      'T' ,'W' ,'Y' ,'V' , '*'
      ]:
      amino_acid[codon]+=1   

amino_acidname = [
  'Alanine       :', 'Arginine      :', 'Asparagine    :', 'Aspartic Acid :',
  'Cysteine      :', 'Glutamic Acid :', 'Glutamine     :', 'Glycine       :',
  'Histidine     :', 'Isoleucine    :', 'Leucine       :', 'Lysine        :',
  'Methionine    :', 'Phenylalanine :', 'Proline       :', 'Serine        :',
  'Threonine     :', 'Tryptophan    :', 'Tyrosine      :', 'Valine        :',
  'Stop codon    :']

amino_acidcode = [
  'A' ,'R' ,'N' ,'D' ,
  'C' ,'E' ,'Q' ,'G' ,
  'H' ,'I' ,'L' ,'K' ,
  'M' ,'F' ,'P' ,'S' ,
  'T' ,'W' ,'Y' ,'V' , 
  '*']

print(f'Total codon   : {len(protein)}')

for i in range(0, len(amino_acidcode)):
  if amino_acid[amino_acidcode[i]] != 0:    #prints only found letters
    print(f"{amino_acidname[i]} {amino_acid[amino_acidcode[i]]}")
