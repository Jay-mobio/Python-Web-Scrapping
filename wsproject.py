from bs4 import BeautifulSoup
import requests

url = "https://oxylabs.io/"

form_data = {"key":'value1',"key2":'value2'}


response = requests.get(url,data = form_data)
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup)

