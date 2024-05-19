#!/usr/bin/env python
# coding: utf-8

# Primeira atividade

# In[27]:


print('Python na Escola de Programação da Alura')


# In[28]:


nome = 'Pamela'
idade = 31
print(f'Meu nome é {nome} e tenho {idade} anos')


# In[29]:


print('A','L','U','R','A',sep='\n')


# In[30]:


pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')


# Segunda atividade

# In[33]:


usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")


# In[34]:


#Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

def verifique_idade():
    qual_idade = int(input('Quantos anos você tem? \n'))
    if 0 <= qual_idade <= 12:
        print(f'É uma criança com a idade {qual_idade} anos!')
    elif 13 <= qual_idade <= 18:
        print(f'É um adolescente com a idade {qual_idade} anos!')
    else:
        print(f'É um adulto de {qual_idade} de anos!')
        
verifique_idade()


# In[35]:


def determinar_quadrante(x, y):
    if x > 0 and y > 0:
        print("O ponto está no Primeiro Quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no Segundo Quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no Terceiro Quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no Quarto Quadrante.")
    else:
        print("O ponto está no eixo ou na origem.")

# Solicita ao usuário as coordenadas do ponto
try:
    x = float(input("Digite a coordenada x do ponto: "))
    y = float(input("Digite a coordenada y do ponto: "))
    
    # Chama a função para determinar o quadrante
    determinar_quadrante(x, y)
except ValueError:
    print("Por favor, insira valores numéricos válidos para as coordenadas.")


# In[36]:


#Para percorrer todos os itens de uma lista com o loop for, você pode usar essa estrutura:
at_numeros = [1,2,3,4,5,6,7,8,9,10]
at_nomes = ['Pamela','Afonso','Rose','Aline']
at_ano =[1993,2024]

for numero in at_numeros:
        print(numero)



# In[37]:


#Para fazer calcular a soma dos números impares de 1 a 10, você pode utilizar o seguinte código:
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)


# In[38]:


#Para imprimir os números de 1 a 10 de forma decrescente, você pode utilizar a seguinte estrutura:
for i in range(10, 0, -1):
    print(i)


# In[39]:


#Para fazer uma tabuada interativa, você pode seguir o seguinte código: 
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")


# In[40]:


#Uma possível resolução para fazer a soma dos elementos de uma lista com for e usar try except para validar, está no código a seguir:
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


# In[41]:


#Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
Dic_Ex = {'nome': 'Pamela', 'idade': 31, 'cidade': 'Praia grande'}


# Atualizar a idade
Dic_Ex['idade'] = 20

# Adicionar uma nova informação (profissão)
Dic_Ex['empresa'] = 'Nttdata'

# Remover a cidade
Dic_Ex.pop('cidade')

print(Dic_Ex)


# In[42]:


#Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


# In[43]:


#- Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura
Dic_Ex = {'nome': 'Pamela', 'idade': 20, 'cidade': 'Praia Grande'}
if 'idade' in Dic_Ex:
    print("A chave 'idade' existe no dicionário.")
else:
    print("A chave 'idade' não existe no dicionário.")

Dic_Ex['idade']


# In[24]:


#Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
frase = "Ele não queria acreditar. Nunca quis, na verdade. Mas, dessa vez, ele precisou."
C_palavras = {}
palavras = frase.split()
for palavra in palavras:
    C_palavras[palavra] = C_palavras.get(palavra, 0) + 1
print(C_palavras)


# In[ ]:




