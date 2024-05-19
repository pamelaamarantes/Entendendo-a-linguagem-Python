#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Buscar cotacao de moedas


import requests
import json


# In[9]:


url = 'https://economia.awesomeapi.com.br/json/all'

response = requests.get(url)
cotacoes_dic = cotacao.json()
print(cotacoes_dic) #aqui ele ira executar todas as informações de moedas sobre api


# Qual foi a ultima cotação do dólar, Euro, Bitcoin?

# In[14]:


print('Dolar: {}'.format(cotacoes_dic['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic['EUR']['bid']))
print('Bitcoin: {}'.format(cotacoes_dic['']['bid']))


# Pegar as cotacoes dos ultimos 30 dias do dólar 

# In[24]:


cotacao_30dias = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_30dias_dic = cotacao_30dias.json()
#print(cotacoes_30dias_dic[2]['bid'])
lista_cotacoes30dias = [item['bid'] for item in cotacoes_30dias_dic]
print(lista_cotacoes30dias)


# Pegar as cotações do bitcoin de Jan/24 a Abr/24

# In[48]:


cotacao_4meses = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20240101&end_date=20240430')
cotacoes_4meses_dic = cotacao_4meses.json()
lista_cotacoes_4meses = [float(item['bid']) for item in cotacoes_4meses_dic]
print(lista_cotacoes_4meses)
print(len(lista_cotacoes_4meses))


# Exibir em grafico cotação de Bitcoin

# In[54]:


import matplotlib.pyplot as plt


plt.figure(figsize=(20, 10))
plt.plot(lista_cotacoes_4meses)
plt.show()

