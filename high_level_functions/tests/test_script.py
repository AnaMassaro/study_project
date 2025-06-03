import unittest
import functools
from src.script import (
    aplicar_desconto,
    aplicar_10_porcento,
    processar_produtos,
)

class TestProdutos(unittest.TestCase):
    def setUp(self):
        # produtos formatados e caros (ordenados por preço)
        self.produtos = [
            ("mouse", 120),
            ("celular", 1500),
            ("notebook", 3500),
        ]

    def test_aplicar_desconto(self):
        resultado = aplicar_desconto(("notebook", 2000), 10)
        self.assertEqual(resultado, ("notebook", 1800.00))

    def test_aplicar_10_porcento_partial(self):
        resultado = aplicar_10_porcento(("celular", 1000))
        self.assertEqual(resultado, ("celular", 900.00))

    def test_processar_produtos_aplica_desconto(self):
        resultado = processar_produtos(self.produtos)
        esperado = [
            ("mouse", 108.0),
            ("celular", 1350.0),
            ("notebook", 3150.0),
        ]
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
