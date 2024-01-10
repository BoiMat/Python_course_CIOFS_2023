import requests

# URL dell'API di JSONPlaceholder
api_url = 'https://jsonplaceholder.typicode.com/todos/1'

# Ottieni i dati JSON dall'API
response = requests.get(api_url)
data = response.json()

# Estrai le informazioni richieste
task_title = data['title']
task_completed = data['completed']
user_id = data['userId']

# Stampate le informazioni
print(f'Titolo dell\'attività: {task_title}')
print(f'Stato completamento dell\'attività: {"Completato" if task_completed else "Incompleto"}')
print(f'ID dell\'utente a cui è assegnata l\'attività: {user_id}')