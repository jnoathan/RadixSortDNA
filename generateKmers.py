__author__ = 'Jonathan'
import time

def main(k):
    """
    @author: Jonathan Luke Raj
    @purpose: Main function
    @since: 24042016
    @modified: 28042016
    @complexity: Best case & worst case: O(N) where N is the length of the characters in the file
    @assumption: input file only contains characters A,C,G,T
    """
    therange = k
    kmerno = []
    count = 0
    file = open("longstring.txt", "r")
    output = open("kmers.txt", "w")
    string = file.read()
    dict = {'A':'0','C':'1','G':'2','T':'3'}
    for i in range(len(string)- therange):
        kmerlist = string[count:therange+count]
        for j in kmerlist:
            kmerno.append(dict[j])
        output.write(''.join(kmerlist) + "\t" + ''.join(kmerno) + "\t"+ str(count) + "\n")
        kmerno = []
        count +=1
    output.close()
