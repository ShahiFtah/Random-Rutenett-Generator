from verden import Verden

def hovedprogram():
    input_rad = int(input("Tast inn ønsket antall rader: "))
    input_kolonne = int(input("Tast inn ønsket antall kolonner: "))
    #Lager to input, som spør om antall rad og kolonne
    
    gameoflifebrett = Verden(input_rad, input_kolonne)
    #Legger brukerens rad og kolonne inn i en objekt
    
    gameoflifebrett.tegn()
    #Kaller på tegn() med objektet for å tegne programmet
    
    flereHandlinger = ""
    #Lager en tom variabel flereHandlinger som vi skal bruke videre

    while flereHandlinger != "q":
        flereHandlinger = input("Trykk ENTER for å legge til en ny generasjon eller q for å avslutte:")

        if flereHandlinger == "":
            gameoflifebrett.oppdatering()
            gameoflifebrett.tegn() #tegner et nytt rutenett, skriver ut generasjon og viser antall levende celler
#Vi lager en while løkke som sier at den vil kjøre så lenge vi ikke taster "q"
#for hver gang spillet starter får brukeren en spørsmål om den vil taste enter eller q
#Fra her lager vi en if setning som gir brukeren det den vil dersom brukeren taster enter
#Da kaller vi på oppdatering og tegn igjen for å kjøre programmet. 


hovedprogram()