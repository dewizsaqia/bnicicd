import requests

print ("hello word")
print ("testing cicd bni")

response = requests.get("https://www.google.com")

print (response.text)
