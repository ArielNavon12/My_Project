#Part 1
A=8
B=10

if A==B:
    print(0)
elif A>B:
    print(A-B)
elif B>A:
    print (B-A)
    
#Part 2
Html_file=open('C:/Users/Ariel/Documents/תואר שני/פסיכולוגיה/שנה א/סימסטר א/תכנות ואיסוף בפייתון/מטלה 9/quotes.html', encoding="utf8") 
Html_text=Html_file.read()   

from bs4 import BeautifulSoup        
Soup=BeautifulSoup(Html_text, "html.parser")
Names=Soup.find_all("small", {"class": "author", "itemprop":"author"})
#OnlyName=list(range(0,10))

for i in range(len(Names)):
    OnlyName=Names[i].get_text()
    #print(OnlyName)
    OnlyName=OnlyName.replace(".", " ")
    OnlyNameSplitted=OnlyName.split(" ")
    if len(OnlyNameSplitted) >= 3:
        print(OnlyName)
    
    
#ThreePartNames=str(OnlyName)
#ThreePartNames=ThreePartNames.split(",")
#ThreePartNamesSplitted=list(range(0,10))
#ThreePartNamesSplittedOnly=list(range(0,10))

#for i in range(len(ThreePartNames)):
    
    
    
for i in range(len(ThreePartNamesSplittedOnly)):
  
    


#Shorter Alternative:
Names=open('C:/Users/Ariel/Documents/תואר שני/פסיכולוגיה/שנה א/סימסטר א/תכנות ואיסוף בפייתון/מטלה 9/quotes.html', encoding="utf8") 
Names=Names.read()   
from bs4 import BeautifulSoup        
Names=BeautifulSoup(Names, "html.parser")
Names=Names.find_all("small", {"class": "author", "itemprop":"author"})
for author in Names:
    name=author.get_text()
    words_num=len(name.split(" "))
    dot_num=len(name.split('.'))
    if (words_num==3) or (dot_num==3):
        
        print(author.get_text())

