# Projeto Integrador

Esse é um projeto integrador necessário para a conclusão do curso integrado em redes de computadores, do Instituto Federal de Educação, Ciência e Tecnologia de Sergipe - Campus Lagarto. O grupo é formado por Carlos Eduardo, Jonata Fontes e Gabriel da Conceição. Alfredo Vieira e Anselmo Machado são os professores orientadores.

O projeto é um aplicativo mobile chamado de Literabit, e tem como objetivo ser uma biblioteca digital, agregando livros em domínio público disponíveis em fontes na internet, como o [site do projeto Gutenberg](https://www.gutenberg.org/). Algumas da funcionalidades são a pesquisa por materiais disponíveis, a leitura dos livros e a visualização de informações coletadas no uso do app.

# Conteúdos

- [Configuração do Ambiente](#configuração-do-ambiente)
  - [Configuração universal para trabalhar em qualquer editor](#para-qualquer-editor)
  - [Configuração específica para o PyCharm](#para-o-pycharm)

- [Building](#building)

- [Instalação](#instalação)
  - [Instalação a partir de pacotes pré-compilados](#pacotes-pré-compilados)
  - [Instalação a partir do código fonte](#instalando-a-partir-da-fonte)

- [A fazer](#a-fazer)

# Configuração do Ambiente

Esse projeto utiliza o [Buildozer](https://github.com/kivy/buildozer) para empacotar o aplicativo para Android/IOS. No entanto, é necessário possuir um sistema Linux ou OSX para realizar esse processo. Se você possui um desses sistemas, acesse a [documentação do buildozer](https://buildozer.readthedocs.io/) e realize a instalação das dependências necessárias. O buildozer será instalado nos passos seguintes desse tutorial. 

Caso não tenha acesso a uma máquina com Linux/OSX, pode tentar uma máquina virtual em um programa como o [VirtualBox](https://www.virtualbox.org/). Se não puder instalar o Buildozer, não será possível empacotar ou executar o aplicativo em dispositivos mobile, mas ainda será possível desenvolver e executá-lo em seu desktop.

## Para qualquer editor

Os passos a seguir devem ser feitos no terminal e usam a convenção do Unix(Linux, MacOs...). Portanto, faça as adaptações necessárias se estiver em um ambiente Windows.

  - Certifique-se de que o [Git](https://git-scm.com/downloads), o [Python 3](https://www.python.org/downloads/) e o [pip](https://pip.pypa.io/en/stable/installing/) estão instalados no sistema.
  - Executar o comando `pip install virtualenv` para instalar o [virtualenv](https://pypi.org/project/virtualenv/) globalmente.
  - Entrar no seu diretório de trabalho (qualquer diretório da sua preferência).
  - Clonar o repositório com o comando `git clone url-desse-repositório`.
  - Entrar no diretório que foi criado pela clonagem do git no passo anterior com o comando `cd projeto-integrador`, por exemplo.
  - Executar o comando `virtualenv .` para criar um ambiente virtual isolado.
  - Executar o arquivo de ativação do ambiente virtual, que está localizado em `./bin/activate`. **Essa etapa deve ser feita toda vez que se for trabalhar no projeto**.
  - Rodar o comando `pip install -r requirements.txt` para instalar as dependências.
  - Por fim, o comando `python projeto_integrador/main.py` executa o projeto.

## Para o PyCharm

Se você prefere usar o PyCharm, essa é uma configuração específica.

  - Na tela inicial do pycharm, clicar no botão `Get from version control`.
  - Clicar na aba `Repository URL`.
  - Selecionar o controle de versionamento `git`.
  - No campo url, inserir a `url-desse-repositório`.
  - Escolher o nome do diretório que será criado.
  - Clicar em `clonar`.
  - Abrir o menu de configurações, clicar em `Project: nome-do-projeto` e em `Python Interpreter`.
  - No campo `Python Interpreter`, clicar no ícone da engrenagem e em `add`.
  - Selecionar a opção `Virtualenv Environment` e a opção `new environment`.
  - Na opção `Base Interpreter`, selecionar a versão mais recente do python 3.
  - Selecionar o ambiente que acabou de ser criado e deixar as outras opções como estão e clicar em Ok. Na janela seguinte clicar em Ok.
  - No terminal do Pycharm, rodar o comando `pip install -r requirements.txt`.
  - Para rodar o projeto basta executar o arquivo `projeto_integrador/main.py`.

# Building

Esse é o processo para construir e/ou instalar o aplicativo para dispositivos Android ou IOS. Lembrando que, se o Buildozer não puder ser instalado de forma correta, você ainda pode executar o arquivo `projeto_integrador/main.py` normalmente. Buildar para dispositivos IOS requer um computador MacOs. Buildar para Android pode ser feito tanto em um sistema Linux quanto em um MacOs.

  - Verifique a [documentação](https://buildozer.readthedocs.io/) do [Buildozer](https://github.com/kivy/buildozer) para conhecer todas as opções disponíveis.
  - Como exemplo, o comando `buildozer -v android debug deploy run logcat` irá instalar e executar o aplicativo em seu dispositivo android conectado via USB ao desktop, além de armazenar uma cópia do APK no diretório `build`. Esse comando também escreve todos os logs do Android em seu terminal. O comando `buildozer -v android debug` apenas compila e salva o APK.

A primeira vez que a compilação é realizada é um processo bastante lento.

# Instalação

## Pacotes pré-compilados

Esses pacotes são compilados previamente a cada nova versão e estão prontos para uso. Acesse a [aba de releases](https://github.com/c4rls/projeto-integrador/releases) no github, faça o download do pacote (no momento apenas o formato APK está disponível) na última versão e instale no seu dispositivo.

## Instalando a partir da fonte

Faça a [configuração necessária](#configuração-do-ambiente) e siga os passos descritos na [seção de build](#building) para compilar o app a partir do código fonte. O pacote ficará disponível do diretório `build`. Use esse arquivo para instalar em seu dispositivo. 

# A fazer

- [x] Menu lateral.
- [ ] Switch entre telas com o menu lateral.
- [ ] Download dos livros e manter no armazenamento local. Manter o ID dos livros para consulta de informações.
- [ ] Tela de livros baixados.
- [ ] Modal com informações do livro.
- [ ] Viewer de livros.
- [x] Separar o arquivo 'projetointegrador.kv' e o código dos widgets em vários arquivos.
- [ ] Evitar o congelamento da UI em tarefas pesadas.
- [ ] Melhorar a UI.
- [ ] Splash Screen e Ícone.
- [ ] Diminuir o tamanho dos pacotes gerados.
