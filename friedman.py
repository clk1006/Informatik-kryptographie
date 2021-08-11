import lib
text=lib.purify(input("Bitte den zu analysierenden Text angeben: "))
sprachIndex=float(input("Bitte den Koinzidenzindex der Sprache in Prozent angeben: "))/100
indexZufällig=1/26
länge=(sprachIndex-indexZufällig)*len(text)/((len(text)-1)*lib.getCoIndex(text)-indexZufällig*len(text)+sprachIndex)
print("Das Schlüsselwort hat etwa eine Länge von",round(länge),"Zeichen")