import requests
import plotly.express as px

url="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000"

intestazioni={"Accept":"application/vnd.github.v3+json"}
r=requests.get(url,headers=intestazioni)
print(f"Status code: {r.status_code}")

response_dict=r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts=response_dict['items']

# Creo tre liste separate, in cui inserirò con un semplice ciclo for, i valori associati a
# link e stelle delle repositories analizzate, oltre che alle info per l'hover sui risultati.
repo_links,stars,hover_texts=[],[],[]
for repo_dict in repo_dicts:

    repo_name=(repo_dict['name'])
    repo_url=(repo_dict['html_url'])
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    # E' una stringa con un anchor tag HTML che ha generalmente questa forma:
    # <a href='URL'>link text</a>
    repo_links.append(repo_link)
    # Sull'asse x avrò i nomi dei progetti ma in forma ipertestuale con collegamento
    # alla relativa pagina online

    stars.append(repo_dict['stargazers_count'])

    # Ora creo degli hover texts per il grafico interattivo
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    # Plotly permettere di usare codice HTML negli elementi di testo, facendoci
    # generare una stringa con un line break "<br />" tra il username e descrizione
    hover_texts.append(hover_text)

# Creo poi un grafico con plotly in cui per ogni repo mostro il numero di stelle ricevute
title="Le repo github con più stars"
labels={"x":"Nome del progetto","y":"Stelle assegnate"}

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts, height=600)
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
# Cambiamo ora il colore di default e trasparenza del grafico
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
# In Plotly, una trace si riferisce a una collezione di dati su di un grafico

fig.show()