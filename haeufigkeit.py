from lib import purify
text = input("Bitte einen Text einfügen: ")
text = purify(text)
haeufigkeiten = []
for i in range(26):
    haeufigkeiten.append(0)
for i in text:
    haeufigkeiten[ord(i)-97]+=1
ausgabe=""
for i in range(len(haeufigkeiten)):
    ausgabe+=chr(i+97)+"  "+str(haeufigkeiten[i])+"  "+str(haeufigkeiten[i]/len(text)*100)+"%\n"
print(ausgabe)
