import requests
# Questo pacchetto permette di prelevare informazioni dalle API call e processarle in python

# Creo un url in cui farò una API call
url="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000" # Spezzato in due per chiarezza

# La prossima linea di codice definisce un dizionario Python chiamato intestazioni
# che verrà utilizzato come header http nella richiesta API. "accept" è un header
# HTTP che indica il tipo di contenuto che il client accetta in risposta, mentre
# "application/vnd.github.v3+json" significa che si vuole ricevere una risposta in
# formato JSON dalla GitHub API v3
intestazioni={"Accept":"application/vnd.github.v3+json"}

# Ora creo la variabile risposta (r) in cui con il metodo get() del modulo requests
# chiamo l'url e l'header definito
r=requests.get(url,headers=intestazioni)

# Controllo se la richiesta API ha avuto successo (200 = OK)
print(f"Status code: {r.status_code}")

# Visto che è andata a buon fine, converto l'oggetto response (r) in un dizionario
# con formato JSON
response_dict=r.json()

# Controlliamo quali sono le chiavi header
print(response_dict.keys())

# Stampo il value associato al total count
print(f"Total repositories: {response_dict['total_count']}")

# Stampo il contrario del valore associato al True/False di incomplete_results
# In modo da far risultare True nel caso sia completo
print(f"Complete results: {not response_dict['incomplete_results']}")

# Ora ho l'ultimo dizionario che è un nesting di altri dizionari contenenti dati riguardanti
# le repositories richieste. Assegno questa lista di dizionari alla seguente variabile
repo_dicts=response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Si può notare come i repositories returned sono solamente 30. Questo è dato da una
# impostazione di defautl dell'API di git hub, che mostra solamente 30 risultati per
# singola richiesta. Per averne di più si può modificare l'url aggiungendo alla fine:
# "per_page=x" in cui x è un numero (max 100). Altrimenti, dovremo usare la seconda pagina
# dell'url, aggiungendo alla fine "&page=x" dove x è il numero della pagina.

# Prelevo le informazioni dei primi repository
print("\n Ecco alcune informazioni riguardo i primi 30 repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository url: {repo_dict['html_url']}")