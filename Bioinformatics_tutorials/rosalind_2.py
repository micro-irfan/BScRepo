	'''
Rosalind Bioinformatics Stronghold 
'''
#############################Locating Restrition Sites#####################################

def Complement(DNA):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in DNA:
        complement += basepairs.get(base)
    return complement

def LocatingRestrictionSite(DNA):
	complementaryDNA = Complement(DNA)
	lst = []
	for i in range (len(DNA)):
		for j in range(4,13):
			reverseDNA = complementaryDNA[i:i+j]
			if DNA[i:i+j] == reverseDNA[::-1]:
				if len(DNA[i:i+j]) > 2 and [i+1, len(DNA[i:i+j])] not in lst:
					lst.append([i+1, len(DNA[i:i+j])])
	return lst

DNA = []
with open('rosalind_revp.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if not line.startswith('>'):
			DNA.append(line)

DNA = ''.join(DNA)
a = (LocatingRestrictionSite(DNA))
'''
for i in a:
	i = str(i)
	print (''.join(i).replace('[','').replace(']','').replace(',', '').replace(' ','\t'))
'''
#############################Ordering Strings of Varying Length Lexicographically#####################################
#Source:http://saradoesbioinformatics.blogspot.com/2016/08/ordering-strings-of-varying-length.html
import itertools

n = 3
alphabet = 'TXVEAFIWHM'
perm = []
for i in range(1, n + 1):
	perm.append(list(map(''.join, (itertools.product(alphabet, repeat=i)))))
permutations = list(itertools.chain(*perm))
srt_perm = sorted(permutations, key=lambda word: [alphabet.index(c) for c in word])
'''
for i in srt_perm:
	print (i)

'''
#############################Finding a Spliced Motif#####################################
#source : http://saradoesbioinformatics.blogspot.com/2016/07/finding-spliced-motif.html

output = open('SplicedMotif.txt', 'w+')
with open('rosalind_sseq.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        if line.startswith('>'):
            output.write('\n' + line + '\n')
        else:
            output.write(line)

    output.close()

genelst11 = []
seqlst11 = []
with open('SplicedMotif.txt', 'r') as r:
    for line11 in r:
        line11 = line11.strip('\n')
        if line11.startswith('>'):
            line21 = line11.replace('>','')
            genelst11.append(line21)
        else:
            seqlst11.append(line11)

seqlst11.pop(0)
s = seqlst11[0]
t = seqlst11[1]

pos = 0                                    
positions = []                             
for i in range(len(t)):                    
    for j in range(pos, len(s)):           
        pos += 1                           
        if len(positions) < len(t):        
            if t[i] == s[j]:               
                positions.append(pos)      
                break                      
#print(*positions, sep=' ')

#############################Rabbits and Recurrence Relations #####################################
##Source: https://medium.com/p/4812c0c2ddb3/responses/show

def rabbitPairs(n,k):
	if n == 1:
		return 1

	elif n == 2:
		return k

	if n <= 4:
		return (rabbitPairs(n-1,k) + rabbitPairs(n-2,k))

	else:
		return (rabbitPairs(n-1,k) + (rabbitPairs(n-2,k) * k))

#print(rabbitPairs(32,5))
 
#############################Inferring mRNA from Protein#####################################

gencode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":" ", "UAG":" ",
    "UGU":"C", "UGC":"C", "UGA":" ", "UGG":"W",
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

from functools import reduce
def mRNAfromProtein(seq):
	seq += ' '
	seq = list(seq)
	totalNumber = []
	for i in seq:
		count = 0
		for key, value in gencode.items():
			if i == value:
				count += 1

		totalNumber.append(count)

	return reduce((lambda x, y: x*y % 1000000), totalNumber)


#############################Partial Permutations#####################################
## search for K permutations
def partialPermutation(n,k):
	count = 1
	for i in range(n):
		count *= i+1

	Dcount = 1
	D = n-k
	for i in range(D):
		Dcount *= (i+1)

	return (int(count/Dcount) % 1000000)

#print (partialPermutation(80,9))

def permute(n):
	if n == 0:
		return 1 
	elif n == 1:
		return 2
	else:	
		return (2*n*(permute(n-1)) - ((n-1)**2)*permute(n-2))

#############################Calculating Protein Mass#####################################
massTableDictionary = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
                "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
                "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
                "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}

def getProteinMass(seq):
	mass = 0
	for i in seq:
		for key, values in massTableDictionary.items():
			if key == i:
				mass += values
	return mass

#############################Open Reading Frames#####################################

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

def readingFrames(seq):
	DNA = seq.replace('T','U')
	DNAseq = []
	for i in range(len(DNA)):
		if DNA[i:i+3] =='AUG':
			DNAseq.append(DNA[i:len(DNA)])

	newlst = []
	for a in DNAseq:
		for i in range(len(a)):
			if a[i:i+3] == 'UAA' or a[i:i+3] == 'UGA' or a[i:i+3] == 'UAG':
				if len(a[0:i+3]) % 3 == 0:
					newlst.append(a[0:i+3])

	prolst = []
	for a in newlst:
		count = 0
		lst = []
		for i in range(len(a)):
			if  a[i:i+3] == 'UAA' or a[i:i+3] == 'UGA' or a[i:i+3] == 'UAG':
				if (i%3 == 0):
					count += 1
					lst.append(i)

		if count == 1:
			prolst.append(a)

	proteinLst = []
	for a in prolst:
		proteinLst.append(Translate(a))
	return proteinLst

def Complement(DNA):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in DNA:
        complement += basepairs.get(base)
    return complement[::-1]

DNA =[]
with open('rosalind_orf.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if not line.startswith('>'):
			DNA.append(line)

seq = ''.join(DNA)
#seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
reverseDNA = Complement(seq)
lst = []
for i in readingFrames(reverseDNA):
	lst.append(i)

for i in readingFrames(seq):
	if i not in lst:
		lst.append(i)
'''
for i in lst:
	print (i)
'''

#############################Consensus and Profile#####################################

#list of seq
def Consensus(seq):
	profileMatrix = [[0 for i in range(len(seq[0]))] for j in range(4)]

	for i in range(len(seq)):
		for j in range(len(seq[i])):
			if seq[i][j] == 'A':
				profileMatrix[0][j] += 1
			elif seq[i][j] == 'C':
				profileMatrix[1][j] += 1
			elif seq[i][j] == 'G':
				profileMatrix[2][j] += 1
			elif seq[i][j] == 'T':
				profileMatrix[3][j] += 1

	consensusDNA = ''
	for j in range (len(profileMatrix[0])):
		a = profileMatrix[0][j]
		b= 0
		for i in range(len(profileMatrix)):
			if profileMatrix[i][j] > a:
				a = profileMatrix[i][j]
				b = str(i)

		if a == profileMatrix[0][j]:
			b = 0
		
		consensusDNA += str(b)
	
	#print (consensusDNA)
	basepairs = {"0":"A", "1":"C", "2":"G", "3":"T"}
	DNA = ''
	for base in consensusDNA:
		DNA += basepairs.get(base)

	return (DNA, profileMatrix)

DNAlst = ['A:', 'C:', 'G:', 'T:']

output = open('Consensus.txt', 'w+')
with open('rosalind_cons.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()


seqlst = []
with open('Consensus.txt', 'r') as r:
	for line1 in r:
		line1 = line1.strip('\n')
		if not line1.startswith('>'):
			seqlst.append(line1)

seqlst.pop(0)
a = (Consensus(seqlst)[1])
for i in range(len(a)):
	a[i].insert(0, DNAlst[i])
'''
print (Consensus(seqlst)[0])
for i in a:
	print (*i)
'''


#############################Calculating Expected Offspring#####################################

def calculatingOffsprings(lst):
	Offspring = 0
	for i in range(len(lst)):
		if i <= 2:
			Offspring += 2*lst[i]
		if i == 3:
			Offspring += 0.75*2*lst[i]
		if i == 4:
			Offspring += 0.5*2*lst[i]

	return Offspring


#print (calculatingOffsprings([16796, 19063, 18681, 16721, 18813, 17753]))

#############################Genome Assembly as Shortest Superstring#####################################
#Source : https://github.com/mtarbit/Rosalind-Problems/blob/master/e025-long.py

output = open('shortestSuperstring.txt', 'w+')
with open('rosalind_long.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		if line.startswith('>'):
			output.write('\n' + line + '\n')
		else:
			output.write(line)

	output.close()

seqlst1 = []
with open('shortestSuperstring.txt', 'r') as r:
	for line1 in r:
		line1 = line1.strip('\n')
		if not line1.startswith('>'):
			seqlst1.append(line1)
seqlst1.pop(0)

def shortestSuperstring1(seq, ss = ''):
	if len(seq) == 0:
		return ss

	elif len(ss) == 0:
		ss = seq.pop(0)
		return shortestSuperstring1(seq, ss)

	else:
		for i in range(len(seq)):
			a = seq[i]
			l = len(seq[i])
			for j in range(int(l/2)):
				k = l - j

				if ss.startswith(a[j:]):
					seq.pop(i)
					return shortestSuperstring1(seq, a[:j] + ss)

				elif ss.endswith(a[:k]):
					seq.pop(i)
					return shortestSuperstring1(seq, ss + a[k:])


