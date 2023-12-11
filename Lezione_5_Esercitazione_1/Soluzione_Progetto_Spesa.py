# Inizializza una lista vuota per la spesa
lista_spesa = []

# Funzione per aggiungere un elemento alla lista della spesa
def aggiungi_elemento():
    elemento = input("Inserisci l'elemento da aggiungere alla lista della spesa: ")
    lista_spesa.append(elemento)
    print(f"{elemento} aggiunto alla lista della spesa.")

# Funzione per visualizzare la lista della spesa
def visualizza_lista():
    print("\nLista della Spesa:")
    for indice, elemento in enumerate(lista_spesa, start=1):
        print(f"{indice}. {elemento}")

# Funzione per rimuovere un elemento dalla lista della spesa
def rimuovi_elemento():
    visualizza_lista()
    if lista_spesa:
        indice = int(input("Inserisci il numero dell'elemento da rimuovere: "))
        if 1 <= indice <= len(lista_spesa):
            elemento_rimosso = lista_spesa.pop(indice - 1)
            print(f"{elemento_rimosso} rimosso dalla lista della spesa.")
        else:
            print("Indice non valido.")
    else:
        print("La lista della spesa è vuota.")

# Ciclo principale del programma
while True:
    print("\nMenu:")
    print("1. Aggiungi elemento alla lista della spesa")
    print("2. Visualizza lista della spesa")
    print("3. Rimuovi elemento dalla lista della spesa")
    print("4. Esci")

    scelta = input("Scegli un'opzione (1-4): ")

    if scelta == '1':
        aggiungi_elemento()
    elif scelta == '2':
        visualizza_lista()
    elif scelta == '3':
        rimuovi_elemento()
    elif scelta == '4':
        print("Grazie per aver usato il programma. Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")
