from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = []
        self._lag_tomt_rutenett()
        self._lag_tom_rad() 
#Lager instansvariabler fra parameter, gir rutenett sin egen liste og kaller på de to første metodene

    def _lag_tomt_rutenett(self):
        for rute in range(self._ant_rader):
            self._rutenett.append(self._lag_tom_rad())
        return self._rutenett  
#lager en for-løkke inne i self._ant_rader, der jeg appender lag_tom_rad(), som lagrer None i cellene

    def _lag_tom_rad(self):
        Liste = []
        for kolonne in range(self._ant_kolonner):
            Liste.append(None)
        return Liste
#Lager en egen liste. Lager en for-løkke for kolonner som iterer gjennom ant_kolonner og appender None i Listen

    def fyll_med_tilfeldige_celler(self):
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                self.lag_celle(rad,kolonne)
#iterer gjennom tomme listen ved å bruke to for-løkker, der jeg kaller på lag_celle med to parametre, for å fylle cellene

    def lag_celle(self, rad, kol):
        celle = Celle()
        self._rutenett[rad][kol] = celle
        tall = randint(0,2)
        if tall == 0:
            return celle.sett_levende()
#Her definerer jeg et sted i self.rutenett[rad][kol] som celle, og bruker dette til å randomizer et tall som gir levende til en celle (33%)

    def hent_celle(self, rad, kol):
        if ( 0>kol or 0>rad or rad > self._ant_rader-1 or kol > self._ant_kolonner-1):
            return None
        else: 
            return self._rutenett[rad][kol]
#Tar imot to parametere og returnerer cellen i posisjonen, men sjekker også om det er en ulovlig indeks
# Hvis kol er mindre enn 0 eller rad er mindre enn 0 eller rad er større enn ant_rader-1 eller kol er større enn ant_kolonner-1, skal det returneres None

    def tegn_rutenett(self):
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                print(self._rutenett[rad][kolonne].hent_status_tegn(),end="") 
            print("\n")
#Her lager vi rutenettet. Vi har cellene og levende celler. Det vi gjør er å itere gjennom to for-løkker og printer ut rutenettet i gitte posisjonen
#Vi setter på en print("\n") for å lage en linjeskift

    def _sett_naboer(self, rad, kol):
        cellene = self.hent_celle(rad,kol)
        rader = [rad,rad+1,rad-1]
        kolonner = [kol,kol+1,kol-1]
        for verdi1 in rader:
            for verdi2 in kolonner:
                if self.hent_celle(verdi1,verdi2) is None or verdi1 == rad and verdi2 == kol:
                    None
                else:
                    cellene.legg_til_nabo(self.hent_celle(verdi1,verdi2))
#Vi tar imot cellenes koordinater, og lager to lister for rader og kolonner, som definerer naboene rundt cellene
#Vi begynner med å itere gjennom listene rad og kolonner og lager en if-setning som kaller hent_celler med verdiene og sjekker om det er None eller om verdi1 og verdi2 er lik rad og kolonne
#Dette gir verdi None, og hvis ikke skal den ta imot en celles koordinater og sette koordinatene til cellene til som nabo for den gitte cellen. 

    def koble_celler(self):
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                self._sett_naboer(rad,kolonne)
#Itere gjennom en nøstet for-løkke, som kaller på sett_naboer med hver plass i rutenettet. 

    def hent_alle_celler(self):
        alle_celler = []
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                alle_celler.append(self._rutenett[rad][kol])
        return alle_celler
#Lager en liste. Går gjennom cellene en og en gjennom en for-løkke og appender hver plass i cellen i listen

    def antall_levende(self):
        antall_levende = 0
        for rad in self._rutenett:
            for celle in rad:
                if celle.er_levende():
                    antall_levende += 1
        return antall_levende
#lager en variabel med verdi = 0. Videre har jeg laget to for-løkker som går gjennom hver plass og sjekker om cellen er levende, ved å kalle på er_levende.
#Hvis det er levende skal variebelen som ble lagd øke verdi med +1 or returnere variabelen til slutt.