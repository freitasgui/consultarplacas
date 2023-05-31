#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

placa_input = "NBX7618"
#op = webdriver.ChromeOptions()
#op.add_argument('headless')

#op.add_argument("--incognito")

driver = webdriver.Chrome()

#options=op
driver.get('http://www.despachantedok.com.br')
print("abrindo...")

try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form-consulta"]/div[1]/fieldset[1]/input'))
    )

except:
    driver.quit()
    print("Conexão com o servidor demorou muito :( ")
    
finally:
    placa = driver.find_element(By.XPATH, '//*[@id="form-consulta"]/div[1]/fieldset[1]/input')
    placa.send_keys(placa_input)
    email_dono = driver.find_element(By.XPATH, '//*[@id="mailHeader"]')
    email_dono.send_keys("traineefreitas@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="form-consulta"]/div[2]/button').click()

try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutDok"]/div/main/section/div/div/section/p/small'))
    )
except:
    driver.quit()
    print("Conexão com o servidor demorou muito :( ")
    
finally:
    print("Sucesso, os dados do veículo foram encontrados!")
    
    placa = str(driver.find_element(By.XPATH, '//*[@id="checkoutDok"]/div/main/section/div/div/section/div[1]/div[1]/span/p').text)
    proprietario = str(driver.find_element(By.XPATH, '//*[@id="checkoutDok"]/div/main/section/div/div/section/div[1]/div[2]/div[1]/p').text)
    cidade = str(driver.find_element(By.XPATH,'//*[@id="checkoutDok"]/div/main/section/div/div/section/div[1]/div[2]/div[2]/p').text)
    data_hora_consulta = str(driver.find_element(By.XPATH, '//*[@id="checkoutDok"]/div/main/section/div/div/section/p/small').text)
    total_deb = str(driver.find_element(By.XPATH, '//*[@id="var-barra-valor-total"]/div/div[2]/b').text)
    desc_debitos = str(driver.find_element(By. XPATH, '//*[@id="checkoutDok"]/div/main/section/div/div/section/div[2]/div[1]/div[1]').text)
    
    #if driver.find_element(By.XPATH, '//*[@id="checkoutDok"]/div/main/section/div/div/section/div[2]/div[1]/div[1]/p/b'):    
        
        
    #Descobrir fipe pela placa 
        
    driver.get('https://placafipe.com/placa/' + placa_input)
    print("Mais detalhes...")
    
    try:
        element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/p[1]'))
    )
        
    except:
        driver.quit()
        print("Conexão com o servidor demorou muito :( ")
        
    finally:
        descricao_do_veiculo = driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/p[1]').text
        
        marca = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[1]/td[2]/a').text)
        modelo = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[2]/td[2]').text)
        importado = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[3]/td[2]').text)
        ano = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[4]/td[2]').text)
        ano_modelo = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[5]/td[2]').text)
        cor = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[6]/td[2]').text)
        cilindrada = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[7]/td[2]').text)
        potencia = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[8]/td[2]').text)
        combustivel = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[9]/td[2]').text)
        chassi = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[10]/td[2]').text)
        motor_numero = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[11]/td[2]').text)
        passageiros_numero = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[12]/td[2]').text)
        uf = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[13]/td[2]').text)
        municipio = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/table[1]/tbody/tr[14]/td[2]').text)
        valor_fipe =  str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/div[4]/table/tbody/tr[1]/td[2]').text)
        aliquota = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/div[4]/table/tbody/tr[2]/td[2]').text)
        valor_ipva = str(driver.find_element(By.XPATH, '//*[@id="layout"]/div[2]/div/div[1]/div/div[4]/table/tbody/tr[3]/td[2]').text)
      
    print ("Possui Débitos debitos")
    print ("placa: " + placa)
    print ("Valor do IPVA: " + valor_ipva)
    print ("Cidade: " + cidade)
    print ("Nome do dono: "  + proprietario.replace('*', ''))
    print("Data da Consulta: " + data_hora_consulta)
    print("Total de débitos: " + total_deb)
    print("Lista de Débitos: " + desc_debitos.replace('Exibir detalhes', ''))
    print("Descrição do Veículo: " + descricao_do_veiculo)
    print("Marca do veículo: " + marca)
    print("Modelo: " + modelo)
    print("Importado: " + importado)
    print("Ano: " + ano )
    print("Ano - Modelo: " + ano_modelo)
    print("Cor: " + cor)
    print("Cilindrada: " + cilindrada)
    print("Potência: " + potencia)
    print("Combustível: " + combustivel)
    print("Chassi: " + chassi)
    print("Número do motor: " + motor_numero)
    print("Número máximo de passageiros: " + passageiros_numero)
    print("UF: " + uf)
    print("Municipio: " + municipio)
        
        
        
    

        


# In[ ]:




