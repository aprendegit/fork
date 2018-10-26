from urllib.request import urlopen as uReq  
from bs4 import BeautifulSoup as soup 
import json

my_url = input('URL:')
my_url = my_url.replace(' ','')
filename = input('File name:')
filename = filename.replace(' ','_')



#abrindo conexão com a página 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,'html.parser')
containers = page_soup.findAll('div',{'class':'item__info'})



placas =[]




filename = filename + '.json'
file = open(filename,'w')
for container in containers :

    placa = {}
    nome_placa = container.h2.span.text

    preco_container = container.findAll('span',{'class':'price-fraction'})
    preco = preco_container[0].text
    preco = 'R$ '+preco.strip()

    placa['Nome'] = nome_placa
    placa['Preco'] = preco
    placas.append(placa)

placas_string = json.dumps(placas,ensure_ascii=False,sort_keys=True,indent=4 )
file.write(placas_string+'\n')

file.close()
