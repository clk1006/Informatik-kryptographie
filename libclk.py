import math
def constraint(x,a,b):
    if x>b:
        x=a+x-b
    elif x<a:
        x=b-a+x
    return x
def distribute2d(elements,width):
    matrix=[]
    for _ in range(math.ceil(len(elements)/width)):
        row=[]
        for _ in range(width):
            row.append(0)
        matrix.append(row)
    for i in range(len(elements)):
        matrix[i//width][i%width]=elements[i]
    return matrix
def uniquify(string):
    uniqueString=""
    for i in range(len(string)):
        if string[i] not in string[:i]:
            uniqueString+=string[i]
    return uniqueString
def find2d(array,element):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]==element:
                return [i,j]
    return -1
def countChar(text,char):
    number=0
    for i in text:
        if i==char:
            number+=1
    return number
def purify(text):
    pureText=""
    for i in text.lower():
        if 96 < ord(i) < 123:
            pureText+=i
    return pureText
def getCoIndex(text):
    text=purify(text)
    index=0
    for i in range(97,123):
        index+=countChar(text,chr(i))*(countChar(text,chr(i))-1)/len(text)/(len(text)-1)
    return index
def splitBlocks(text,blockNumber):
    blocks=list(range(blockNumber))
    for i in range(len(blocks)):
        blocks[i]=[]
    for i in range(len(text)):
        blocks[i%blockNumber].append(text[i])
    return blocks