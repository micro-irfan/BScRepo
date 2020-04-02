## Exercise 1 

def calculateNumberOfPaths(n, m):
    if n>m :
        a =n
    else: 
        a =m

    matrix = [[1 for x in range(a)] for y in range(a)]
    for i in range(1, a):
        for j in range(1, a):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] 
    return matrix[n-1][m-1]

## output=30421755
##print (calculateNumberOfPaths(13, 17))

#exercise 

def ManhattanTourist(n, m, down_matix, right_matrix): 
    s_dic = {(0,0):0}
    for i in range(1,n+1):
        s_dic[(i,0)] = s_dic[(i-1,0)] + down_matix[i-1][0]

    for j in range(1,m+1):
        s_dic[(0,j)] = s_dic[(0,j-1)] + right_matrix[0][j-1]

    # calulation
    for i in range(1,n+1):  
        for j in range(1,m+1):
            s_dic[(i,j)] = max(s_dic[(i-1,j)]+down_matix[i-1][j], s_dic[(i,j-1)] + right_matrix[i][j-1])

    #return
    return s_dic[(n,m)]

#Exercise 2


from functools import lru_cache

@lru_cache(maxsize=128, typed=False)
def RecursiveChange(money, coins):
    if money == 0:
        return 0

    MinNumCoins = float('inf')
    for i in range(len(coins)):
        if coins[i] <= money:
            NumCoins = RecursiveChange(money-coins[i], coins)
            if NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1

    return MinNumCoins

coins = (5, 4, 1)
lst = []
for m in range(13,23):
    a = RecursiveChange(m, coins)
    a = str(a)
    lst.append(a)
 
def memoize(f):
    memo = {}
    def helper(x,y):
        if x and y not in memo:            
            memo[x][y] = f(x)
        return memo[x][y]
    return helper

##@memoize

def DPChange(money, Coins):
    MinNumCoins = {0:0}
    for m in range(1, money+1):
        combs = []
        for c in Coins:
            if m >= c:
                val = MinNumCoins.get(m-c,0)
                combs.append(val+1)

        MinNumCoins[m] = min(combs)
    return MinNumCoins[money]

money = 40 
Coins = [50,25,20,10,5,1]

money1 =8074
Coins1 = (24,13,12,7,5,3,1)
#print (DPChange(money, Coins))
##print (DPChange(money,Coins))

## adding of diagonal

def ManhattanTourist1(n, m, down_matix, right_matrix, cross_matrix = None): 
    s_dic = {(0,0):0}

    for i in range(1,n+1):
        s_dic[(i,0)] = s_dic[(i-1,0)] + down_matix[i-1][0]

    for j in range(1,m+1):
        s_dic[(0,j)] = s_dic[(0,j-1)] + right_matrix[0][j-1]

    # calulation
    for i in range(1,n+1):
        for j in range(1,m+1):
            s_dic[(i,j)] = max(s_dic[(i-1,j)]+down_matix[i-1][j], s_dic[(i,j-1)] + right_matrix[i][j-1])

            if cross_matrix is not None:
                s_dic[(i,j)] = max(s_dic[(i-1,j-1)] + cross_matrix[i-1][j-1], s_dic[(i,j)])
                
    return s_dic[(n,m)]

down_matrix = [[1, 0, 2, 4, 3],[4, 6, 5, 2, 1], [4, 4, 5, 2, 1], [5, 6, 8, 5, 3]]
right_matrix = [[3, 2, 4, 0], [3, 2, 4, 2], [0, 7, 3, 4], [3, 3, 0, 2], [1, 3, 2, 2]]
cross_matrix = [[5, 0, 2, 1], [8 ,4, 3, 0] ,[10 , 8 ,9, 5], [5 ,6 , 4 ,7]]

print (ManhattanTourist1(4 ,4, down_matrix, right_matrix, cross_matrix))

def LCSBackTrack(v,w): 

    backtrack = ''
    for i in range(v):
        s[(i,0)] = 0
    for j in range(w):
        s[(0,j)] = 0 
    for i in range(1, v):
        for j in range(1, w):
            if v[i-1] == w[j-1]:
                match = 1
            s[(i,j)] = max(s[(i-1,j)], s[(i,j-1)], s[(i-1,j-1)] + match)

            if s[(i,j)] == s[(i-1,j)]:
                backtrack[(i,j)] = "↓"
            elif s[(i,j)] == s[(i,j-1)]:
                backtrack[(i,j)] = "→"
            elif s[(i,j)] == (s[(i-1,j-1)] + match):
                backtrack[(i,j)] = "↘"

    return backtrack

def lcs(xs, ys):
    '''Return a longest common subsequence of xs and ys.
    
    Example
    >>> lcs("HUMAN", "CHIMPANZEE")
    ['H', 'M', 'A', 'N']
    '''
    if xs and ys:
        *xb, xe = xs
        *yb, ye = ys
        if xe == ye:
            return lcs(xb, yb) + [xe]
        else:
            return max(lcs(xs, yb), lcs(xb, ys), key=len)
    else:
        return []

print (lcs("HUMAN", "CHIMPANZEE"))

b, *c = range(5)
print (b)

from collections import defaultdict, namedtuple
from itertools import product
# from http://wordaligned.org/articles/longest-common-subsequence
def lcs_grid(xs, ys):
    '''Create a grid for longest common subsequence calculations.
    
    Returns a grid where grid[(j, i)] is a pair (n, move) such that
    - n is the length of the LCS of prefixes xs[:i], ys[:j]
    - move is \, ^, <, or e, depending on whether the best move
      to (j, i) was diagonal, downwards, or rightwards, or None.
    
    Example:
       T  A  R  O  T
    A 0< 1\ 1< 1< 1<
    R 0< 1^ 2\ 2< 2<
    T 1\ 1< 2^ 2< 3\
    '''
    Cell = namedtuple('Cell', 'length move')
    grid = defaultdict(lambda: Cell(0, 'e'))
    sqs = product(enumerate(ys), enumerate(xs))
    for (j, y), (i, x) in sqs:
        if x == y:
            cell = Cell(grid[(j-1, i-1)].length + 1, '\\')
        else:
            left = grid[(j, i-1)].length
            over = grid[(j-1, i)].length
            if left < over:
                cell = Cell(over, '^')
            else:
                cell = Cell(left, '<')
        grid[(j, i)] = cell
    return grid

#print (lcs_grid('TAROT', 'ART'))

def LCSBackTrack(v,w): 
    s = {(0,0):0}
    backtrack = {(0,0):'e'}
    for i in range(len(v)):
        s[(i,0)] = 0
    for j in range(len(w)):
        s[(0,j)] = 0 
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1

            s[(i,j)] = max(s[(i-1,j)], s[(i,j-1)], s[(i-1,j-1)] + match)
            ## "↓" -> ^ "→" -> >
            if s[(i,j)] == s[(i-1,j)]:
                backtrack[(i,j)] = "^"
            elif s[(i,j)] == s[(i,j-1)]:
                backtrack[(i,j)] = ">"
            elif s[(i,j)] == (s[(i-1,j-1)] + match):
                backtrack[(i,j)] = "||"
    return backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ''
    if backtrack[(i,j)] == "^":
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[(i,j)] == ">":
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i]


v= 'AACCTTGG'
w= 'ACACTGTGA'
backtrack = LCSBackTrack(v, w)
i = len(v)-1
j = len(w)-1
a= LCSBackTrack(v,w)
print (OutputLCS(backtrack, v, i, j))
print (lcs(v,w))


import heapq
from sys import stdin, stdout
 
# Dijktra's shortest path algorithm. Prints the path from source to target.
# https://algocoding.wordpress.com/2015/03/28/dijkstras-algorithm-part-4a-python-implementation/
def dijkstra(adj, source, target):
    INF = ((63**1) - 1)//2
    pred = {x:x for x in adj}
    dist = {x:INF for x in adj}
    dist[source] = 0
    PQ = []
    heapq.heappush(PQ, [dist[source], source])

    while (PQ):
        u = heapq.heappop(PQ) # u is a tuple [u_dist, u_id]
        print (u)
        u_dist = u[0]
        u_id = u[1]
        print (dist)
        if u_dist == dist[u_id]:
            #if u_id == target:
            #    break
            for v in adj[u_id]:
                print (1, adj[u_id])
                v_id = v[0]
                w_uv = v[1]
                if dist[u_id] +  w_uv < dist[v_id]:
                    dist[v_id] = dist[u_id] + w_uv
                    print (2, dist[v_id])
                    heapq.heappush(PQ, [dist[v_id], v_id])
                    print (3, PQ)
                    pred[v_id] = u_id

                    print (4, pred[v_id])
                
    if dist[target]==INF:
        stdout.write("There is no path between " + source+ " and " + target)
    else:
        st = []
        node = target
        while(True):
            st.append(str(node))
            if(node==pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        stdout.write("The shortest path is: " + " ".join(path) + "\n\n")
        stdout.write("The distance is: " + str(dist[4]) + "\n\n")
        stdout.write("distance dictionary: " + str(dist) + "\n\n")
        stdout.write("predecessor dictionary: " + str(pred))

adj1 = {0: [(1,-7), (2,-4)], 2:[(3,-2)], 1:[(4,-1)], 3:[(4,-3)], 4:[(4,0)]}

print (dijkstra(adj1, 0, 4))