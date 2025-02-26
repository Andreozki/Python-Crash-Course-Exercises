import requests
from operator import itemgetter


url="https://hacker-news.firebaseio.com/v0/"
url+="topstories.json" # Questo link permette di accedere alle stories di hackernews
# situate in prima pagina

# Ora creo la variabile risposta HTTP (r) in cui con il metodo get() del modulo requests
# chiamo il nostro url. N.B. La riposta è una SINGOLA STRINGA DI TESTO
r=requests.get(url)
print(f"Status code: {r.status_code}") # Se status code = 200 allora è tutto ok

submission_ids=r.json() # Converto la risposta HTTP (r) in un dizionario Python in modo
# In questa variabile, ottengo solo i codici delle stories del sito.

submission_dicts=[]

# Creo un for loop in cui per ogni codice che leggo, lo inserisco nell'url della chiamata
# API e faccio esattamente quello che ho fatto in "hn_article.py". Creo uno slice in cui
# chiedo di controllare solo i primi 5 items in submission_ids
for submission_id in submission_ids[:5]:

    # Creo una nuova API call per ogni submission
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"id: {submission_id}\tstatus_code: {r.status_code}")
    response_dict= r.json()

    # Creo un nuovo dizionario per ogni articolo
    submission_dict={
        "title":response_dict["title"],
        "hn_link":f"https://news.ycombinator.com/item?id={submission_id}",
        "comments":response_dict["descendants"],
    }
    # Inserisco tutti i dizionari nella lista (che diventerà una lista di
    # dizionari) creata appositamente
    submission_dicts.append(submission_dict)

# Ora voglio ordinare la lista di dizionari in base al valore della chiave
# "comments". Il parametro reverse fa si che l'ordine sia decrescente. E'
# importante notare che itemgetter è un metodo della libreria "operator"
submission_dicts=sorted(submission_dicts,key=itemgetter("comments"),
                        reverse=True)

# Per ogni dizionario nella lista, printo titolo, link e numero di commenti
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
