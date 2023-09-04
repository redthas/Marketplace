import time
# import alert
from datetime import datetime
import random

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from funciones.funciones_generales import GlobalFunctions

from os import mkdir
# import pyautogui
import socket
import os

t = .2


# xpath para buscar asiento //table[contains(@class, 'table seat-selector-table seat-selector-large') ] //a[contains(@class, "map-item seat-klass-stars-2  popover-button seat-taken")]
def test_demoRecorrido():
    print(socket.gethostbyname(socket.gethostname()))
    global driver, f, fe, i, referencia, filas
    origen = 'concepcion'
    destino = 'SANTIAGO'
    service = Service(executable_path="C:\SeleniumFirma\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(f"https://somebodyyyy:123qweasdzxc@"
               f""
               f"recorrido.club")
    driver.maximize_window()
    f = GlobalFunctions(driver)
    time.sleep(0.3)
    ida = driver.find_element(By.XPATH, "//*[@id='bus_travel_departure_city_id-selectized']")
    ida.send_keys(origen)
    ida.send_keys(Keys.ENTER)
    time.sleep(1)

    vuelta = driver.find_element(By.XPATH, "//*[@id='bus_travel_destination_city_id-selectized']")
    vuelta.send_keys(destino)
    vuelta.send_keys(Keys.ENTER)

    time.sleep(0.5)

    f.TextMixto("xpath", "//*[@id='bus_travel_departure_date']", "8/09/2023", 0.5)

    driver.find_element(By.XPATH, "//*[@id='bus-search-submit']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.refresh()
    time.sleep(2)
    button = driver.find_element(By.XPATH,
                                 "//*[@id='collapse-bus-operator-55']/div/ul/li[7]/div[2]/div/div[2]/p/a")  # Operador Eme bus

    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)

    filas = driver.find_elements(By.XPATH,
                                 "//*[@id='level-2-outbound'] //table[contains(@class, 'table seat-selector-table seat-selector-large') ] //tr   ").__len__()
    print(filas)
    contf = 1
    conta = 1
    asientos_libres_total = []
    asientos_nivel1 = []
    asientos_nivel2 = []
    asietos_individules = []
    asietos_bloqueados = []
    asietos_light = []
    prueba = [2, 30, 3, 37, 38]
    tipos2 = ['   seat-single seat-available seat', '  popover-button seat-taken', '    seat-available seat']

    f.ClickMixto("xpath", "//*[@id='seat-map-outbound']/ul/li[1]/a", 0.1)
    nivel = 1
    while nivel <= 2:

        while contf <= filas:
            while conta < 14:
                mapItem = 0
                while mapItem < len(prueba):
                    seat = 0
                    while seat < len(tipos2):
                        try:
                            num = driver.find_element(By.XPATH,
                                                      f"//*[@id='level-{nivel}-outbound'] //table[contains(@class, 'table seat-selector-table seat-selector-large') ] //tr[{contf}] //td[{conta}]  //a[contains(@class, 'map-item seat-klass-stars-{prueba[mapItem]}{tipos2[seat]}')]").text

                            if tipos2[seat] == '    seat-available seat' and nivel == 1:
                                asientos_nivel1.append(num)
                                asientos_libres_total.append(num)


                            elif tipos2[seat] == '   seat-single seat-available seat' and nivel == 1:
                                asientos_nivel1.append(num)
                                asientos_libres_total.append(num)
                                asietos_individules.append(num)

                            elif tipos2[seat] == '   seat-single seat-available seat' and nivel == 2:
                                asientos_nivel2.append(num)
                                asientos_libres_total.append(num)
                                asietos_individules.append(num)

                            elif prueba[mapItem] == '38' or prueba[mapItem] == '37':
                                asietos_light.append(num)

                            elif tipos2[seat] == '  popover-button seat-taken':
                                asietos_bloqueados.append(num)
                            else:
                                asientos_libres_total.append(num)
                                asientos_nivel2.append(num)


                        except:

                            pass

                        seat += 1
                    mapItem += 1
                    seat = 0
                mapItem = 0
                conta += 1

            conta = 1
            contf += 1
        nivel += 1
        if nivel == 2:
            contf = 0
            f.ClickMixto("xpath", "//*[@id='seat-map-outbound']/ul/li[2]/a", 0.2)

    print("Asientos disponibles del nivel 1: " + str(asientos_nivel1))
    print("Asientos disponibles del nivel 2: " + str(asientos_nivel2))
    print("Asientos disponibles individuales: " + str(asietos_individules))
    print("Asientos disponibles Light: " + str(asietos_light))
    print("Asientos bloqueados: " + str(asietos_bloqueados))
    print("Los Asientos disponibles EN TOTAL son: " + str(asientos_libres_total))

    pasajeros = random.randrange(1, 6)
    print("Los pasajes a comprar son: " + str(pasajeros))

    print(len(asientos_libres_total))
    print(asientos_libres_total)
    asientos_reservados = []
    while True:
        cont1 = 1

        while cont1 <= pasajeros:
            print("Pasajero" + str(cont1))
            # asientosl = len(asientos_libres_total) - 1
            print(asientos_libres_total)
            seat = random.choice(asientos_libres_total)
            print("Clic en el asiento: " + str(seat))
            if str(seat) in asientos_nivel1:
                f.ClickMixto("xpath", "//*[@id='seat-map-outbound']/ul/li[1]/a", 0.1)
                f.ClickMixto("xpath",
                             f"//table[contains(@class, 'table seat-selector-table seat-selector-large') ] //span[text()='{seat}']",
                             t)
                print("El asiento " + str(seat) + " fue reservado")
                asientos_nivel1.remove(str(seat))
                asientos_libres_total.remove(str(seat))
                time.sleep(0.5)
                asientos_reservados.append(seat)
                cont1 += 1
            else:
                f.ClickMixto("xpath", "//*[@id='seat-map-outbound']/ul/li[2]/a", 0.1)
                f.ClickMixto("xpath",
                             f"//table[contains(@class, 'table seat-selector-table seat-selector-large') ] //span[text()='{seat}']",
                             t)
                print("El asiento " + str(seat) + " fue reservado")
                asientos_nivel2.remove(str(seat))
                asientos_libres_total.remove(str(seat))
                time.sleep(0.5)
                asientos_reservados.append(seat)
                cont1 += 1
        break

    print(len(asientos_nivel2))
    print(asientos_libres_total)
    print(asientos_reservados)

    # pasajeros

    num_pasa = 0
    bloqueo = []
    pasaportes = ['1152712847', '11111111', '1152712884', '1152412567', '22412321']
    f.ClickMixto("xpath", "//*[@id='seat-selection-form']/div[1]/div/div[2]/div[2]/button", t)
    while num_pasa < pasajeros:
        if pasajeros == 1:
            datos_pasajeros = '1152712847'
            print(pasajeros)
        else:

            datos_pasajeros = random.choice(pasaportes)
        print("iD del pasajero: " + str(datos_pasajeros))

        print("Ids usados: " + str(bloqueo))
        if bloqueo.__contains__(str(datos_pasajeros)):
            print("Ids usados en el if: " + str(bloqueo))
        else:
            button2 = driver.find_element(By.XPATH,
                                          f"//*[@id='booking_tickets_attributes_{num_pasa}_passenger_document_passport']")
            driver.execute_script("arguments[0].click();", button2)
            f.TextMixto("xpath", f"//*[@id='booking_tickets_attributes_{num_pasa}_passenger_identification']",
                        f"{datos_pasajeros}", 1)
            bloqueo.append(datos_pasajeros)
            print("Se bloqueo el ID:" + datos_pasajeros)
            num_pasa += 1
            if datos_pasajeros == '1152712847':
                button2.send_keys(Keys.TAB)

    print("Ids Bloqueados en total: " + str(bloqueo))
    time.sleep(5)

    f.ClickMixto("xpath", "//*[@id='same-as-first-passenger']", 1)

    # compra

    f.TextMixto("xpath", "//*[@id='booking_phone']", "3225411271", 1)
    f.TextMixto("xpath", "//*[@id='booking_email']", "daniel.giraldo+bot@recorrido.cl", 1)
    f.TextMixto("xpath", "//*[@id='booking_email_confirmation']", "daniel.giraldo+bot@recorrido.cl", 2)

    pago = random.randrange(1, 2)
    print(pago)
    if pago == 1:  # webpay
        f.ClickXY("xpath", "//*[@id='passengers-form']/div[1]/div[4]", "20", "40", 2)
        f.ClickMixto("xpath", "//*[@id='submit-payment']/div/button", 2)
        f.ClickMixto("xpath", "//*[@id='summary-modal']/div/div/div[4]/div/div[2]/form/button", 1)
        f.ClickMixto("xpath", "//*[@id='debito']", 1)
        # Pago
        bank = driver.find_element(By.XPATH,
                                   "/html/body/app-root/app-home/main-panel/main/section/right-panel/app-debit/div/div/button")
        bank.click()
        bank.send_keys(Keys.TAB, Keys.ENTER)

        # f.ClickMixto("xpath", "/html/body/app-root/app-home/main-panel/main/section/right-panel/app-debit/div/div/button",10)
        time.sleep(1)
        f.TextMixto("xpath", "//*[@id='pan']", "4051 8856 0044 6623", 1)
        f.ClickMixto("xpath",
                     "/html/body/app-root/app-home/main-panel/main/section/right-panel/app-debit/form[1]/button",
                     1)
        f.TextMixto("xpath", "//*[@id='rutClient']", "11.111.111-1", 1)
        f.TextMixto("xpath", "//*[@id='passwordClient']", "123", 1)
        f.ClickMixto("xpath", "/html/body/div/form/table/tbody/tr[9]/td/input[1]", t)
        f.ClickMixto("xpath", "/html/body/div/form/table/tbody/tr[4]/td/input", 5)

        booking = driver.find_element(By.XPATH,
                                      "/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/p/strong").text
        print(booking)
        time.sleep(5)


    else:  # paypal

        f.ClickMixto("xpath", "//*[@id='paypal-radio']", 1)
        f.ClickMixto("xpath", "//*[@id='submit-payment']/div/button", 2)
        f.ClickMixto("xpath", "//*[@id='root']/div/div[1]/main/div[1]/div[1]/button", 1)
        f.TextMixto("xpath", "//*[@id='email']", "jan@recorrido.cl", 1)
        f.ClickMixto("xpath", "//*[@id='btnNext']", 1)
        f.TextMixto("xpath", "//*[@id='password']", "123qweasd", 1)
        f.ClickMixto("xpath", "//*[@id='btnLogin']", 1)
        f.ClickMixto("xpath", "//*[@id='payment-submit-btn']", 5)
        booking = driver.find_element(By.XPATH,
                                      "/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/p/strong").text
        print(booking)
        time.sleep(5)
