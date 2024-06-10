from unittest import TestCase
from telefone import Telefone, TelefoneInvalidoException


class TelefoneTestCase(TestCase):

    def test_telefone_movel_com_codigo_pais(self):
        telefone = Telefone(numero='5511997799298', codigo_area='11', codigo_pais='55')
        self.assertEqual('5511997799298', telefone.numero)

    def test_telefone_movel_sem_codigo_pais(self):
        telefone = Telefone(numero='11997799298', codigo_area='11', codigo_pais='55')
        self.assertEqual('5511997799298', telefone.numero)

    def test_telefone_movel_sem_codigo_pais_e_sem_codigo_de_area(self):
        telefone = Telefone(numero='997799298', codigo_area='11', codigo_pais='55')
        self.assertEqual('5511997799298', telefone.numero)
    
    def test_telefone_fixo_com_codigo_pais(self):
        telefone = Telefone(numero='551137092380', codigo_area='11', codigo_pais='55')
        self.assertEqual('551137092380', telefone.numero)

    def test_telefone_fixo_sem_codigo_pais(self):
        telefone = Telefone(numero='1137092380', codigo_area='11', codigo_pais='55')
        self.assertEqual('551137092380', telefone.numero)

    def test_telefone_fixo_sem_codigo_pais_e_sem_codigo_de_area(self):
        telefone = Telefone(numero='37092380', codigo_area='11', codigo_pais='55')
        self.assertEqual('551137092380', telefone.numero)
    
    def test_telefone_remover_caracteres_especiais(self):
        telefone = Telefone(
            numero='+551137092380', 
            codigo_area='11', 
            codigo_pais='55', 
            remover_caracteres_especiais=True
        )
        self.assertEqual('551137092380', telefone.numero)
    
    def test_telefone_semf_remover_caracteres_especiais(self):
        telefone = Telefone(
            numero='+551137092380', 
            codigo_area='11', 
            codigo_pais='55', 
            remover_caracteres_especiais=False
        )
        self.assertEqual('+551137092380', telefone.numero)
    
    def test_telefone_eh_movel(self):
        telefone = Telefone(
            numero='551199779298', 
            codigo_area='11', 
            codigo_pais='55'
        )
        self.assertTrue(telefone.eh_movel)
    
    def test_telefone_nao_eh_movel(self):
        telefone = Telefone(numero='551137092380', codigo_area='11', codigo_pais='55')
        self.assertFalse(telefone.eh_movel)

    def test_telefone_invalido(self):
        self.assertRaises(TelefoneInvalidoException, Telefone, '2380', '11', '55')