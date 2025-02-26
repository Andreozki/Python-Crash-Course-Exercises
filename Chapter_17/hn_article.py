import requests
import json # In questo caso il json che riceviamo è incasinato quindi utilizzeremo
# il modulo per assegnarlo a una variabile e leggerlo con indent assegnato

url="https://hacker-news.firebaseio.com/v0/"
url+="item/43182325.json"

# Ora creo la variabile risposta HTTP (r) in cui con il metodo get() del modulo requests
# chiamo il nostro url. N.B. La riposta è una SINGOLA STRINGA DI TESTO
r=requests.get(url)
print(f"Status code: {r.status_code}") # Se status code = 200 allora è tutto ok

response_dict=r.json() # Converto la risposta HTTP (r) in un dizionario Python in modo
# da poter accedere a singole key e values
response_string=json.dumps(response_dict,indent=4) # Adesso il problema è che il dizionario
# Python si sviluppa su una sola riga. Ripassiamo a JSON formattando il testo con un
# indent che migliora la visualizzazione.
print(response_string)