"""
    Neste arquivo será utilizado o Pytest para a execução dos testes
    Exibir status de testes (Pass, 'Warning' e Error)
    Será realizada a chamada das funções (ações) do arquivo main.py
    Para ser mais dinâmico, aqui seram informados os valores das variáveis esperadas da função    
"""
import os
import sys
# print(sys.path)
from src.main import Actions
from pytest import mark
import pytest



class Testes:
        
    #@pytest.mark.Abrir
    def teste_abrir_notepad(self):
        self.caminho = 'C://Windows//System32//notepad.exe'
        self.titulo = '.* - Notepad$'
        Actions.startApp(Actions,self.caminho, self.titulo)


    #@pytest.mark.Inserir
    def teste_inserir_texto(self):
        self.texto = "Vamos!!!"
        Actions.insertText(Actions,self.texto)
        
        
    def teste_alterarFonte(self):
        self.nomeFonte = "Arial"
        self.tamanhoFonte = "18"
        self.estiloFonte = "Bold Italic"        
        Actions.alterFont(Actions,self.nomeFonte, self.tamanhoFonte, self.estiloFonte)
        
        
    def teste_salvar_doc(self):
        Actions.saveFile(self)