# Projeto Integrador

Esse é um projeto integrador necessário para a conclusão do curso integrado em redes de computadores, do Instituto Federal de Educação, Ciência e Tecnologia de Sergipe - Campus Lagarto. O grupo é formado por Carlos Eduardo, Jonata Fontes e Gabriel da Conceição. Alfredo Vieira e Anselmo Machado são os professores orientadores.

O projeto é um aplicativo mobile chamado de Literabit, e tem como objetivo ser uma biblioteca digital, agregando livros em domínio público disponíveis em fontes na internet, como o [site do projeto Gutenberg](https://www.gutenberg.org/). Algumas da funcionalidades são a pesquisa por materiais disponíveis, a leitura dos livros e a visualização de informações coletadas no uso do app.

# ⚡️ Configuração do Ambiente

Esse projeto utiliza o [Buildozer](https://github.com/kivy/buildozer) para empacotar o aplicativo para Android/IOS. No entanto, é necessário possuir um sistema Linux ou OSX para realizar esse processo. Se você possui um desses sistemas, acesse a [documentação do buildozer](https://buildozer.readthedocs.io/) e realize a instalação das dependências necessárias. O buildozer será instalado nos passos seguintes com o pip. 

Caso não tenha acesso a uma máquina com Linux/OSX, pode tentar uma máquina virtual com o [VirtualBox](https://www.virtualbox.org/). Se não puder instalar o Buildozer, não será possível empacotar ou executar o aplicativo em dispositivos mobile, mas ainda será possível desenvolver e executá-lo em seu desktop.

## Para qualquer editor

Os passos a seguir devem ser feitos no terminal e usam a convenção do Unix(Linux, MacOs...). Portanto, faça as adaptações necessárias se estiver em um ambiente Windows.

  - 1: Certifique-se de que o [Git](https://git-scm.com/downloads), o [Python 3](https://www.python.org/downloads/) e o [pip](https://pip.pypa.io/en/stable/installing/) estão instalados no sistema.
  - 2: Executar o comando `pip install virtualenv` para instalar o [virtualenv](https://pypi.org/project/virtualenv/) globalmente.
  - 3: Entrar no seu diretório de trabalho (qualquer diretório da sua preferência)
  - 4: Clonar o repositório com o comando `git clone url-dessa-pagina`.
  - 5: Entrar no diretório que foi criado pela clonagem do git no passo anterior.
  - 6: Executar o comando `virtualenv .` para criar um ambiente virtual isolado.
  - 7: Executar o arquivo de ativação do ambiente virtual, que está localizado em `./bin/activate`. Essa etapa deve ser feita toda vez que se for trabalhar no projeto.
  - 8: Rodar o comando `pip install -r requirements.txt` para instalar as dependências.
  - 9: Por fim, o comando `python projeto_integrador/main.py` executa o projeto

## Para o PyCharm

  - 1: Na tela inicial do pycharm, clicar no botão `Get from version control`
  - 2: Clicar na aba `Repository URL`
  - 3: Selecionar o controle de versionamento `git`
  - 4: No campo url, inserir a url-dessa-pagina
  - 5: Escolher o nome do diretório que será criado
  - 6: Clicar em `clonar`
  - 7: Abrir o menu de configurações, clicar em `Project: nome-do-projeto` e em `Python Interpreter`
  - 8: No campo `Python Interpreter`, clicar no ícone da engrenagem e em `add`
  - 9: Selecionar a opção `Virtualenv Environment` e a opção `new environment`
  - 10: Na opção `Base Interpreter`, selecionar a versão mais recente do python 3
  - 11: Selecionar o ambiente que acabou de ser criado e deixar as outras opções como estão e clicar em Ok. Na janela seguinte clicar em Ok
  - 12: No terminal do Pycharm, rodar o comando `pip install -r requirements.txt`
  - 13: Para rodar o projeto basta executar o arquivo `projeto_integrador/main.py`

## Build

  - Verifique a [documentação](https://buildozer.readthedocs.io/) do [Buildozer](https://github.com/kivy/buildozer) para conhecer todas as opções disponíveis.
  - Como exemplo, o comando `buildozer -v android debug deploy run logcat` irá instalar e executar o aplicativo em seu dispositivo android conectado via USB ao desktop, além de armazenar uma cópia do APK no diretório `build`. Esse comando também escreve todos os logs do Android em seu terminal.
