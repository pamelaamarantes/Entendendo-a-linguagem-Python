from carro import Carro
from Veiculo.moto import Moto

def main():
    # Instanciando objetos
    carro1 = Carro('Toyota', 'Corolla', 4)
    carro2 = Carro('Honda', 'Civic', 2)
    carro3 = Carro('Hyundai', 'Creta', 4) 
    
    moto1 = Moto('Harley-Davidson', 'Sportster', 'Esportiva')
    moto2 = Moto('Honda', 'CB 500', 'Casual')
    
    # Alterando o estado dos veículos para "ligado"
    carro1._ligado = True
    moto2._ligado = True
    
    # Exibindo informações
    print("Resultados para os carros:")
    print(carro1)
    print(carro2)
    print(carro3)
    
    print("\nResultados para as motos:")
    print(moto1)
    print(moto2)

if __name__ == '__main__':
    main()
