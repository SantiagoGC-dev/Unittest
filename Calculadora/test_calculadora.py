#importación de UnitTest para realizar pruebas unitarias
import unittest

#importación de la clase Calculadora desde el archivo calculadora
from calculadora import Calculadora

#definición de la clase TestCalculadora que hereda de unittest.TestCase
class TestCalculadora(unittest.TestCase):

    #método antes de ejecutar cada prueba
    def setUp(self):
        #instanciar la clase Calculadora
        self.calc = Calculadora()

    #método para probar la suma de 2 números    
    def test_suma(self):
        #prueba de la suma de 2 números positivos
        self.assertEqual(self.calc.suma(2, 3), 5)
        #prueba de la suma de 1 número negativo y 1 positivo
        self.assertEqual(self.calc.suma(-1, 1), 0)
        #prueba de la suma de 2 ceros
        self.assertEqual(self.calc.suma(0, 0), 0)

    #método para probar la resta de 2 números
    def test_resta(self):
        #prueba de la resta de 2 números positivos
        self.assertEqual(self.calc.resta(2, 3), -1)
        #prueba de resta de 2 números iguales 
        self.assertEqual(self.calc.resta(2, 2), 0)
        #prueba de resta de 2 números negativos
        self.assertEqual(self.calc.resta(-2, -2), 0)

    #método para probar la multiplicación de 2 números
    def test_multiplicacion(self):
        #prueba de la multiplicación de un número positivo por cero (debe dar 0)
        self.assertEqual(self.calc.multiplicacion(1, 0), 0)
        #prueba de la multiplicación de 2 números positivos
        self.assertEqual(self.calc.multiplicacion(5, 5), 25)
        #prueba de la multiplicación de 1 número negativo por 1 positivo
        self.assertEqual(self.calc.multiplicacion(-1, 1), -1)


    #método para probar la división de 2 números
    def test_division(self):
        #prueba de la división de 2 números positivos
        self.assertEqual(self.calc.division(4, 2), 2)
        #prueba de la división entre 1 (debe dar el mismo número)
        self.assertEqual(self.calc.division(5, 1), 5)
        #prueba de la división por un número negativo
        self.assertEqual(self.calc.division(6, -2), -3)
        #prueba de la división de 2 números negativos
        self.assertEqual(self.calc.division(-6, -2), 3)
        #Prueba la división con resultado decimal
        self.assertEqual(self.calc.division(11, 6), 1.8333333333333333)
        #Prueba con división periodica usando assertAlmostEqual para comparar la precisión limitada
        self.assertAlmostEqual(self.calc.division(40, 9), 4.444444444444445 , places=15)
        #Prueba especifica para verificar el manejo de la división por cero
        with self.assertRaises(ValueError):
            self.calc.division(5, 0)



#bloque condicional para ejecutar las pruebas
if __name__ == '__main__':
    #inicio de las pruebas
    unittest.main()


#Trabajo de David Santiago Gutiérrez Calderón