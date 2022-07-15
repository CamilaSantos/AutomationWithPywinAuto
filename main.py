from storageCode.constructor import selectApp
from pywinauto.application import Application
import string
import random


class actions:

    # inicia o aplicativo
    def startApp(self, a, b):
        global paramApp
        self.a = a
        self.b = b
        # Variável responsável por dosponibilizar as ações do Application
        paramApp = Application(backend='uia').start(
            f'{a}').window(title_re=f'{b}')
        paramApp.wait('ready', timeout=10)

    # Imprimindo no terminal a arvore de estrutora do aplicativo.

    def structureApp(self):
        app = paramApp
        app.print_control_identifiers()

    # Incluir texto dentro do aplicativo

    def insertText(self, texto):
        self.text = texto
        textEditor = paramApp.child_window(
            title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
        textEditor.type_keys(f'{self.texto}', with_spaces=True)
        return texto
        
        

    # Alterando Fonte

    def alterFont(self, nameF, sizeF, styleF):
        self.nameF = nameF
        self.sizeF = sizeF
        self.styleF = styleF

        # menuBar = paramApp.child_window(title="Application", auto_id="MenuBar", control_type="MenuBar").wrapper_object()
        # menuBar.click_input()

        # Abrir menu Format
        menuFormat = paramApp.child_window(
            title="Format", control_type="MenuItem").wrapper_object()
        menuFormat.click_input()

        # Selecionando o input para digitar a fonte desejada
        inputFont = paramApp.child_window(
            auto_id="33", control_type="MenuItem").wrapper_object()
        inputFont.click_input()

        # Insere o nome da fonte no campo
        nameFont = paramApp.child_window(
            title="Font:", auto_id="1001", control_type="Edit").wrapper_object()
        nameFont.type_keys(nameF, with_spaces=True)

        # Campo para informar o Style
        styleFont = paramApp.child_window(
            title="Font style:", auto_id="1001", control_type="Edit").wrapper_object()
        styleFont.type_keys(styleF, with_spaces=True)

        # Digitar Style
        sizeFont = paramApp.child_window(
            title="Size:", auto_id="1090", control_type="Text").wrapper_object()
        sizeFont.type_keys(sizeF, with_spaces=True)

        # Clicar botão OK
        okButtonFont = paramApp.child_window(
            title="OK", auto_id="1", control_type="Button").wrapper_object()
        okButtonFont.click_input()

     # Salvar arquivo .txt

    def saveFile(self):

       #Randomizando letras e números para salvar novo documento até 3 caracteres
        S = 3
        ran = ''.join(random.choices(string.ascii_letters + string.digits, k=S))

        #Acessando menu File e selecionando Save As... para salvar o aqruivo
        menuFile = paramApp.child_window(
            title="File", control_type="MenuItem").wrapper_object()
        menuFile.click_input()

        menuFileSaveAs = paramApp.child_window(
            auto_id="4", control_type="MenuItem")
        menuFileSaveAs.click_input()
        #Apenas retornando a pasta raiz (This PC)
        barraThisPC = paramApp.child_window(
            title="This PC", control_type="SplitButton").wrapper_object()
        barraThisPC.click_input()
        #Selecionando pasta Desktop
        barraDesktop = paramApp.child_window(
            title="Desktop", auto_id="1", control_type="ListItem").wrapper_object()
        barraDesktop.double_click_input()

        #Abrindo pasta TESTE AUT para salvar o arquivo dentro
        selectFolder = paramApp.child_window(
            title="TESTE AUT", auto_id="4", control_type="ListItem").wrapper_object()
        selectFolder.double_click_input()

        #Informando o nome do arquivo que será salvo, juntamente com as letras e números
        #randomizados
        nameDocSave = paramApp.child_window(
            title="File name:", auto_id="1001", control_type="Edit").wrapper_object()
        nameDocSave.type_keys("Doc_ "+str(ran)+".txt")

        #Clicando em salvar
        saveButton = paramApp.child_window(
            title="Save", auto_id="1", control_type="Button").wrapper_object()
        saveButton.click_input()


#==================================================#
cls = actions()  # <- Classe

# """
#     Com a condição abaixo, informamos a função inicial
#     e disponibilizamos para as demais funções a variável
#     global ''paramApp''
# """
if __name__ == "__main__":
    cls.startApp(string, string)

# cls.alterFont("Verdana", "20", "Regular")

# cls.insertText()# <- Função para incluir o texto no Notepad
