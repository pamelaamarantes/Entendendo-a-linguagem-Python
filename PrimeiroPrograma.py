#!/usr/bin/env python
# coding: utf-8

# Primeiro programa

# In[26]:


#Script para cadastramento de restaurantes, as categorias e o status
import os

#listas
restaurantes = [{'nome': 'PizzaBar','categoria':'italiana','Ativo':False},
               {'nome': 'SushiBar','categoria':'japonesa','Ativo':True},
               {'nome': 'ChurrascoBar', 'categoria':'Sulista', 'Ativo':False}]

#exibir o nome do programa
def exibir_nome_programa():
    print('\n    ## Sabor Express ##      \n')

#exibir as opções de cadastramentos
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listrar restaurante')
    print('3. Alterar o status do restaurante')
    print('4. Sair\n')
    
#limpar e finalizar
def finalizar_app():
    print('Finalizando o app')
    
#corrigir repetição
def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal \n')
    main()
    
#limpeza para opções invalidas  
def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_menu_principal()
   
    #cadastramentos   
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes \n')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    restaurantes.append(nome_restaurante)
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}:\n')
    dados_restaurante = {'nome': nome_restaurante, 
                         'categoria':categoria ,
                         'Ativo':False}
    restaurantes.append(dados_restaurantes)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_menu_principal()
    
   
    #listar restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listar novos restaurantes \n')
    print(f"{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante ['Ativo'] else 'Desativado'
        print(f"-{nome_restaurante.ljust(22)}  |{categoria.ljust(20)} | {ativo}")   
        
    voltar_menu_principal()
    
#escolher opções    
def escolher_opcoes():   
    try:
        opcao_escolhida = int(input('Escolha uma opção:\n'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()        
        
        
#todas as funçoes     
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()

