'''
Problems solved 
'''
def CountNucleotides(text):
	count_A = 0
	count_C = 0
	count_G = 0
	count_T = 0
	for i in range(len(text)):
		if text[i] == 'A':
			count_A += 1
		elif text[i] == 'C':
			count_C += 1
		elif text[i] == 'G':
			count_G += 1
		elif text[i] == 'T':
			count_T += 1

	return str(count_A) + ' ' + str(count_C) + ' ' + str(count_G) + ' ' + str(count_T)

def RNAstring(DNA):
	return DNA.replace('T','U')

def Complement(DNA):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in DNA:
        complement += basepairs.get(base)
    return complement[::-1]

def GCcontentCount(DNA):
	count_GC = 0 
	for i in range(len(DNA)):
		if DNA[i] == 'G' or DNA[i] == 'C':
			count_GC += 1 
	return (count_GC/len(DNA)) * 100  
'''
output = open('GC_content.txt', 'w+')
with open('rosalind_GC.txt', 'r+') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()

data = open('GC_content.txt', 'r+')
for line1 in data:
	line1 = line1.strip('\n')
	try:
		if line1.startswith('>'):
			print (line1)	
		else:
			print (GCcontentCount(line1))
	except:
		pass
'''

## did not manage to get the highest value

def hamming_distance(DNA1, DNA2):
    return sum(c1 != c2 for c1, c2 in zip(DNA1, DNA2))

def Translate(seq):
    gencode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
    "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    
    protein ="" 
    if len(seq)%3 == 0: 
        for i in range(0, len(seq), 3): 
            codon = seq[i:i + 3] 
            protein+= gencode[codon] 
    return protein 

def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        pos = i 
        if Genome[i:i + len(Pattern)] == Pattern:
            positions.append(pos + 1)
    return positions  

'''
##Create a dictionary from the file 
output = open('graph1.txt', 'w+')
with open('rosalind_grph.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()
'''
genelst = []
seqlst = []
with open('graph1.txt', 'r') as r:
	for line1 in r:
		line1 = line1.strip('\n')
		if line1.startswith('>'):
			line2 = line1.replace('>','')
			genelst.append(line2)
		else:
			seqlst.append(line1)

seqlst.pop(0)
dictionary = dict(zip(genelst, seqlst))
dictionary2 = dictionary

lst = [] 
for key, values in dictionary.items():
	for key2, values2 in dictionary2.items():
		if values[0:3] == values2[-3:] and key != key2:
			lst.append(key2 + ' ' + key)
'''
for i in lst:
	print (i)
'''	    
##def mandelianInheritance (k, m, n):


#Finding a shared Motif
'''
output = open('lcsm.txt', 'w+')
with open('rosalind_lcsm.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()
'''
genelst1 = []
seqlst1 = []
with open('lcsm.txt', 'r') as r:
	for line11 in r:
		line11 = line11.strip('\n')
		if line11.startswith('>'):
			line21 = line11.replace('>','')
			genelst1.append(line21)
		else:
			seqlst1.append(line11)

seqlst1.pop(0)
dictionary1 = dict(zip(genelst1, seqlst1))
dictionary21 = dictionary1
a = (len(dictionary1))
DNAstring = ''

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
            	if j > len(substr) and is_substr(data[0][i:i+j], data):
                	substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


def RNAsplicing(DNA, listOfIntrons):
	finalDNA = DNA
	for i in range(len(DNA)):
		for a in listOfIntrons:
			if finalDNA[i:i + len(a)] == a:
				finalDNA = finalDNA[0:i] + finalDNA[i + len(a):len(finalDNA)]

	protein = Translate(finalDNA.replace('T','U'))
	return protein

output = open('RNAsplicing.txt', 'w+')
with open('rosalind_splc.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()

genelst11 = []
seqlst11 = []
with open('RNAsplicing.txt', 'r') as r:
	for line11 in r:
		line11 = line11.strip('\n')
		if line11.startswith('>'):
			line21 = line11.replace('>','')
			genelst11.append(line21)
		else:
			seqlst11.append(line11)

seqlst11.pop(0)
DNAsequence = seqlst11[0]
seqlst11.pop(0)

a = (RNAsplicing(DNAsequence, seqlst11))

def TransitionsTransversion(DNA1,DNA2):
	transition = 0
	transversion = 0
	for i in range(len(DNA1)):
		if DNA1[i] != DNA2[i]:
			if DNA1[i] == 'A' and DNA2[i] == 'G' or DNA1[i] == 'G' and DNA2[i] == 'A':
				transition += 1 
			elif DNA1[i] == 'C' and DNA2[i] == 'T' or DNA1[i] == 'T' and DNA2[i] == 'C':
				transition += 1
			else:
				transversion += 1

	return (transition/transversion) 

output = open('TTratio.txt', 'w+')
with open('rosalind_tran.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()

genelst111 = []
seqlst111 = []
with open('TTratio.txt', 'r') as r:
	for line11 in r:
		line11 = line11.strip('\n')
		if line11.startswith('>'):
			line21 = line11.replace('>','')
			genelst111.append(line21)
		else:
			seqlst111.append(line11)

seqlst111.pop(0)
'''
def makingSubsequence(t):
	t1 = t + t
	lst = []
	for i in range(len(t1)):
		for j in range(i, len(t1)+1):
			subsequences = t1[i:j]
			if len(subsequences) > 1 and subsequences not in lst and len(subsequences) < len(t):
				lst.append(subsequences)
	lst.append(t)
	return lst

def subsequence(s,t):
	lstOfSubsequences = makingSubsequence(t)
	print (lstOfSubsequences)
	pos = []
	for i in range(len(s)):
		for a in lstOfSubsequences:
			if s[i:i+len(a)] == a:
				pos.append(i)

	return pos
'''
def hamming_distance(DNA1, DNA2):
    return sum(c1 != c2 for c1, c2 in zip(DNA1, DNA2))

def splicedMotif(s, t):
	pos = []
	for i in range(len(s)):
		if hamming_distance(s[i:i+len(t)] , t) <= 1	or hamming_distance(s[i:i+len(t)] , t[::-1]) <= 1:
			pos.append(i+1)

	return pos


ab = (splicedMotif('ACGTACGTGACG', 'GTA'))

import itertools
def enumeratingGeneOrder(n):
	lst = []
	for i in range(n):
		lst.append(i+1)
	
	return list(itertools.permutations(lst))

abb =  (enumeratingGeneOrder(7))
'''
print (len(abb))
for i in abb:
	print (*i)
'''

def signedpermutation(n):
	lst = []
	for i in range(n):
		lst.append(i+1)

	lst2 = []
	for p in itertools.permutations(lst):
		for signs in itertools.product([-1,1], repeat=len(lst)):
			a = [a*sign for a, sign in zip(p,signs)] 
			lst2.append(a)

	return (lst2)

abbb = (signedpermutation(5))
'''
print (len(abbb))
for i in abbb:
	print (*i)
'''
import random
def enumeratingKmers(letters, k):
	lst = []
	while len(lst) != len(letters)**k:
		a = ''
		while len(a) != k:
			a += random.choice(letters)
		if a not in lst:
			lst.append(a)

	return lst

letters = ['A', 'B', 'C', 'D', 'E' ,'F']
a = (sorted(enumeratingKmers(letters, 3)))
'''
for i in a:
	print (i)
'''

def mandelianInheritance(k, m, n):
	total = k + m + n
	mm = 1/4 * m/total * (m-1)/(total-1)
	mn = 1/2 * m/total * (n)/(total-1)
	nm = 1/2 * n/total * (m)/(total-1)
	nn = n/total * (n-1)/(total-1)
	return (1 - (mm + mn + nm + nn))

###
import random
def enumeratingKmers(letters, k):
	lst = []
	while len(lst) != len(letters)**k:
		a = ''
		while len(a) != k:
			a += random.choice(letters)
		if a not in lst:
			lst.append(a)

	return lst

letters = ['A', 'C', 'T', 'G']

def KmerComposition(DNAstring, letters, k):
	lstOfKmers = (sorted(enumeratingKmers(letters, k)))
	lst = []
	dicto = {}
	for i in range(len(DNA)):
		for a in lstOfKmers:
			if DNA[i:i + k] == a: 
				lst.append(a)

	for a in lstOfKmers:
		dicto[a] = lst.count(a)
	'''
	for key in sorted(dicto.keys()) :
		print(key , " :: " , dicto[key])
	'''
	finalAnswer = []
	for key, value in sorted(dicto.items()):
		finalAnswer.append(str(value))
	
	return (' '.join(finalAnswer))

DNA = []
with open('rosalind_kmer.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if not line.startswith('>'):
			DNA.append(line)

DNA = ''.join(DNA)
#DNA = 'CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'
#print (KmerComposition(DNA, letters, 4))


