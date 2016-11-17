__author__ = 'Jonathan'
import time

def radixLSD(therange):
    """
    @author: Jonathan Luke Raj
    @purpose: Radix sort function (bucket sort)
    @since: 24042016
    @modified: 28042016
    @complexity: Best case & worst case: O(N) where N is the number of bytes in the file
    @assumption: input file only contains three columns, the first one containing characters A,C,G,T, the second containing its base4 representation and the third oe with the offset value
    """
    offset = 0
    file = open('kmers.txt','r')
    output = open("kmers_sorted.txt", "w")
    hugeArray = []
    for i in file:
        line = i.split("\t")
        hugeArray.append([])
        hugeArray[offset].append(line[0])
        hugeArray[offset].append(line[1])
        hugeArray[offset].append((line[2]).strip("\n"))
        offset += 1
    bucket = []
    for i in range(therange,2,-4):
        for l in range(256):
            bucket.append([])
        for k in hugeArray:
            bucket[int((k[1][i-4:i]),4)].append(k)
        hugeArray = []
        for j in bucket:
            hugeArray.extend(j)
        bucket = []
        for m in range(256):
            bucket.append([])
    for line in hugeArray:
        output.write(str(line[0]) + "\t" + str(line[1]) + "\t" + str(line[2] + "\n"))
    output.close()

starttime = time.clock()

radixLSD(16)
endtime = time.clock()
print(endtime-starttime)
