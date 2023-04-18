from unittest import TestCase

from app.conversao import converte


class TestConverte(TestCase):
    def test_converte_deve_retornar_0_quando_receber_32(self):
        assert converte(32) == 0

    def test_converte_deve_retornar_40_quando_receber_40(self):
        assert converte(-40) == -40

    def test_converte_deve_retornar_17_77_quando_receber_0(self):
        self.assertAlmostEqual(converte(0), -17.77, places=1)
