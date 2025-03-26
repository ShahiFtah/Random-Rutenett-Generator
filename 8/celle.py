class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
#Skriver en konstruktør med instansvariablene status, naboer og ant_levende_naboer
    
    def sett_doed(self):
        self._status = "doed"
#gir self._status verdien "doed"

    def sett_levende(self):
        self._status = "levende"
#registrerer levende i self._status

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)
#legger parameter nabo i naboer, ved å bruke append

    def er_levende(self):
        #kan også bruke self._status == "levende":
        if self._status == "levende":
            return True
        else:
            return False
#lager en if/else program som returnerer om status er levende eller ikke

    def hent_status_tegn(self):
        if self.er_levende():
            return "O"
        else:
            return "."
#Lager en annen program som ligner er_levende. Her kaller vi er_levende og returnerer "0" eller "."

    def tell_levende_naboer(self):
        antall = 0
        for tell in self._naboer:
            if (tell.er_levende()):
                antall += 1
        self._ant_levende_naboer = antall 
        return self._ant_levende_naboer
#Man må først lage en variabel antall og itere gjennom verdiene og sjekke med if om verdien er levende, ved å kalle på er_levende. Er det lik så legger vi +1 til verdien antall og returnerer

    def oppdater_status(self): 
        if (self._status == "doed" and self._ant_levende_naboer == 3):
            self._status = "levende"

        elif (self._status == "levende" and self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3):
            self._status = "doed"

        elif (self._status =="levende" and self._ant_levende_naboer == 3 or self._ant_levende_naboer == 2) :
            None
#I metoden over lager vi tre if/elif setninger. Den første sier at hvis status er død og antall levende naboer er 3 skal den endres til levende
#Den andre sier at hvis status er levende og antall levende naboer er mindre enn 2 eller mer enn 3 skal den endres status død
#Den tredje sier at hvis statu er levende og antall levende naboer er 2 eller 3 skal den ikke gjøre noe, for den skal fortsatt være levende

