
import requests
page = requests.get('https://www.google.com')
print(page.text[0:100])


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
get_cont = soup.find('title').text
print(get_cont)

