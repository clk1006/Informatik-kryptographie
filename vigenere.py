import libclk
text=input("Bitte die zu verschlüsselnde Nachricht einfügen: ")
schlüssel=input("Bitte das Schlüsselwort angeben: ")
ausgabe=""
i=0
for zeichen in text:
    verschiebung=ord(schlüssel[libclk.constraint(i,0,len(schlüssel)-1)])-97
    if 64<ord(zeichen)<91:
        ausgabe+=chr(libclk.constraint(ord(zeichen)+verschiebung,65,90))
    elif 96<ord(zeichen)<123:
        ausgabe+=chr(libclk.constraint(ord(zeichen)+verschiebung,97,122))
    else:
        ausgabe+=zeichen
    i+=1
print(ausgabe)