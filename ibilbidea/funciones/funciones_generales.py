
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains #funciones de mouse


class GlobalFunctions():

   def __init__(self,drive): # se le pide el argumento
       self.drive = drive


   #Navegar url y tiempo
   def nave(self,url,tie):
       self.drive.get(url)
       print("Pagina en uso: " +str(url) )
       t = time.sleep(tie)
       return t



       # tomar elemento x id mejorado




   def SelectXpathAllTypes(self,xpath,tipo,dato,tie):
       try:
           val = self.SEX(xpath)
           val=Select(val)
           if(tipo=="text"):
               val.select_by_visible_text(dato)
           elif(tipo=="index"):
               val.select_by_index(dato)
           elif(tipo=="value"):
               val.select_by_value(dato)

           print("El campo seleccionado es: " + str(dato))
           t = time.sleep(tie)
           return t
       except TimeoutException as ex:
           print(ex.msg)
           t = time.sleep(tie)
           print("No se encontro el elemento: " + xpath)
           return t

   def UploadXpath(self, xpath,ruta, tie=1):
       try:
           val=self.SEX(ruta)
           val.send_keys(ruta)
           print("Se carga la img: " + ruta)
           t = time.sleep(tie)
           return t
       except TimeoutException as ex:
           print(ex.msg)
           t = time.sleep(tie)
           print("No se encontro el elemento: " + xpath)
           return t

   #radiobuttons
   def CheckXpath(self, xpath, tie):
       try:
           val = WebDriverWait(self.drive, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))  # se le da tiempo de encontrar el elemento
           val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
           val = self.drive.find_element(By.XPATH, xpath)  # lo encuentra
           val.click()
           print("Clic en el elemento: " + xpath)
           t = time.sleep(tie)
           return t
       except TimeoutException as ex:
           print(ex.msg)
           t = time.sleep(tie)
           print("No se encontro el elemento: " + xpath)
           return t

   def CheckXpathMasivo(self,tie,*args):
       try:
           for num in args:
               val = WebDriverWait(self.drive, 2).until(EC.visibility_of_element_located((By.XPATH, num)))  # se le da tiempo de encontrar el elemento
               val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
               val = self.drive.find_element(By.XPATH, num)  # lo encuentra
               val.click()
               print("Clic en el elemento: " + num)
               t = time.sleep(tie)
               return t
       except TimeoutException as ex:
           for num in args:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + num)
               return t

       #Selector Mixto

   def TextMixto(self, tipo, selector,texto, tie):
       if(tipo=="xpath"):
           try:
               val = self.SEX(selector)
               val = WebDriverWait(self.drive, 2).until(EC.visibility_of_element_located((By.XPATH, selector)))  # se le da tiempo de encontrar el elemento
               val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
               val = self.drive.find_element(By.XPATH, selector)  # lo encuentra
               val.clear()
               val.send_keys(texto)
               print("Escribiendo en el campo {} el texto {}".format(selector, texto))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:
               val = self.SEID(selector)
               val.clear()
               val.send_keys(texto)
               print("Escribiendo en el campo {} el texto {}".format(selector, texto))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       #click Mixto
   def ClickMixto(self, tipo, selector, tie):
       if(tipo=="xpath"):
           try:
               val = self.SEX(selector)
               val.click()
               print("Dando click en: "+ selector)
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:
               val = self.SEID(selector)
               val.click()
               print("Dando click en: " + selector)
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t


       #Si existe el valor
   def Existe(self, tipo, selector, tie):
       if(tipo=="xpath"):
           try:
               val = WebDriverWait(self.drive, 2).until(EC.visibility_of_element_located((By.XPATH, selector)))  # se le da tiempo de encontrar el elemento
               val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
               val = self.drive.find_element(By.XPATH, selector)  # lo encuentra
               val.click()
               print("El elemento {} -> existe ".format(selector))
               t = time.sleep(tie)
               return "Existe"
           except TimeoutException as ex:
               print(ex.msg)
               print("No se encontro el elemento: " + selector)
               return "No Existe"

       elif (tipo == "id"):
           try:
               val = WebDriverWait(self.drive, 2).until(EC.visibility_of_element_located((By.ID, selector)))  # se le da tiempo de encontrar el elemento
               val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
               val = self.drive.find_element(By.ID, selector)  # lo encuentra
               val.click()
               print("El elemento {} -> existe ".format(selector))
               t = time.sleep(tie)
               return "Existe"
           except TimeoutException as ex:
               print(ex.msg)
               print("No se encontro el elemento: " + selector)
               return "No Existe"

   def Dobleclick(self, tipo, selector, tie=.3):
       if(tipo=="xpath"):
           try:
               val = self.SEX(selector)
               act = ActionChains(self.drive)
               act.double_click(val).perform()
               print("Doble click xpath en {}".format(selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:
               val = self.SEID(selector)
               act = ActionChains(self.drive)
               act.double_click(val).perform()
               print("Doble click id en {}".format(selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

   def Clickderecho(self, tipo, selector, tie=.3):
       if(tipo=="xpath"):
           try:
               val = self.SEX(selector)
               act = ActionChains(self.drive)
               act.context_click(val).perform()
               print("Click derecho xpath en {}".format(selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:
               val = self.SEID(selector)
               act = ActionChains(self.drive)
               act.context_click(val).perform()
               print("Click derecho id en {}".format(selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t


   def DragAndDrop(self, tipo, selector, destino,tie=.3):
       if(tipo=="xpath"):
           try:

               val = self.SEX(selector)
               val2 = self.SEX(destino)
               act = ActionChains(self.drive)
               act.drag_and_drop(val,val2).perform()
               print("se solto el elemento xpath {} en {}".format(val2,selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:

               val = self.SEID(selector)
               val2 = self.SEX(destino)
               act = ActionChains(self.drive)
               act.drag_and_drop(val).perform()
               print("se solto el elemento id en {}".format(selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

   def DragAndDropXY(self, tipo, selector, x,y, tie=.3):
       if (tipo == "xpath"):
           try:
               self.drive.switch_to.frame(0)
               val = self.SEX(selector)
               act = ActionChains(self.drive)
               act.drag_and_drop_by_offset(val, x,y).perform()
               print("se solto el elemento xpath {} en {}".format(x,y, selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:
               self.drive.switch_to.frame(0)
               val = self.SEID(selector)
               act = ActionChains(self.drive)
               act.drag_and_drop_by_offset(val, x, y).perform()
               print("se solto el elemento id en {}".format(selector))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

   def ClickXY(self, tipo, selector, x, y, tie=.3):
       if (tipo == "xpath"):
           try:
               #self.drive.switch_to.frame(0)
               val = self.SEX(selector)
               act = ActionChains(self.drive)
               act.move_to_element_with_offset(val, x, y).click().perform()
               print("Click al elemento {} cordenada {}, {}".format(selector,x,y))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t

       elif (tipo == "id"):
           try:
               #self.drive.switch_to.frame(0)
               val = self.SEID(selector)
               act = ActionChains(self.drive)
               act.move_to_element_with_offset(val, x, y).click().perform()
               print("Click al elemento {} cordenadas {}, {}".format(selector, x, y))
               t = time.sleep(tie)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               t = time.sleep(tie)
               print("No se encontro el elemento: " + selector)
               return t



   #FUncion mejorar de seleccionar elemento por xpath
   def SEX(self, elemento):
       try:
           val = WebDriverWait(self.drive, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))  # se le da tiempo de encontrar el elemento
           val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
           val = self.drive.find_element(By.XPATH, elemento)  # lo encuentra
           return val
       except TimeoutException as ex:
           print(ex.msg)
           print("No se encontro el elemento: " + val)
           return "Gracias"

   # FUncion mejorar de seleccionar elemento por id

   def SEID(self, elemento):
       val = WebDriverWait(self.drive, 2).until(EC.visibility_of_element_located((By.ID, elemento)))  # se le da tiempo de encontrar el elemento
       val = self.drive.execute_script("arguments[0].scrollIntoView();", val)
       val = self.drive.find_element(By.ID, elemento)  # lo encuentra
       return val

   def Salida(self):
       print("Termino la prueba exitosamente")


