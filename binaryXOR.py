import lib
text=input("Bitte Text angeben: ")
key=int(input("Bitte Schlüssel angeben: "))
isEncrypting=bool(int(input("0 => Entschlüsseln; 1=> Verschlüsseln: ")))
if isEncrypting:
    text=lib.purify(text)
    chars=[]
    for char in text:
        chars.append(ord(char)-97)
    chars=lib.encryptXOR(chars,key)
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
    chars=lib.encryptXOR(chars,key)
    text=""
    for char in chars:
        text+=chr(char+97)
    print(text)