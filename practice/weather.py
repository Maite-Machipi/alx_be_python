import requests

#replace with own API key
API_KEY = "fd73dfb92016438786684807252011"
CITY = "Polokwane"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

#make a get request
response = requests.get(url)

#convert response to JSON format
data = response.json()

#extract useful information
location = data["location"]["name"]
temperature = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]

#print weather information
print(f"Weather in {location}:")
print(f"Temperature: {temperature}°C")
print(f"Condition: {condition}")
