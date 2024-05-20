#!/usr/bin/env python
# coding: utf-8

# EXERCICIO API - CEP 

# In[2]:


import requests
import json


# Consulta de informações de um CEP

# In[6]:


#conferindo o retorno

#url = 'https://viacep.com.br/ws/11702240/json/'
#response = requests.get(url)
#print(response)


# In[12]:


class CEP:
    def __init__(self, cep):
        self.cep = self._format_cep(cep)
        self.dados = None

    def _format_cep(self, cep):
#Remove caracteres indesejados do CEP.
        return cep.replace("-", "").replace(".", "").replace(" ", "")

    def validar(self):
#Verifica se o CEP tem 8 dígitos."""
        return len(self.cep) == 8

    def consultar(self):
#Consulta o CEP usando a API ViaCEP e armazena os dados
        if self.validar():
            url = f'https://viacep.com.br/ws/{self.cep}/json/'
            requisicao = requests.get(url)
            if requisicao.status_code == 200:
                self.dados = requisicao.json()
            else:
                print("Erro na requisição:", requisicao.status_code)
        else:
            print("CEP Inválido")


# In[29]:


def exibir_dados(self):
#Exibe os dados do CEP, se disponíveis
    if self.dados:
        uf = self.dados.get('uf', 'Não disponível')
        cidade = self.dados.get('localidade', 'Não disponível')
        bairro = self.dados.get('bairro', 'Não disponível')
        print(f"UF: {uf}")
        print(f"Cidade: {cidade}")
        print(f"Bairro: {bairro}")
        print(self.dados)
    else:
        print("Dados não disponíveis. Certifique-se de ter consultado o CEP corretamente.")


cep = CEP("11.702-240")
cep.consultar()
cep.exibir_dados()

