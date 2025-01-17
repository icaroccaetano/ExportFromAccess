from app.database.access_db import get_df
from app.database.bigdata_db import get_engine
from sqlalchemy import text
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
#from app.models.base.DadosConcurso import DadosPS2022

def main():
    dados_servidores = get_df("SELECT processoSEI FROM REQUISICOES_DESPACHOS WHERE status = 'Captura de tela OK'")
    engine = get_engine()
    browser = webdriver.Chrome()
    browser.get("https://sei.go.gov.br")
    browser.maximize_window()
    browser.implicitly_wait(10)

    browser.find_element(By.NAME, "txtUsuario").send_keys("01780742177")
    browser.find_element(By.ID,"pwdSenha").send_keys("0217Edu")
    browser.find_element(By.ID,"selOrgao").send_keys("SEDUC")
    browser.find_element(By.NAME,"Acessar").click()
    browser.execute_script("arguments[0].click();", browser.find_element(By.ID,'lnkInfraUnidade'))
    browser.execute_script("arguments[0].click();", browser.find_element(By.XPATH,"//*[text()='SEDUC/SUPLIC-12479']"))
    
    for dados_servidor in dados_servidores.itertuples():
        browser.find_element(By.NAME,"txtPesquisaRapida").send_keys(dados_servidor.processoSEI)
        browser.find_element(By.XPATH,"//*[@id='frmProtocoloPesquisaRapida']/div/span").click()
        browser.switch_to.frame("ifrVisualizacao")
        browser.execute_script("arguments[0].click();", browser.find_element(By.XPATH, "//*[@title='Enviar Processo']"))
        time.sleep(0.5)  # Aguarda 500ms
        browser.execute_script("objLupaUnidades.selecionar(700,500);")
        browser.switch_to.default_content()
        browser.switch_to.frame("modal-frame")
        sigla_unidade = browser.find_element(By.ID, "txtSiglaUnidade")
        sigla_unidade.click()
        sigla_unidade.clear()
        sigla_unidade.send_keys("SEDUC/SGDP-15916")
        browser.find_element(By.ID, "btnPesquisar").click()
        time.sleep(0.5)  # Aguarda 500ms
        browser.execute_script("infraSelecionarItens(this,'Infra');")
        Table = browser.find_element(By.CLASS_NAME, "infraTable")
        Lines = Table.find_elements(By.TAG_NAME, "tr")
        for Line in Lines:
            browser.implicitly_wait(1)
            coluns = Line.find_elements(By.TAG_NAME, "td")
            browser.implicitly_wait(10)
            if len(coluns) > 4:
                coluns[0].click()
        browser.find_element(By.ID, "btnTransportarSelecao").click()
        browser.find_element(By.ID, "btnFecharSelecao").click()
        time.sleep(0.1)  # Aguarda 100ms
        browser.switch_to.default_content()
        browser.switch_to.frame("ifrVisualizacao")
        browser.find_element(By.ID, "sbmEnviar").click()
        browser.switch_to.default_content()
if __name__ == "__main__":
    main()