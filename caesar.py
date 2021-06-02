import libclk
text=input("Bitte die zu verschlüsselnde Nachricht einfügen: ")
verschiebung=int(input("Bitte Verschiebung angeben: "))
ausgabe=""
for zeichen in text:
    if 64<ord(zeichen)<91:
        ausgabe+=chr(libclk.constraint(ord(zeichen)+verschiebung,64,90))
    elif 96<ord(zeichen)<123:
        ausgabe+=chr(libclk.constraint(ord(zeichen)+verschiebung,96,122))
    else:
        ausgabe+=zeichen
print(ausgabe)