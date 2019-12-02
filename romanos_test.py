import unittest
from romanos import romano_a_arabigo, arabigo_a_romano

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romano_a_arabigo('I'), 1)
        self.assertEqual(romano_a_arabigo('V'), 5)
        self.assertEqual(romano_a_arabigo('X'), 10)
        self.assertEqual(romano_a_arabigo('L'), 50)
        self.assertEqual(romano_a_arabigo('C'), 100)
        self.assertEqual(romano_a_arabigo('D'), 500)
        self.assertEqual(romano_a_arabigo('M'), 1000)
        self.assertEqual(romano_a_arabigo('A'), 0)

    def test_numeros_crecientes(self):
        self.assertEqual(romano_a_arabigo('XVI'), 16)
        self.assertEqual(romano_a_arabigo('III'), 3)

    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(romano_a_arabigo('LXXIII'), 73)
        self.assertEqual(romano_a_arabigo('IIII'), 0)
        self.assertEqual(romano_a_arabigo('VV'), 0)

    def test_numeros_decrecientes(self):
        self.assertEqual(romano_a_arabigo('CMXCIX'), 999)
        self.assertEqual(romano_a_arabigo('MMCMLXIX'), 2969)
        self.assertEqual(romano_a_arabigo('MCDXCII'), 1492)
    
    def test_restas_no_admiten_repeticiones(self):
        self.assertEqual(romano_a_arabigo('MIIX'), 0)
        self.assertEqual(romano_a_arabigo('IIX'), 0)

    def test_restas_no_admiten_derivados_del_5(self):
        self.assertEqual(romano_a_arabigo('MVL'), 0)
        self.assertEqual(romano_a_arabigo('VL'), 0)
        self.assertEqual(romano_a_arabigo('VC'), 0)

    def test_restas_no_admiten_mas_de_un_orden_de_diferencia(self):
        self.assertEqual(romano_a_arabigo('IL'), 0)
        self.assertEqual(romano_a_arabigo('IC'), 0)
  
    def test_numeros_mayores_de_3999(self):
        self.assertEqual(romano_a_arabigo('(IV)'), 4000)
        self.assertEqual(romano_a_arabigo('(III)I'), 3001)
        self.assertEqual(romano_a_arabigo('((IV))'), 4000000)
        self.assertEqual(romano_a_arabigo('(VII)CMXXIII'), 7923)
        self.assertEqual(romano_a_arabigo('(((VII)))(DLIII)DCXXXVII'), 7000553637)


class ArabicNumberTest(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(arabigo_a_romano(1), 'I')
        self.assertEqual(arabigo_a_romano(2), 'II')
        self.assertEqual(arabigo_a_romano(3), 'III')
        self.assertEqual(arabigo_a_romano(4), 'IV')
        self.assertEqual(arabigo_a_romano(5), 'V')
        self.assertEqual(arabigo_a_romano(6), 'VI')
        self.assertEqual(arabigo_a_romano(7), 'VII')
        self.assertEqual(arabigo_a_romano(8), 'VIII')
        self.assertEqual(arabigo_a_romano(9), 'IX')

    def test_arabic_a_roman(self):
        self.assertEqual(arabigo_a_romano(2123), 'MMCXXIII')
        self.assertEqual(arabigo_a_romano(2444), 'MMCDXLIV')
        self.assertEqual(arabigo_a_romano(3555), 'MMMDLV')
        self.assertEqual(arabigo_a_romano(3000), 'MMM')
        self.assertEqual(arabigo_a_romano(1678), 'MDCLXXVIII')
        self.assertEqual(arabigo_a_romano(2999), 'MMCMXCIX')
        self.assertEqual(arabigo_a_romano(3999), 'MMMCMXCIX')
        self.assertEqual(arabigo_a_romano(4000), 0)
        self.assertEqual(arabigo_a_romano(-1), 0)


if __name__ == '__main__':
    unittest.main()