class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False 
    
    def __str__(self):
        ligado_str = 'ligado' if self._ligado else 'desligado'
        return f'{self._marca} {self._modelo} - Estado: {ligado_str}'




