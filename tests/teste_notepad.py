from main import actions
from pytest import mark


class testes:

    @mark.Abrir
    def test_abrir_notepad():
        caminho = 'C:\\Windows\\System32\\notepad.exe'
        titulo = 'Untitled - Notepad'
        actions.startApp(caminho, titulo)

    # @mark.Inserir
    # def test_inserir_texto():
    #     texto = "Opa Teste automático!"
    #     actions.insertText(texto)
