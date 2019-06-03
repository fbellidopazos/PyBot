import  requests

from bs4 import BeautifulSoup
word = str(input("Word to lookup: "))
r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))

soup = BeautifulSoup(r.content, "html.parser")

print(soup.find("div",attrs={"class":"meaning"}).text)
