##problem 1

import json
with open('blosum62.json', 'r') as f:
    blosum62 = json.load(f)

def GlobalAlignment(v,w, blosum62, sigma=5):
    D = []
    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    
    for i in range(len(v)+1):
        D.append([0]* (len(w)+1))

    for i in range(len(v)+1):
        a = [h*-5 for h in range(len(v)+1)]
        D[i-1][0] = a[i-1]

    for i in range(len(w)+1):
        a = [h*-5 for h in range(len(w)+1)]
        D[0][i-1] = a[i-1]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            distRight = D[i][j-1] - sigma
            distDown = D[i-1][j] - sigma
            distDiag = D[i-1][j-1] + blosum62[v[i-1]][w[j-1]]
            DirectionScore = [distDown,distRight,distDiag]
            D[i][j] = max(distRight,distDown,distDiag)
            backtrack[i][j] = DirectionScore.index(D[i][j])

    for row in D:
        for column in row:
            print 
        #print (row)

    for row in backtrack:
        for column in row:
            print 
        #print (row)

    #init
    v_aligned, w_aligned  = v, w
    
    #get pos of highest scoring cell in the matrix and score
    i, j = len(v), len(w)
    max_score = str(D[i][j])

    #backtrack to the edge of the matrix starting at the highest scoring cell 
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    for repeat in range(j):
        v_aligned = insert_indel(v_aligned, 0)

    for repeat in range(i):
        w_aligned = insert_indel(w_aligned, 0)

    return max_score, v_aligned, w_aligned

#print (GlobalAlignment('PLEASANTLY','MEANLY', blosum62))
M = (GlobalAlignment('PLEASANTLY','MEANLY', blosum62))


#######---WORKS---#######
PAM250 = {'A': {'A': 2, 'C': -2, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': -1, 'M': -1, 'L': -2, 'N': 0, 'Q': 0, 'P': 1, 'S': 1, 'R': -2, 'T': 1, 'W': -6, 'V': 0, 'Y': -3}, 'C': {'A': -2, 'C': 12, 'E': -5, 'D': -5, 'G': -3, 'F': -4, 'I': -2, 'H': -3, 'K': -5, 'M': -5, 'L': -6, 'N': -4, 'Q': -5, 'P': -3, 'S': 0, 'R': -4, 'T': -2, 'W': -8, 'V': -2, 'Y': 0}, 'E': {'A': 0, 'C': -5, 'E': 4, 'D': 3, 'G': 0, 'F': -5, 'I': -2, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'D': {'A': 0, 'C': -5, 'E': 3, 'D': 4, 'G': 1, 'F': -6, 'I': -2, 'H': 1, 'K': 0, 'M': -3, 'L': -4, 'N': 2, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'G': {'A': 1, 'C': -3, 'E': 0, 'D': 1, 'G': 5, 'F': -5, 'I': -3, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -3, 'T': 0, 'W': -7, 'V': -1, 'Y': -5}, 'F': {'A': -3, 'C': -4, 'E': -5, 'D': -6, 'G': -5, 'F': 9, 'I': 1, 'H': -2, 'K': -5, 'M': 0, 'L': 2, 'N': -3, 'Q': -5, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -1, 'Y': 7}, 'I': {'A': -1, 'C': -2, 'E': -2, 'D': -2, 'G': -3, 'F': 1, 'I': 5, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -2, 'S': -1, 'R': -2, 'T': 0, 'W': -5, 'V': 4, 'Y': -1}, 'H': {'A': -1, 'C': -3, 'E': 1, 'D': 1, 'G': -2, 'F': -2, 'I': -2, 'H': 6, 'K': 0, 'M': -2, 'L': -2, 'N': 2, 'Q': 3, 'P': 0, 'S': -1, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': 0}, 'K': {'A': -1, 'C': -5, 'E': 0, 'D': 0, 'G': -2, 'F': -5, 'I': -2, 'H': 0, 'K': 5, 'M': 0, 'L': -3, 'N': 1, 'Q': 1, 'P': -1, 'S': 0, 'R': 3, 'T': 0, 'W': -3, 'V': -2, 'Y': -4}, 'M': {'A': -1, 'C': -5, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 2, 'H': -2, 'K': 0, 'M': 6, 'L': 4, 'N': -2, 'Q': -1, 'P': -2, 'S': -2, 'R': 0, 'T': -1, 'W': -4, 'V': 2, 'Y': -2}, 'L': {'A': -2, 'C': -6, 'E': -3, 'D': -4, 'G': -4, 'F': 2, 'I': 2, 'H': -2, 'K': -3, 'M': 4, 'L': 6, 'N': -3, 'Q': -2, 'P': -3, 'S': -3, 'R': -3, 'T': -2, 'W': -2, 'V': 2, 'Y': -1}, 'N': {'A': 0, 'C': -4, 'E': 1, 'D': 2, 'G': 0, 'F': -3, 'I': -2, 'H': 2, 'K': 1, 'M': -2, 'L': -3, 'N': 2, 'Q': 1, 'P': 0, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -2, 'Y': -2}, 'Q': {'A': 0, 'C': -5, 'E': 2, 'D': 2, 'G': -1, 'F': -5, 'I': -2, 'H': 3, 'K': 1, 'M': -1, 'L': -2, 'N': 1, 'Q': 4, 'P': 0, 'S': -1, 'R': 1, 'T': -1, 'W': -5, 'V': -2, 'Y': -4}, 'P': {'A': 1, 'C': -3, 'E': -1, 'D': -1, 'G': 0, 'F': -5, 'I': -2, 'H': 0, 'K': -1, 'M': -2, 'L': -3, 'N': 0, 'Q': 0, 'P': 6, 'S': 1, 'R': 0, 'T': 0, 'W': -6, 'V': -1, 'Y': -5}, 'S': {'A': 1, 'C': 0, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': -1, 'P': 1, 'S': 2, 'R': 0, 'T': 1, 'W': -2, 'V': -1, 'Y': -3}, 'R': {'A': -2, 'C': -4, 'E': -1, 'D': -1, 'G': -3, 'F': -4, 'I': -2, 'H': 2, 'K': 3, 'M': 0, 'L': -3, 'N': 0, 'Q': 1, 'P': 0, 'S': 0, 'R': 6, 'T': -1, 'W': 2, 'V': -2, 'Y': -4}, 'T': {'A': 1, 'C': -2, 'E': 0, 'D': 0, 'G': 0, 'F': -3, 'I': 0, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -1, 'T': 3, 'W': -5, 'V': 0, 'Y': -3}, 'W': {'A': -6, 'C': -8, 'E': -7, 'D': -7, 'G': -7, 'F': 0, 'I': -5, 'H': -3, 'K': -3, 'M': -4, 'L': -2, 'N': -4, 'Q': -5, 'P': -6, 'S': -2, 'R': 2, 'T': -5, 'W': 17, 'V': -6, 'Y': 0}, 'V': {'A': 0, 'C': -2, 'E': -2, 'D': -2, 'G': -1, 'F': -1, 'I': 4, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -1, 'S': -1, 'R': -2, 'T': 0, 'W': -6, 'V': 4, 'Y': -2}, 'Y': {'A': -3, 'C': 0, 'E': -4, 'D': -4, 'G': -5, 'F': 7, 'I': -1, 'H': 0, 'K': -4, 'M': -2, 'L': -1, 'N': -2, 'Q': -4, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -2, 'Y': 10}}

#does not work well
def localAlignment(v, w, PAM250, sigma = 5):
    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    D = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            distZero = 0
            distRight = D[i][j-1] - sigma
            distDown = D[i-1][j] - sigma
            distDiag = D[i-1][j-1] + PAM250[v[i-1]][w[j-1]]
            DirectionScore = [distDown,distRight,distDiag, distZero]
            D[i][j] = max(distZero, distRight, distDown, distDiag)
            backtrack[i][j] = DirectionScore.index(D[i][j])

    for row in D:
        for column in row:
            print 
        #print (row)

    for row in backtrack:
        for column in row:
            print 
        print (row)

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            #finding maximum value from a list of lists
            if D[i][j] == max([sublist[-1] for sublist in D]):
                max_score = str(D[i][j])
                a = i
                b = j
                #print (a,b, max_score)

    i = a    
    j = b

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            #print (w_aligned)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            #print (v_aligned)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned

def localAlignment2(v, w, PAM250, sigma = 5):
    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    D = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            distZero = 0
            distRight = D[i][j-1] - sigma
            distDown = D[i-1][j] - sigma
            distDiag = D[i-1][j-1] + PAM250[v[i-1]][w[j-1]]
            DirectionScore = [distDown,distRight,distDiag, distZero]
            D[i][j] = max(distZero, distRight, distDown, distDiag)
            backtrack[i][j] = DirectionScore.index(D[i][j])

    for row in D:
        for column in row:
            print 
        print (row)
    try:
        lst = []
        for i in range(1, len(v)+1):
            lst.append((max([sublist[i-1] for sublist in D])))
    except:
        pass

    a1 = (max(lst))

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
                #finding maximum value from a list of lists
            if a1 == D[i][j]:
                max_score = str(D[i][j])
                optloc  = (i, j)

    i, j = optloc

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            #print (w_aligned)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            #print (v_aligned)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned

v = 'AMTAFRYRQGNPRYVKHFAYEIRLSHIWLLTQMPWEFVMGIKMPEDVFQHWRVYSVCTAEPMRSDETYEQKPKPMAKWSGMTIMYQAGIIRQPPRGDRGVSDRNYSQCGKQNQAQLDNNPTWTKYEIEWRVQILPPGAGVFEGDNGQNQCLCPNWAWEQPCQWGALHSNEQYPNRIHLWAPMSKLHIKIEKSSYNRNAQFPNRCMYECEFPSYREQVDSCHYENVQIAFTIFSGAEQKRKFCSCHFWSNFIDQAVFSTGLIPWCYRRDDHSAFFMPNWNKQYKHPQLQFRVAGEGTQCRPFYTREMFTKVSAWRIAGRFAGPYERHHDAHLELWYQHHKVRTGQQLGIIWNNRDKTRNPCPFSAYYNKLPWWKINQNAFYNCLQNIAHSTHDETHEFNPVKCIDWLQGTMVPTECKKGFVHEKCECYRNPGPPLHDMYHQMEDIFGVRFDCLTGWKHLSDYNPCQERRNINDFYIFAYEIAPAVKNLVLSPQPLADATKKCAFNYTPLDQSPVVIACKWYIHQPICMLLIVLICAMDKYNAHMIVIRTTEGQQPMHACRMTEGPGMCMKEPLVTFTLPAQWQWPNHEFKYVYMYVLNYHLSQYTYTDEGHAGGQHYSFNVAVDVGMAWGHNRCYCQPACYSQQETQTRTIDYEKWQYMKHQAFKWGLWFCEQERHAWFKGQNRCEMFTAKMTRMGADSNLDQYKLMLAQNYEEQWEQPIMECGMSEIIEIDPPYRSELIFTFWPFCTYSPWQNLIKCRCNNVIEEMDQCVPLTFIGFGVKQAGGIQAWAFYKEEWTSTYYLMCQCMKSDKAQYPYEIILFWMQPMDTGEQEPPQQNMWIFLPHSWFFDWCCNAPWSEICSSRHDHGQCQDAFYPCELFTVFDDIFTAEPVVCSCFYDDPM'
w = 'WQEKAVDGTVPSRHQYREKEDRQGNEIGKEFRRGPQVCEYSCNSHSCGWMPIFCIVCMSYVAFYCGLEYPMSRKTAKSQFIEWCDWFCFNHWTNWAPLSIVRTSVAFAVWGHCWYPCGGVCKTNRCKDDFCGRWRKALFAEGPRDWKCCKNDLQNWNPQYSQGTRNTKRMVATTNQTMIEWKQSHIFETWLFCHVIIEYNWSAFWMWMNRNEAFNSIIKSGYPKLLLTQYPLSQGSTPIVKPLIRRDQGKFWAWAQMWWFREPTNIPTADYCHSWWQSRADLQNDRDMGPEADASFYVEFWYWVRCAARTYGQQLGIIWNNRLKTRNPCPYSADGIQNKENYVFWWKNMCTKSHIAFYYCLQNVAHYTHDVTAEFNPVKCIDWLQGHMVLSSWFKYNTECKKLFVHEKCECYRMFCGVVEDIFGVRFHTGWKHLSTAKPVPHVCVYNPSVQERRNINDFYIFYEIAPAVKNLVLSAQPLHDYTKKCAFNYTPITITRIISTRNQIIWAHVVIACQFYSPHQMLLIELAMDKYCADMNVRRSTEGHQPMHACRSTFGPGMAAKEPLVTFTLVAFWQWPNHEFQYVYMYTEDKIIQIGPHLSNGCEMVEYCVDCYAKRPCYRAYSAEAQYWRMITEAEDYSYKTRNAIAATATVRGQYCHPFRWLGIVWMAHHDCFFANECGTICIPQMAEMRPPETTPYEIDIIFMMFWKEHMSTTILDVVGMYRPATFSHWHDAHHQCEPYLTPLMCQSKLVFDAAFTQVGVKGVWYHTEKLELMAGFNHMKFKKEEAQQSCFYWFQDCPDYDPPDAVRKTDEKHIRAHGEIWWLMRYYCMYHILHIASRHEWMHLRWDQACTNPGYELFEFIPWVLRRYVVYDKIRYNYSYRNSASMEFV'
v1, w1 = 'MEANLY', 'PENALTY'
v3, w3 = 'AAAAAASSSSSSSVVVVVVVVTTTTTTTLLLLLL','SSSSLLLLLTTTTTTTWWWWWWWWWWWPPPPPPPPPP'
v2, w2 = 'ATGVWYYYYC','GYYCFFF'
v4, w4 = 'PLEASANTLY', 'MEANLY'
#print (localAlignment2(v4, w4, PAM250))


import sys
sys.setrecursionlimit(10000)
# A Naive recursive Python program to fin minimum number 
# operations to convert str1 to str2 
def editDistance(str1, str2, m , n): 
  
    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m==0: 
         return n 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n==0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                   editDistance(str1, str2, m-1, n-1)    # Replace 
                   ) 

v5 = 'KIEIAADMWEFEAWTSHTQQANNREQIPWVQCYQLNVEQMDFANQYKILLFTTITNFWWYRYGGDMHETAMIYVFINDIYCMQDDCTFSMYVMTWTGGMKRTAPTNGNEAFNLSKTPVHKQEMQFDDFFEYTWIIEMESWEFDSLMKHESALADHWPKIHVKKDKEDGCGITIDQSTWLHKVEKGDNCITLADVQVPINEECKKRWTHIQDIMGQNVSLKRFLGRKFRAPEHITTQSKCMEPHPYCHLCECFTYHGSIRDPNRAGVFKYGNWWRLYSLISYAYHNDGVSDLFKTSYVSAAWMGPGDDQDSMQHTTDCCHPNVDPADERWTIGWEIYEYGWEVLFSVLDYNNCCDESQGTWCVNARLILPQNTNTFSMVGLTANGYNMNLADGCLSQPGLYHFPKAKSDEIGIAHRDQQSHAPNQKQDNLHLTLPLRICTPHGLINRMCHQTHWFPFAPYLSNFEEHCFEMLWTYSSNRDEWDTISTKLGPHVTWFLLHHKVDQPNLQEGHHQLTWTKFLLNRPKLQWFRYQRMVLAPKTFQCDVQIQANPLADDHAPDDIEDGISYTPQDYNWCLEWCYDHKRPHREQTCLSFFQYKRRGEFVGRKEPPLHSGTHKHQPHLPKWVMRAVSDRANTFNERWIVGSDNYLEPRINQDRYDHEQGAVIQITHSCTTFVKTEHWRREFSKLPFQTVFGGVQKMRWIKFDRHHKTSSMTTRVYHQEVKGWTLDVKNTRDRETIQVLVTKYRENVRESQRPENCWTHPDYNAAICHHHQGTQCACNPGGDYPIVERTDFLWTSGHHMLILMRKFIYNICECRVLMKEMSDAKGHPFAFHDKRNLKINDAISEMPVWLAVNMGQWFFYKYFFQAAQYMKWDYSNHRESESANHDQHQ'
w5 = 'GIEIAADMWEFEMDWHWWPCMLYALFKHTVQANREQIPWVQCYQLNVEQMDFGFARRTVHAAKNYWAKYEYKILLFTTIKDEPENFKAMDWYQRGTHKWNETAAIYVFINDIYCMQDDCTFSMYVMTWTKCWGMKRGNPCNALVAPTNGNEAFNLSKTPVHKQIALICTEYQKCNIIEMESWEFDSHYPKDHVKKDKECGITIDWVWLHFAAYVEIGDCITLADVQVPIREEMQYINDAPRLTGRHCQDILKRFLGRFVLSQMVHNFGRLYPPIWAPEHITISKQSPLCMCFTYHGSGSVRLDGYEWMVDWRGRAGVKFAYHGTTPNGVSDLSYVSASYHRVDHGRDGPGSMQHTMDCGHLEWHKYHPNVDPADERQFKTIGWEGYEYGWYVLYVYYHTQRVLLYNNGCDWYSNISFSTGAGRPPTCCVNARLILPQIPHWYVSPTNTFSDQKPVFLTANGYIKAGGMNLADGCENESQPGLYHVIKAKSDEMYCWASVGIAHRDQQSHFEHWPAPNQKQDNLHMTLPLRICTAGAGRCWAWTLMSHLFPSNFEEICTAQPWRREMLCFCVWIQYSSNRDHARPVEAWKTISTKLGPHFCEPRSGFWDQPNLQEGHMQLTWTKQVGILGLTCAEPFNWFRYQRMVLAPKTFQSCMMKGDVQIQANPLADDHAIKLGISLEWCYTYHFSHKRGHREYTCLSFWLITFLFVGRKEPAFEQGSEYNWCVGNYSGTHKHQPHWYLPQRWRSWNTMNERWFRSIIRHCRVGSDNYLECRINQDYSAQWLRYGITHRDPVDKYKCTTEFSLPFQTVFGGVQKMRKSSMTQVDPLWQQRNVCIKKGWTLDVKVVTRDRETIVVYRENEDGRPENHHCQGTQCACNPGGDYPIVERTDFLWTSGHHMLILMRKFIYNICECRVLMKEMSDAKGHPFAFHDKRALMGNDAISEMPVWLAVNMGQWFFYLYFFPAAQYMKWQYSNHFESESANHIQIT'
#print (editDistance(v4, w4, len(v4), len(w4)))

def GlobalAlignmentForEditDistance(v,w, sigma=-1):
    D = []
    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    
    for i in range(len(v)+1):
        D.append([0]* (len(w)+1))

    for i in range(len(v)+1):
        a = [h*-5 for h in range(len(v)+1)]
        D[i-1][0] = a[i-1]

    for i in range(len(w)+1):
        a = [h*-5 for h in range(len(w)+1)]
        D[0][i-1] = a[i-1]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            distRight = D[i][j-1] - sigma
            distDown = D[i-1][j] - sigma
            if v[i-1]==w[j-1]:
                distDiag = D[i-1][j-1] + 0
            else:
                distDiag = D[i-1][j-1] - sigma
            DirectionScore = [distDown,distRight,distDiag]
            D[i][j] = max(distRight,distDown,distDiag)
            #backtrack[i][j] = DirectionScore.index(D[i][j])

    for row in D:
        for column in row:
            print 
        #print (row)

    for row in backtrack:
        for column in row:
            print 
        #print (row)

    #get pos of highest scoring cell in the matrix and score
    i, j = len(v), len(w)
    max_score = str(D[i][j])

    return max_score

def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1,ch2 in zip(s1,s2))
#print (GlobalAlignmentForEditDistance(v4, w4))
#print (hamming_distance(v4, w4))

def fittingALignment(v1, w1):
    if v1>w1:
        v, w= v1, w1
    else:
        v, w= w1, v1

    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    D = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            distRight = D[i][j-1] - 1
            distDown = D[i-1][j] - 1
            if v[i-1]==w[j-1]:
                distDiag = D[i-1][j-1] + 1
            else:
                distDiag = D[i-1][j-1] -1 
            DirectionScore = [distDown,distRight,distDiag]
            D[i][j] = max(distRight,distDown,distDiag)           
            backtrack[i][j] = DirectionScore.index(D[i][j])
            
    for row in D:
        for column in row:
            print 
        #print (row) 

    for row in backtrack:
        for column in row:
            print 
        #print (row) 

    #print (len(w))
    try:
        lst = []
        for i in range(0, len(v)+1):
            lst.append(D[i][len(w)])
    except:
        pass
    #print (lst)
    a1 = (max(lst))


    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
                #finding maximum value from a list of lists
            if a1 == D[i][j]:
                max_score = str(D[i][j])
                optloc  = (i, j)

    i, j = optloc

    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            #print (w_aligned)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            #print (v_aligned)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned

    #return optloc, max_score

v6, w6 = 'GTAGGCTTAAGGTTA', 'TAGATA'
#print (fittingALignment(v6, w6))

v7 = 'CAATCACCCCAATCCCTCAATCCTGGCCCCACGCATAGGCTAATGCCAATCGCGGCCAGGGTATAACCGCCATAACTGTGGGTCAGAAGGGATAAGTTCCACAATCCTATTTTCCTCGAGGCGCTTCGATGCGTTAACGCGTACACTCTGTCGGCCAACCGTGTGGGAGCCGAATTGGCTGGGCTGTTGAACATTCTATCAGTAGATAAACGAAGGTACATCCGAGGTTGTCGATCGACCGCGGGGTCGTAGCGCGTGCATGTTCCTTTCAGGCCCACATACTCCGGAACGGTTCATATCACGACTATTCTTGCACAATCGGACAACGGTGTACCATGGTGGACACCGTAGGAGACCAATACTGCGTAAATCATAAGCATTGGAGAGTGGACTGCTAGCGAGGCTCACCATGGAGTCTCGGTCGGCATCTCCTGACTGCTGTTCCATCGCGTTTTTCTTTTACTCACGCAATAAATCAATACCCCCTAACACAGGCCTGCTCCAGCCTTATTAAGGCCATAGTAGCTCTACATGTAGACCGAACGGAAGCACAGTTTGGTAGAAATTCTTAATCGACTATGGTCCGTGCAGGCCAAAAAAGGAATAATCTTCGAATTCTCACGCCTTCATTAGGGCGCACATGGTGGGGTAAATCACTGCACTCTGTTCGCAGTTAAGCGTTGCAATCAATATCGGCAGAACTCGGAGTCCGTATAAAGCCGCCTCAGCGTGCACACGCCCGTGCGGCACGTCATTAGACGAGGATTCCGGGGGACTGGCCTGTTCGTAATCCACTAAAACAATGGTCCTACCATCTAAAACGCACCGTGTTCCCCTCTACGGGAACCCCCTAGAT'
w7 = 'AGAGCGCAGAGAAGTCATTAGAACATGTAGCACATCGCTTATTAAGGGTCAATACCTAAAGGGCCTAACTATACGCCACACGGAACAGCTC'

#print (fittingALignment(v7, w7))

def overlapAlignment(v,w):
    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    D = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            distRight = D[i][j-1] - 2
            distDown = D[i-1][j] - 2
            if v[i-1]==w[j-1]:
                distDiag = D[i-1][j-1] + 1
            else:
                distDiag = D[i-1][j-1] - 2
            DirectionScore = [distDown,distRight,distDiag]
            D[i][j] = max(distRight,distDown,distDiag)           
            backtrack[i][j] = DirectionScore.index(D[i][j])
    

    a1 = (max(D[len(v)]))

    for row in D:
        for column in row:
            print 
        #print (row) 

    for row in backtrack:
        for column in row:
            print 
        #print (row) 

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
                #finding maximum value from a list of lists
            if a1 == D[i][j]:
                max_score = str(D[i][j])
                optloc  = (i, j)

    i, j = optloc

    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            #print (w_aligned)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            #print (v_aligned)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned

vv = 'GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA'
ww = 'TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG'
v11, w11 = 'PAWHEAE', 'HEAGAWGHEE'

vv1 = 'CCTCCACGGTCCCCTTAAACTCCGACATGACCCCGTGTTCAGTCTGCCATAATACAAGGATGGTTAGGTATCACAGGACTCAATGCCCGGCTAATACAGCCTAACAATATTAACGAGACGACAATTTAATTGTACAATTCATGTTCGGACAGATATACACCGGTAGGTCTACCCATATTATGTGATCACGTGGACATCAAACAGGGCCTGGTGCGTATCTAAGGATCTTTGAAGTTACACTTTCCCCCACGGCAATAAAAACTCCTGGCGAACATTAGGGTATATACAAGGAGTCCTGGCGTTTACTCTACTCTTGCGAGCTAGTGAGTCAAGCGTTACAACCGGCGTGATCACATAGCTGACGGGTATGTTACAGCCATTCGCTAGATATGCATAGTCCGCTCAGTGTTATCTTTGCCTTTGGCAAGACGTGAGTAGCGAGTCATGGAAGCGCATCTAGCTCATCAACACTACTTTTCCGAAGAGATTTGACGTTCAAGTAATTGGTAGAAGAACTCCAGTTATTGGTGTTGGGAGGCAGATACCTGCAGGTGTGCTTGCGTCACAAGGCTATGTGCAAGGATCGAATCGCTCCCGTCTTTCCCACGGCTATAAAGCTCCTACGCCACCCCACCGAGAATATTCGTGCAAAATGATGCAAATTAGTTGCAGTCGTACCGTGAATTCTCAACCTTTATGACGAGGGCGCCACGCTTTGCCTATAAGGATGAAAGATCATTATTTCAGAATGTGCACACATCAAATGGCTGAAACTTATAGGTCCAATACGAACCCATTTGTCGTCGTCACCGGAGGTGTATCCCCACGCTGGCTCGTTACGTAGTCTGTACCACCACGATAATGGTTTGCAACACGCTATTGTGTTTGTGCCGACATATCGTCCTTGTTCTGCGC'
ww1= 'CTACCTTTGTGGCGAGGGGCCACCCTAGCCTAAAAGTAAAGGTCATTATTCCGAGTAGTGCCGCACAGCTCAAACAGCTGAACCCCAGTCGAACGACTCATTGTCGCGCCGTCCCGGGGGTGTATCCCATTTTGCCCGATACGTAGTTTATCCTCACATAATTTCCTGCAACACGCTATTGTATTATGCCGACAATCGCTTGTTTCGAGCAAATAACATCTTTCATGCGACTCCAAGGTCGGTGGGTGAATTGGTCTTTCATCAAGCAGCACAGGATCGAGCGTTTAACGAAGAAACAGGGCGACACAATACATTCGGTGCCCAAAAAGTGTGTCCTATCCGTATCTCGAGGGCAACGCACCAATTCTTATTCATACCACGCAACCGTCGGCTGCCCCTTCCAGCGGTCAGTAACGCCCGGGCCGCTCCTATTGGTTCCGCGCGATACTACGGTTATCGCCTATGGTCAGTATGTGACTTGGATGCAGCTGCCTGATCGTCTAGGACAAGAGCTACCTAAGGATTCTTAACATGCGGTCTAAGAGCAATCGATGAAGAGGGCCCTCTTCGCTCCACGCTACAAACTTCCGCGAAGCTTCAGTATCATCTGCCATAGCCACCTTTGTTTCAGCCAGACATTTTGGGAGACACTTGCGCAACCACCCCCTTACTTGGGCCCTATATAATCACCTAGCCTCTCTATGGTACCATACTGTTCCATTTACTCTTGAGAGCTTTTAGTATAGGGTTGTTGGGGAGGATCTGCGGCGTGTACAGGGACATAAATCCGGCATCACGCACCTCGCTAATGCGTTCCGAAAGGGCAGATGCG'
print (overlapAlignment(vv2,ww2))