'''
Rosalind Bioinformatics Stronghold 
'''
#############################Finding a Shared Spliced Motif#####################################
import sys
sys.setrecursionlimit(1500)

def LCSBackTrack(v, w):
	s = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
	backtrack = [['e' for j in range(len(w)+1)] for i in range(len(v)+1)]

	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			if v[i-1] == w[j-1]:
				s[i][j] = s[i-1][j-1] + 1
			else:
				s[i][j] = max(s[i-1][j], s[i][j-1])
			
			if s[i][j] == s[i-1][j]:
				backtrack[i][j] = '^'
			elif s[i][j] == s[i][j-1]:
				backtrack[i][j] = '>'
			elif s[i][j] == s[i-1][j-1]+1:
				backtrack[i][j] = '|'	
	'''
	for i in s:
		print (*i)
	'''
	return backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ''
    if backtrack[i][j] == "^":
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == ">":
        return OutputLCS(backtrack, v, i, j - 1)
    elif backtrack[i][j] == '|':
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i]

'''
output = open('LCSM1.txt', 'w+')
with open('rosalind_lcsq.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        if line.startswith('>'):
            output.write('\n' + line + '\n')
        else:
            output.write(line)

    output.close()

genelst11 = []
seqlst11 = []
with open('LCSM1.txt', 'r') as r:
    for line11 in r:
        line11 = line11.strip('\n')
        if line11.startswith('>'):
            line21 = line11.replace('>','')
            genelst11.append(line21)
        else:
            seqlst11.append(line11)

seqlst11.pop(0)
v = seqlst11[0]
w = seqlst11[1]
w, v= 'AACCTTGG', 'ACACTGTGA'
i = (len(v)-1)
j = (len(w)-1)
a = LCSBackTrack(v,w)
#print (OutputLCS(a, v, i, j))
#print (len(OutputLCS(a, v, i, j)))
'''
def lcs(xs, ys):
    ###Return a longest common subsequence of xs and ys.
    if xs and ys:
        *xb, xe = xs
        *yb, ye = ys
        if xe == ye:
            return lcs(xb, yb) + [xe]
        else:
            return max(lcs(xs, yb), lcs(xb, ys), key=len)
    else:
        return []

#a = (lcs(v,w))
#print (''.join(a))
w, v= 'AACCTTGG', 'ACACTGTGA'

v, w = 'PRETTY', 'PRTTEIN'
t =w
s = v
###http://saradoesbioinformatics.blogspot.com/2016/08/finding-shared-spliced-motif.html
lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
#creates array of len(s) containing arrays of len(t) filled with 0
for i, x in enumerate(s):
    for j, y in enumerate(t):
        if x == y:
            lengths[i + 1][j + 1] = lengths[i][j] + 1
        else:
            lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

for i in lengths:
	print (*i)

spliced_motif = ''
x, y = len(s), len(t)
while x * y != 0:
    if lengths[x][y] == lengths[x - 1][y]:
        x -= 1
    elif lengths[x][y] == lengths[x][y-1]:
        y -= 1
    else:
        spliced_motif = s[x - 1] + spliced_motif
        x -= 1
        y -= 1


print(spliced_motif)
print (len(spliced_motif))

#############################Edit Distance#####################################
	
memo = {}
sys.setrecursionlimit(15000)
def editDistance(str1, str2, m , n): 
	args = (m,n)
	if args in memo:
		return memo[args]
	
	# If first string is empty, the only option is to insert all characters of second string into first
	if m == 0: 
		ans = n

    # If second string is empty, the only option is to remove all characters of first string 
	elif n == 0: 
		ans = m 
  
    # If last characters of two strings are same, nothing much to do. Ignore last characters and get count for  remaining strings. 
	elif str1[m-1]==str2[n-1]: 
		ans = editDistance(str1,str2,m-1,n-1) 
  
    # If last characters are not same, consider all three  operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values. 
	else:
		ans = 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                   editDistance(str1, str2, m-1, n-1)    # Replace 
                   ) 

	memo[args] = ans
	return ans

'''
output = open('editDistance1.txt', 'w+')
with open('rosalind_edit.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        if line.startswith('>'):
            output.write('\n' + line + '\n')
        else:
            output.write(line)

    output.close()

genelst11 = []
seqlst11 = []
with open('editDistance1.txt', 'r') as r:
    for line11 in r:
        line11 = line11.strip('\n')
        if line11.startswith('>'):
            line21 = line11.replace('>','')
            genelst11.append(line21)
        else:
            seqlst11.append(line11)

seqlst11.pop(0)
str1 = seqlst11[0]
str2 = seqlst11[1]
print (editDistance(str1, str2, len(str1), len(str2)))
'''

#############################Perfect Matchings and RNA Secondary Structures#####################################
import functools
def RNAfolding(seq):
	count_A = 0
	count_G = 0 
	for a in range(len(seq)):
		if seq[a] == 'A':
			count_A +=1
		elif seq[a] == 'G':
			count_G += 1

	A = functools.reduce(lambda x, y: x*y, list(x for x in range(1,count_A + 1)))
	G = functools.reduce(lambda x, y: x*y, list(x for x in range(1,count_G + 1)))

	return (A * G)
Seq = 'CGUACGGGUUUAACCCCUCGUAUCGCGGUACAUGACCUAGUACAAACCAGAGUAGGGCCGGUCGCAUAUUGUGCUA'
#print (RNAfolding(Seq))

#############################Longest Increasing Subsequence#####################################

def longest_subsequence(arr, f):
    cache = [1] * len(arr)
    for j in range(1,len(arr)):
        for i in range(j):
            if f(arr[j], arr[i]):
                cache[j] = max(cache[j], cache[i] + 1)

    top = max(cache)
    index = cache.index(max(cache))
    lst = [arr[index]]
    top -= 1
    while top != 0:
        index = arr.index(lst[-1])
        templst = []
        for i in range(index):
            if cache[i] == top:
                templst.append(arr[i])
        top -= 1 
        a = max(templst)
        lst.append(a)
    #print (cache.index(max(cache)))
    #print (*arr)
    #print (*cache)
    return (lst[::-1])

def longest_increasing_subsequence(arr, f):
    cache = [1] * len(arr)
    for j in range(1,len(arr)):
        for i in range(j):
            if f(arr[j], arr[i]):
                cache[j] = max(cache[j], cache[i] + 1)

    top = max(cache)
    index = cache.index(max(cache))
    lst = [arr[index]]
    top -= 1
    while top != 0:
        index = arr.index(lst[-1])
        templst = []
        for i in range(index):
            if cache[i] == top:
                templst.append(arr[i])
        top -= 1 
        a = min(templst)
        lst.append(a)
    #print (cache.index(max(cache)))
    #print (*arr)
    #print (*cache)
    return (lst[::-1])

output = open('rosalind_lgis.txt', 'r+')
arr = []
for line in output:
    line = line.strip('\n').split(' ')
    arr.append((line))

arr1 = []
for i in arr[1]:
    arr1.append(int(i))

#print (arr1)

arr = [2, 50, 4, 30, 6, 8, 10, 12, 22, 14, 16, 18, 17, 20]
arr11 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
a = longest_increasing_subsequence(arr1, lambda x, y : x > y) # increasing
b = longest_subsequence(arr1, lambda x, y : x < y) # decreasing

#print (*a)
#print (*b)

#############################Interleaving Two Motifs#####################################
def scs(a,b):
    matrix = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
    
    for i in range(len(b)+1):
        for j in range(len(a)+1):
            if i == 0 or j == 0:
                matrix[0][j] = j
                matrix[i][0] = i
            elif b[i-1] == a[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1])
                
    index = matrix[len(b)][len(a)]
    string = ''
    i, j = len(b), len(a)
    while i>0 and j>0:
        if b[i-1] == a[j-1]:
            string += b[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            string += a[j-1]
            j -= 1
            index -= 1
        else:
            string += b[i-1]
            i -= 1
            index -= 1

    while (i>0):
        string += b[i-1]
        i -= 1
        index -= 1
    while (j>0):
        string += a[j-1]
        j -= 1
        index -= 1

    print (index)
    return string[::-1]
    

a1 , b1= 'GXTXAYB', 'AGGTAB'
a, b= 'ATCTGAT','TGCATA'
s, t = [line.strip() for line in open('rosalind_scsp.txt','r')]
#print (scs(s,t))

#############################Mortal Fibonacci Rabbits#####################################
import sys
sys.setrecursionlimit(15000)
memo = {}
def mortal_fib(n,m):
    args = (m,n)
    if args in memo:
        return memo[args]

    elif n <= 2:
        ans = 1

    elif n <= m:
        ans = mortal_fib(n-2,m) + mortal_fib(n-1,m) 

    else:
        ans = mortal_fib(n-2,m) + mortal_fib(n-1,m) - mortal_fib(n-(m+1),m)

    memo[args] = ans
    return ans

#print (mortal_fib(100,20))

#############################Error Correction in Reads#####################################

lst = ['TCATC','TTCAT','TCATC','TGAAA','GAGGA','TTTCA','ATCAA','TTGAT','TTTCC']

lst = []
with open('rosalind_corr.txt', 'r+') as f:
    for line in f:
        line = line.strip('\n')
        if not line.startswith('>'):
            lst.append(line)

def Complement(DNA):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in DNA:
        complement += basepairs.get(base)
    return complement[::-1]

def hamming_distance(DNA1, DNA2):
    return sum(c1 != c2 for c1, c2 in zip(DNA1, DNA2))

DNAlst = []
for i in lst:
    a = (Complement(i))
    DNAlst.append(a)

newlst = []
for i in lst:
    for j in DNAlst:
        if i == j:
            newlst.append(i)

for i in newlst:
    lst.remove(i)

newlst1 = []
list(newlst1.append(x) for x in lst if lst.count(x) == 1)
newlst2 = []
list(newlst2.append(x) for x in lst if lst.count(x) > 1)

finallst = []

for i in range(len(newlst1)):
    for j in range(len(DNAlst)):
        if hamming_distance(newlst1[i], DNAlst[j]) == 1 and (newlst1[i] + '->' + DNAlst[j]) not in finallst:
            finallst.append(newlst1[i] + '->' + DNAlst[j]) 

for i in range(len(newlst1)):
    for k in range(len(newlst2)):
        if hamming_distance(newlst1[i], newlst2[k]) == 1 and (newlst1[i] + '->' + newlst2[k]) not in finallst:
            finallst.append((newlst1[i] + '->' + newlst2[k]))
'''
for i in finallst:
    print (i)
'''
#############################Maximum Matchings and RNA Secondary Structures#####################################
import functools
def RNAfolding1(seq):
    count_A = 0
    count_U = 0
    count_G = 0
    count_C = 0 
    for a in range(len(seq)):
        if seq[a] == 'A':
            count_A +=1
        elif seq[a] == 'G':
            count_G += 1
        elif seq[a] == 'C':
            count_C += 1
        elif seq[a] == 'U':
            count_U += 1

    minAU = min(count_A, count_U)
    minGC = min(count_G, count_C)
    maxAU = max(count_A, count_U)
    maxGC = max(count_G, count_C)
    diffAU = maxAU - minAU
    diffGC = maxGC - minGC

    AU = functools.reduce(lambda x, y: x*y, list(x for x in range(1,maxAU + 1)))
    GC = functools.reduce(lambda x, y: x*y, list(x for x in range(1,maxGC + 1)))
    AU1 = functools.reduce(lambda x, y: x*y, list(x for x in range(1,diffAU + 1)))
    GC1 = functools.reduce(lambda x, y: x*y, list(x for x in range(1,diffGC + 1)))
    return int((AU//AU1) * (GC//GC1))
Seq = 'CAUAGACCGUGCUGUAAUUCGAUUAUGGUCGACAUGACCGGUAGUAGCAGUUUCUCCGUCAUCAGUAUAGUGGUUCUAGUAC'
print (RNAfolding1(Seq))