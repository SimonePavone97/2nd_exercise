from rubrica import Rubrica

nuova_rubrica = Rubrica({"Mario Rossi": "mario.rossi@gmail.com",
"Pippo Franco": "pippo_franco@hotmail.it"})

print(f"Rubrica creata con questi contatti: \n{nuova_rubrica}")

contatti_su_file = nuova_rubrica.readFile("2nd_exercise\contatti.txt")

for contatto in contatti_su_file:
    nuova_rubrica.addContact(contatto[0], contatto[1])

print(f"Rubrica con i contatti appena aggiunti: \n{nuova_rubrica}")

nuova_rubrica.saveContacts()

contatti_trovati = nuova_rubrica.searchContactsBySurname("R")
if len(contatti_trovati) == 0:
    print("Nessun contatto trovato")
else:
    print(f"Contatti cui il cognome inizia con la lettera 'R': \n{contatti_trovati}")
    
for contatti in contatti_trovati:
    nuova_rubrica.send_message(contatti)
