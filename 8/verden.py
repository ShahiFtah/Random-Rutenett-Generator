from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
       self._rutenett = Rutenett(rader,kolonner)
       self._generasjonsnummer = 0
       self._rutenett.fyll_med_tilfeldige_celler()
       self._rutenett.koble_celler()
#Lager instansvariabler for Rutenett ved å kalle på parameterene
#gir generasjonsnummer verdi 0 
#Kobler og fyller i konstruktøren til verden, med to metoder fra rutenett. 

    def tegn(self):
        print("\n")
        self._rutenett.tegn_rutenett()
        print("\n" + "Generasjonsnummer: ", self._generasjonsnummer)
        print("Antall levende celler: ", self._rutenett.antall_levende())
#Lager en metode tegn, der jeg kaller på teng_rutenett, printer generasjonsnummeret og printer antall_levende()

    def oppdatering(self):
        for blokk in self._rutenett.hent_alle_celler():
            blokk.tell_levende_naboer()
            blokk.oppdater_status()
        self._generasjonsnummer +=1
#I metode oppdatering lager vi en for løkke som iterer gjennom listen for cellene, der vi kaller på tell_levende_celler, og oppdater_status.
#i tillegg øker vi generasjonsnummer med +1 for hver gang oppdatering blir kalt på, som betyr for hver gang vi trykker på enter. 