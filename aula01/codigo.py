# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas as pd
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
pyautogui.PAUSE = 0.3
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# esperar o link carregar
time.sleep(3)

# Passo 2: Fazer o login
# Point(x=760, y=549) usuario
# Point(x=722, y=699) senha
pyautogui.click(x=760, y=549)
pyautogui.write("admin@gmail.com")
pyautogui.click(x=722, y=699)
pyautogui.write("admin")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# fechar alert de verificar senha
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
tabela = pd.read_csv("produtos.csv")
print(tabela)

# index = linhas
# columns = colunas
for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    # clica no primeiro campo
    pyautogui.click(x=749, y=380)

    # preencher os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # se a obs não for nula
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")  

    # apertar para enviar
    # rolar para o topo
    pyautogui.scroll(5000)
    # Passo 5: Repetir o cadastro para todos os produtos