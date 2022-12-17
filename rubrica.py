# Creare un classe Rubrica con le seguenti caratteristiche:
# La classe va inizializzata con un dizionario del tipo:
    
#     {"Mario Rossi": "mario.rossi@gmail.com",
#     "Pippo Franco": "pippo_franco@hotmail.it"}

# La classe ha un metodo (class method) per leggere da file
# La classe ha un metodo per aggiungere contatti alla rubrica
# La classe ha un metodo per salvare i contatti su file
# La classe ha un metodo per trovare tutti i contatti il cui cognome ha la stessa iniziale
# La classe ha un metodo per mandare un messaggio di benvenuto ad un contatto
# specifico
# La gestione degli attributi della classe è libera. Se necessario, è possibile implementare
# metodi di supporto.

# Funzionamento della classe Rubrica :
# Importo la classe Rubrica dal file dove l'ho implementata
# Leggo da un file esterno una serie di contatti
# Aggiungo una serie di contatti alla rubrica
# Salvo la nuova rubrica su file
# Mando un messaggio di benvenuto a tutti i contatti il cui cognome inizia per "R"


class Rubrica(dict):

        
    def addContact(self, key, value):
        """ Should add the key to the dictionary if it doesn't exist """
        
        if key not in self.keys():
            self[key] = value
            
    @classmethod
    def readFile(cls, fileName):
        contacts_on_file = []
        with open(fileName, 'r') as file:
            list = file.readlines()
            for line in list:
                contacts_on_file.append(line.rstrip().split(";"))
        return contacts_on_file
    
    def saveContacts(self):
        with open("2nd_exercise\contatti_salvati.txt", 'w') as file:
            for contact in self:
                file.write(f"{contact};{self[contact]}\n")
        print("Contatti salvati sul file!")
                
    def searchContactsBySurname(self, start_letter):
        contacts_found = {}
        for contact in self.keys():
            if contact.split(" ")[1].startswith(start_letter):
                contacts_found[contact] = self[contact]
        return contacts_found 
    
    
    def send_message(self, contact_name):
        if contact_name in self.keys():
            print(f"Benvenuto/a nella mia rubrica! {contact_name}")
        else:
            print("Il contatto non esiste")

        
    
    