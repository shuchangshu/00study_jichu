from unittest import TestCase
from test01 import calcul

class Testcalcul (TestCase):
    def test_add(self):
        Calcul=calcul()
        self.assertEqual(Calcul.add(3,4),7)
        # self.fail ()
