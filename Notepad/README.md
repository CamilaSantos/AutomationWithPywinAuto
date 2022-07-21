# AutomationWithPywinAuto


Automatização de Teste na prática utilizando Python, Pywinauto e Pytest.


O objetivo deste projeto é automatizar testes de aplicações desktop, esta foi uma alternativa encontrada no momento em que me deparei com um ambiente onde o sistema a ser testado é um sistema legado e o ambiente de teste não pode sefrer muitas alterações.

Configuração para utilizar Python, Pywinauto e Pytest:

* Instalar versão python na máquina (Versão atual deste projeto *Python 3.10.4*)
* No VS Code configurar as extensões Python
* Instalar Pytest 
(https://blog.finxter.com/how-to-install-pytest-in-python/#:~:text=Your%20Python%20Skills-,How%20to%20Install%20pytest%20on%20Windows%3F,for%20your%20default%20Python%20installation.)

Estou treinando Python, então optei em trabalhar com classes e tornar mais dinâmica a utilização do projeto.

Para ter uma visão simples de como funciona o Pywinauto, sugiro o vídeo abaixo:

https://www.youtube.com/watch?v=_-H1GgIhjhA



## *Executando teste com pytest *

Através do terminal, no diretório 'test' dentro deste projeto, executar o comando:

*** python -m pytest -v teste_notepad.py ***

O comando *python -m* é para evitar o erro de módulo ao importar o arquivo main.py no arquivo de teste 'teste_notepad.py'
