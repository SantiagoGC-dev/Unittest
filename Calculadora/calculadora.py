#definincion de la clase calculadora que proporciona operaciones matematicas basicas
class Calculadora:
    #metodo para sumar 2 numeros

    def suma (self, a , b):
        return a+b
     
    #metodo para restar 2 numeros
    def resta (self, a, b):
        return a-b
    
    #metodo para multiplicar 2 numeros
    def multiplicacion (self, a, b):
        return a*b
    
    #metodo para dividir 2 numeros, incluye validacion para no dividir por 0
    def division (self, a, b):
        if b == 0:
            raise ValueError ("No se puede dividir por 0")
        return a/b
    
