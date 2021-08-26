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
    text=purify(text)
    blocks=list(range(blockNumber))
    for i in range(len(blocks)):
        blocks[i]=""
    for i in range(len(text)):
        blocks[i%blockNumber]+=text[i]
    return blocks
def encryptXOR(chars,key):
    text=""
    for char in chars:
        char=str(bin(char))[2:]
        while len(char)<5:
            char="0"+char
        text+=char
    textLen=len(text)
    key=str(bin(key))[2:]
    while len(key)<textLen:
        key+=key
    key=int(key[:textLen],2)
    text=str(bin(int(text,2)^key))[2:]
    while len(text)<textLen:
        text="0"+text
    text=distribute2d(text,5)
    chars=[]
    for block in text:
        num=""
        for entry in block:
            num+=str(entry)
        num=int(num,2)
        chars.append(num)
    return chars
def extEuclid(a,b):
    [s,v,u,t]=[1,1,0,0]
    while b!=0:
        q=a//b
        b1=b
        b=a-q*b
        a=b1
        u1=u
        u=s-q*u
        s=u1
        v1=v
        v=t-q*v
        t=v1
    return [a,s,t]