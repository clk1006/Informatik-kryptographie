import libclk
text=input("Bitte Text angeben: ")
key=int(input("Bitte Schlüssel angeben: "))
encrypting=bool(int(input("0 => Entschlüsseln; 1=> Verschlüsseln: ")))
if encrypting:
    text=libclk.purify(text)
    chars=[]
    for char in text:
        chars.append(ord(char)-97)
    text=""
    for char in chars:
        char=str(bin(char))[2:]
        while len(char)<5:
            char="0"+char
        text+=char
    textLen=len(text)
    keyLen=len(str(bin(key)))-2
    text=libclk.distribute2d(text,keyLen)
    text2=[]
    for block in text:
        num=""
        for entry in block:
            num+=str(entry)
        num=int(num,2)
        text2.append(num)
    text=""
    for num in text2:
        block=str(bin(num ^ key))[2:]
        while len(block)<keyLen:
            block="0"+block
        text+=block
    text=text[:textLen]
    chars=[]
    text=libclk.distribute2d(text,5)
    for block in text:
        num=""
        for entry in block:
            num+=str(entry)
        num=int(num,2)
        chars.append(num)
    text=""
    for char in chars:
        if(char>25):
            text+=chr(char+39)
        else:
            text+=chr(char+97)
    print(text)
else:
    chars=[]
    for char in text:
        if ord(char)<97:
            chars.append(ord(char)-39)
        else:
            chars.append(ord(char)-97)
    text=""
    for char in chars:
        char=str(bin(char))[2:]
        while len(char)<5:
            char="0"+char
        text+=char
    textLen=len(text)
    keyLen=len(str(bin(key)))-2
    text=libclk.distribute2d(text,keyLen)
    text2=[]
    for block in text:
        num=""
        for entry in block:
            num+=str(entry)
        num=int(num,2)
        text2.append(num)
    text=""
    for num in text2:
        block=str(bin(num ^ key))[2:]
        while len(block)<keyLen:
            block="0"+block
        text+=block
    text=text[:textLen]
    chars=[]
    text=libclk.distribute2d(text,5)
    for block in text:
        num=""
        for entry in block:
            num+=str(entry)
        num=int(num,2)
        chars.append(num)
    text=""
    for char in chars:
        text+=chr(char+97)
    print(text)