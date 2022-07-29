import selenium 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Passo 1: Pegar a cotação do dolar
# abrir o navegador

navegador = webdriver.Chrome()

# entrar no google

navegador.get('https://www.google.com.br/')

# pesquisar cotação do dolar no google

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pegar cotação 

cotacao_dolar = navegador.find_element('xpath', 
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(cotacao_dolar)

#Passo 2: Pegar a cotação do euro.


# abrir o navegador

navegador = webdriver.Chrome()

# entrar no google

navegador.get('https://www.google.com.br/')

# pesquisar cotação do euro no google

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')

navegador.find_element('xpath',
                       '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pegar cotação 

cotacao_euro = navegador.find_element('xpath', 
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(cotacao_euro)

#Passo 3: Pegar a cotação do ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')

# pesquisar cotação do ouro no site

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

print(cotacao_ouro)


#Passo 4: Atualizar a base de dados
import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')


#Passo 5: Recalcular os Preços

# Atualizar as cotações
# No pandas podemos procurar utilizando tabela.loc(delocalizar)[linha, coluna]

tabela.loc[tabela['Moeda']== 'Dólar', "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela['Moeda']== 'Euro', "Cotação"] = float(cotacao_euro)
tabela.loc[tabela['Moeda']== 'Ouro', "Cotação"] = float(cotacao_ouro)


# Preço de compra = Preço Original + Cotação 

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# Preço de Venda = Preço de compra + Margem 

tabela['Preço de Venda'] = tabela['Preço de Compra'] + tabela['Margem']

print(('\n')*2,tabela)

# Passo 6: Exportar a base de dados em excel 

# Primeiro criamos o arquivo excel 

tabela.to_excel('Produto_atualizado.xlsx', index = False)




