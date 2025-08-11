# RE605X Configurator

Ferramenta em Python para configurar automaticamente o repetidor TP-Link RE605X via interface gráfica e automação com Selenium.

Python tool to automatically configure the TP-Link RE605X Wi-Fi repeater using a graphical interface and Selenium automation.

---

## Funcionalidades | Features

- Detecta redes Wi-Fi disponíveis
- Permite selecionar uma rede e digitar a senha
- Abre a interface do repetidor e preenche os campos automaticamente
- Interface moderna com `tkinter`
- Compatível com Chrome, Firefox e Edge

- Detects available Wi-Fi networks
- Allows selecting a network and entering the password
- Opens the repeater interface and fills in the fields automatically
- Modern interface using `tkinter`
- Compatible with Chrome, Firefox, and Edge

---

## Requisitos | Requirements

- Windows 10 ou superior
- Python 3.8+ (apenas para desenvolvimento)
- Navegador instalado: Chrome, Firefox ou Edge
- Internet na primeira execução (para baixar o WebDriver)

- Windows 10 or later
- Python 3.8+ (development only)
- Installed browser: Chrome, Firefox, or Edge
- Internet required on first run (to download WebDriver)

---

## Instalação | Installation

```bash
git clone https://github.com/seu-usuario/re605x-configurator.git
cd re605x-conf.
pip install -r requirements.txt
python main.py
```

### Para usuários finais | For end users
Baixe o arquivo main.exe compilado e execute diretamente.
Não é necessário instalar Python ou dependências.

Download the compiled main.exe and run it directly.
No need to install Python or dependencies.

Uso | Usage
- Conecte-se à rede Wi-Fi do repetidor TP-Link (ex: TP-Link_Extender_XXXX).
- Execute o programa.
- Selecione a rede principal e digite a senha.
- Clique em "Configurar".
- O navegador abrirá e a automação será executada.

- Connect to the TP-Link repeater Wi-Fi network (e.g., TP-Link_Extender_XXXX).
- Run the program.
- Select your main network and enter the password.
- Click "Configure".
- The browser will open and automation will run.
