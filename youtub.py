import os
from pytube import YouTube
from bs4 import BeautifulSoup
import lxml
from transliterate import translit

url=input() #url of youtbe video
folder='pop'#variable for name of folder
yt=YouTube(url)
name=yt.title#title of video
c=yt.captions

try:
    language=str(yt.captions).split("'")[1]#get name laguage of video
except:
    language='en'

if (language)=='a.en' or (language)=='en':
    name=name.replace(' ','_')
    name=name[0:10]

if (language)=='a.ru' or (language)=='ru':
    name=translit(name,language_code='ru', reversed=True).replace(' ','_')
    name=name[0:10]

if (language)[0:2]=='a.de' or (language)[0:2]=='de':
    name=name[0:10]
    li=['ä','ö', 'ü', 'ß', '?',' ']#list fo replace
    li2=['ae', 'oe', 'ue', 'ss','', '_']#replaced
    language='a.de'
    for r in li:
        name=name.replace(r,li2[li.index(r)])
        name=name[0:10]

if not os.path.exists(f'{folder}'): #prove existence of folder and crete
    os.mkdir(f'{folder}')

xml=c.get_by_language_code(language).xml_captions#get xml from requests
soup = BeautifulSoup(xml, 'lxml').get_text()#get only text
soup=soup.replace('\n\n','')#make more pretty text

li = ['ä', 'ö', 'ü', 'ß']  # list fo replace
li2 = ['ae', 'oe', 'ue', 'ss']  # replaced

for r in li:
    soup = soup.replace(r, li2[li.index(r)])
with open(f'./pop/{name}.txt','w') as f:
    f.write(soup)