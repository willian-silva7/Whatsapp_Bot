from selenium import webdriver 
import time

class WhatsappBot:
  def __init__(self):
    self.mensagem = "_Olá eu sou o ZapBot *Willgnis*_ :robot \n" 
    self.mensagem2 = "_Assista a esse vídeo no Youtube: https://www.youtube.com/_"

    self.grupos = ["Grupo1",
    "Grupo2",
    "Grupo3"]
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

  def EnviarMensagens(self):
    # <div tabindex="-1" class="_1Plpp">
    self.driver.get('https://web.whatsapp.com/')
    time.sleep(30)
    for grupo in self.grupos:
        grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
        time.sleep(3)
        grupo.click()
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)
        chat_box.click()
        chat_box.send_keys(self.mensagem2)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)
        

bot = WhatsappBot()
bot.EnviarMensagens()