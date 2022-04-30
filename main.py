class Ksiazka():
    def __init__(self,tytul,autor):
        self._tytul = tytul
        self._autor = autor
        self._counter = 1
    def getTytul(self):
        return self._tytul
    def getAutor(self):
        return self._autor
    def getCounter(self):
        return self._counter
    def setCounter(self,a):
        self._counter +=a


listaKsiazek = list()
liczbaKsiazek = int(input())
for i in range(liczbaKsiazek):
    egzemplarz = eval(input())
    ksiazka = Ksiazka(egzemplarz[0],egzemplarz[1])

    if len(listaKsiazek) == 0:
        listaKsiazek.append(ksiazka)
    else:
        czyKsiazkaTaSama = False
        for line in listaKsiazek:

            if line.getAutor() == ksiazka.getAutor() and line.getTytul() == ksiazka.getTytul():
               line.setCounter(1)
               czyKsiazkaTaSama = True
        if czyKsiazkaTaSama == False:
            listaKsiazek.append(ksiazka)

listaKrotek = []

for line in listaKsiazek:
    linijka =  line.getTytul(),line.getAutor(),line.getCounter()
    listaKrotek.append(linijka)

listaNowa = sorted(listaKrotek)
for line in listaNowa:
    print(line)
