import libclk
text=input("Bitte die zu ver-/entschlüsselnde Nachricht einfügen: ")
schlüssel=input("Bitte das Schlüsselwort in Kleinbuchstaben angeben: ")
kodieren=bool(int(input("1 für verschlüsseln/0 für entschlüsseln: ")))
for i in range(97,123,1):
    schlüssel+=chr(i)
schlüssel=libclk.uniquify("j"+schlüssel)
matrix=libclk.distribute2d(schlüssel[1:],5)
if kodieren:
    reintext=""
    for i in text.lower():
        if ord(i) in range(97,123):
            reintext+=i
    textFormatiert=""
    for i in range(len(reintext)):
        if i%2!=0 and reintext[i-1]==reintext[i]:
            if reintext[i]=="x":
                textFormatiert+="q"
            else:
                textFormatiert+="x"
        textFormatiert+=reintext[i]
    if len(textFormatiert)%2!=0:
        if reintext[-1]=="x":
            textFormatiert+="q"
        else:
            textFormatiert+="x"
    