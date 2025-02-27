import requests
from operator import itemgetter
import plotly.express as px

url="https://hacker-news.firebaseio.com/v0/"
url+="topstories.json"

r=requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids=r.json()
submission_dicts,x_axis,y_axis,hovers=[],[],[],[]
max_chars=15  # Dato che inserirò i titoli sull'asse delle x, potrei aver bisogno di accorciarli.
# Decido un limite massimo di 15 caratteri e creo un if else che controlli il numero di caratteri
# originali del titolo

for submission_id in submission_ids[:30]:
    try:
        url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r=requests.get(url)
        response_dict = r.json()
        link=f"https://news.ycombinator.com/item?id={submission_id}"
        title=response_dict["title"]
        hover_text=f"<a href='{link}'>"
        hover_text+=response_dict["title"][:max_chars] + "..." if len(response_dict["title"]) > max_chars else response_dict["title"]
        hover_text+="</a>"
        submission_dict={
            "title":title,
            "comments":response_dict["descendants"],
            "linked_text":hover_text,
        }
        submission_dicts.append(submission_dict)
    except KeyError: # Ho bisogno di un try except perché tra le notizie ci sono degli ad senza commenti che danno errore
        pass

submission_dicts=sorted(submission_dicts,key=itemgetter("comments"),
                        reverse=True)

for submissions in submission_dicts:
    x_axis.append(submissions["linked_text"])
    y_axis.append(submissions["comments"])
    hovers.append(submissions["title"])

labels={"x": "Nomi degli articoli", "y":"Numero di commenti"}

fig=px.bar(x=x_axis,y=y_axis,labels=labels, hover_name=hovers)
fig.update_xaxes(tickangle=45)
fig.update_traces(marker_color="Red", marker_opacity=0.6)
fig.show()