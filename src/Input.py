class Input:   
    @classmethod
    def validar_input(cls):
        input_numeros = input('Digite os 4 números: ')
        array_numeros = list(input_numeros)
        return array_numeros