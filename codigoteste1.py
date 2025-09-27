import pyautogui    

import time

# pyautogui.click -> clicar em um lugar 
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win")  
pyautogui.write("microsoft edge")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer Login
# selecionar o campo de email
pyautogui.click(x=673, y=361)
pyautogui.write("pythonimpressionador@gmail.com")

# Preencher senha
pyautogui.press("tab")
pyautogui.write("minhasupersecreta")

# Botao logar
pyautogui.press("tab")
pyautogui.press("enter")

# Espera de 3s
time.sleep(3)

# Passo 3: Importar a base de produtos
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index: # Para cada linha da tabela
    pyautogui.click(x=700, y=239)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # Passar para o proximo campo
    marca =  tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") # Passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") # Passar para o proximo       

    categoria = str(tabela.loc[linha, "categoria"])  # string = texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab") # Passar para o proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # Passar para o proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # Passar para o proximo campo
    obs = str(tabela.loc[linha, "obs"]) 
         
    if obs != "nan": # Se tiver observação
        pyautogui.write(obs)

    pyautogui.press("tab") # Passar para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)






# Passo 5: Repetir o cadastro para todos os produtos


