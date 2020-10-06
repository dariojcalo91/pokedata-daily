import requests
import random

# api-endpoint 
URL = " https://pokeapi.co/api/v2/pokemon/"

# random id of pokemon
pokemon_id = str(random.randrange(100))

# sending get request and saving the response as response object 
r = requests.get(url = URL+pokemon_id) 
 
# extracting data in json format 
data = r.json() 

print("data", data['types'])

# extracting pokemon data
name = data['name']
pokemon_first_type = data['types'][0]['type']['name']
pokemon_second_type = data['types'][1]['type']['name']

# printing the output 
print("Pokemon data:")
print("name:%s\nType1:%s\nType2:%s"
      %(name, pokemon_first_type, pokemon_second_type)) 

def pokemon_data():
  return name, pokemon_first_type, pokemon_second_type
