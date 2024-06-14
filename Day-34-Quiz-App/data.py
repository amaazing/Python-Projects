import requests

parameters = {"amount": 10,
              "type": "boolean"}
data = requests.get("https://opentdb.com/api.php", params= parameters)
data.raise_for_status()
questions_unparsed = data.json()
question_data = questions_unparsed["results"]