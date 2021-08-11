import libclk
import sys
alph=input("Bitte das verschlüsselte Alphabet in Kleinbuchstaben angeben: ")
text=input("Bitte Klartext angeben: ")
isEncrypting=bool(int(input("0 => Entschlüsseln; 1=> Verschlüsseln: ")))
alph=libclk.purify(libclk.uniquify(alph))
if len(alph)!=26:
    print("Nicht alle Buchstaben sind im Alphabet enthalten")
    sys.exit(1)
text=libclk.purify(text)
geheimtext=""
for i in text:
    if isEncrypting:
        geheimtext+=alph[ord(i)-97]
    else:
        geheimtext+=chr(alph.find(i)+97)
print(geheimtext)
