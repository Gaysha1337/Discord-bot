import requests, asyncio
from bs4 import BeautifulSoup

url = "https://www.merriam-webster.com/word-of-the-day"
def makeRequest(url):
    r = requests.get(url)
    if r.status_code == 200:
        print("connection successful")
        #print(r.content)
    else:
        print("OOPSIE WOOPSIE!! \nUwu We made a fucky wucky!! \nA wittle fucko boingo! \nThe code monkeys at our headquarters are working VEWY HAWD to fix this!")
    data = r.content
    return data

soup = BeautifulSoup(makeRequest(url),"html.parser")
def GetWordOfThedayHtml(soup=soup):
    word_of_the_day_div = soup.findAll("div", {"class": "word-and-pronunciation"})
    for div in word_of_the_day_div:
        for h1 in div.findAll("h1"):
            word = h1.text
            #print(word)
            return word        
def GetWordAtttributes(word):
    allAttributes = {}
    attribute_div = soup.find_all("div", {"class":"word-attributes"})
    for div in attribute_div:
        for span in div.find_all("span",{"class":"main-attr"}):
            data = span.text
            allAttributes["grammatical class"] = data
            #print(data)   
        for span in div.find_all("span",{"class":"word-syllables"}):
            data = span.text
            allAttributes["syllables"] = data
    return allAttributes
            
def GetWordDefinition(word):
    word_def_container = soup.find("div",{"class":"wod-definition-container"})
    definitions = [div.text for div in word_def_container.find_all("p",recursive=False)]
    #print(definitions)
    return definitions
            
def getTodayDate(word):
    div_with_date = soup.find_all("div",{"class":"article-header-container wod-article-header"},limit=
    1)
    for div in div_with_date:
        for span in div.find_all("span",{"class":"w-a-title margin-lr-0 margin-tb-1875em"}):
            date = span.text.strip()
            return date
def makeDisplay(word, definitions, word_attributes,date):
    print("----------------------------------------------------------------------------------------")
    print(date)
    print(word)
    print("definitions: ")
    for definition in definitions:
        print(definition)
    for k,v in word_attributes.items():
        print(k + ":",v )

    print(str(word_attributes))
    print("----------------------------------------------------------------------------------------")

def discord_wod(word=GetWordOfThedayHtml(soup), definitions=GetWordDefinition(soup), word_attributes=GetWordAtttributes(soup),date=getTodayDate(soup)): 
    return word, definitions, word_attributes, date    

#getToday(soup)
#makeRequest(url)
#GetWordOfThedayHtml(soup)
#print(GetWordAtttributes(soup)) # returns a dict with all atttributes as values
#print(GetWordDefinition(soup))

if __name__ == "__main__":
    #print(discord_wod())
    makeDisplay(GetWordOfThedayHtml(soup),GetWordDefinition(soup),GetWordAtttributes(soup),getTodayDate(soup))
    #input("press any key to exit")
    x = 2