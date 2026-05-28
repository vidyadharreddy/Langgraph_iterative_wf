import json
topic="gen ai"
input=f"""{{ "iteration" : 1, "topic":"gen ai" , "max_iteration" : 5 }}"""

data = json.loads(input)
print(data)

