import requests
import pytest

def return_status_code(): # Con questa funzione voglio ottenere lo status code delle api github
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python&sort=stars&stars=>10000"
    headers = {"Accept": "application/vnd.github.v3+json", # Significa che voglio una risposta in JSON
               "User-Agent":"MyPythonScript" # Specifico al server cosa sta facendo la api call, altrimenti potrei
    } # venir bloccato (GitHub non da questo problema però)
    try:
        # Invio la richiesta HTTP con l'Url, con headers definiti e impostando 5 secondi prima di fallire
        r = requests.get(url, headers=headers, timeout=5)
        # Se la richiesta ha successo, restituisco r.status_code
        return r.status_code

    except requests.RequestException as e: # E' una classe di eccezioni che cattura tutti i possibili errori di request
        print(f"Errore nella richiesta: {e}") # Qualsiasi sia l'errore, stampo il codice dell'errore
        return None
# Senza il blocco try-except, se la richiesta fallisce, il codice si interrompe con un errore. Ora invece il programma
# Continua a funzionare anche con problemi di rete.

def test_api():
    status_code = return_status_code()
    assert status_code == 200, f"Errore: codice di stato {status_code}"