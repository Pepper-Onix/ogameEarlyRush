#!/usr/bin/env python
  
import requests
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CONSTANTS
T = 4


#FUNCIONS
def click(xpath):
    btn = driver.find_element_by_xpath(xpath)
    btn.click()
    time.sleep(1)

def write(token,xpath):
    form = driver.find_element_by_xpath(xpath)
    form.send_keys("%s" % (token))
    time.sleep(1)

def login(email,password):
    click("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]")
    time.sleep(T - 1)
    click("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[3]/input")
    time.sleep(T - 1)
    write(email,"/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/input")
    time.sleep(T/2)
    write(password,"/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form /div[2]/div/input")
    time.sleep(T/2)
    click("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/p/button[1]") 
    time.sleep(T - 1)
    click("/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/button")
    time.sleep(T + 1)

def resources():
    click("/html/body/div[7]/div[2]/div[2]/div/ul/li[2]/a/span")
    time.sleep(T)

def upgradeMetal():
    click("/html/body/div[6]/div[3]/div[2]/div/div[2]/ul/li[1]/span")
    time.sleep(2)
    click("/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[4]/button")
    
def upgradeCrystal():
    click("/html/body/div[6]/div[3]/div[2]/div/div[2]/ul/li[2]/span")
    time.sleep(2)
    click("/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[4]/button")
    
def upgradeDeut():
    click("/html/body/div[6]/div[3]/div[2]/div/div[2]/ul/li[3]/span")
    time.sleep(2)
    click("/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/button")

def upgradeSolar():
    click("/html/body/div[6]/div[3]/div[2]/div/div[2]/ul/li[4]/span")
    time.sleep(2)
    click("/html/body/div[6]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[4]/button")

def delay(resource,v,lvl):
    
    if resource == "metal":
        resource = 108
    elif resource == "crystal":
        resource = 103
    elif resource == "deut":
        resource = 432
    elif resource == "solar":
        resource = 151
    else:
        return 0

    time.sleep( (resource + lvl)/v )

def rush25():
    upgradeSolar()
    delay("solar",10,0) #Lvl 1
    upgradeMetal()
    delay("metal",10,0) #Lvl 1
    upgradeMetal()
    delay("metal",10,54) #Lvl 2
    upgradeSolar()
    delay("solar",10,76) #Lvl 2
    upgradeMetal()
    delay("metal",10,135) #Lvl 3
    upgradeMetal()
    delay("metal",10,256) #Lvl 4
    upgradeSolar()
    delay("solar",10,190) #Lvl 3
    upgradeCrystal()
    delay("crystal",10,0) #Lvl 1
    upgradeMetal()
    delay("metal",10,439) #Lvl 5
    upgradeSolar()
    delay("solar",10,358) #Lvl 4
    upgradeCrystal()
    delay("crystal",10,64) #Lvl 2
    upgradeCrystal()
    delay("crystal",10,161) #Lvl 3
    upgradeSolar()
    delay("solar",10,615) #Lvl 5
    upgradeDeut()
    delay("deut",10,0) #Lvl 1
    upgradeCrystal()
    delay("crystal",10,323) #Lvl 4
    upgradeSolar()
    delay("solar",10,996) #Lvl 6
    upgradeMetal()
    delay("metal",10,711) #Lvl 6
    upgradeMetal()
    delay("metal",10,1123) #Lvl7
    upgradeSolar()
    delay("solar",10,1571) #Lvl 7
    upgradeCrystal()
    delay("crystal",10,575) #Lvl 5
    upgradeDeut()
    delay("crystal",10,217) #Lvl 2
    upgradeSolar()
    solarDelay(151,10,2432) #Lvl 8
    upgradeDeut()
    delay("crystal",10,540) #Lvl 3
    upgradeDeut()
    delay("crystal",10,1026) #lvl 4
    upgradeDeut()
    delay("crystal",10,1755) #Lvl 5



#def upgradeResources(resource):
#    print("Select the resource you want to upgrade:")
#    print("[1] METAL")
#    print("[2] CRYSTAL")
#    print("[3] DEUTERIUM")
#    print("[4] SOLAR PLANT")


#PROGRAMA
print("What do u want to do?")
print("[1]Login or [2]Register ")
a = input()

if a = 1: #Login
    driver = webdriver.Firefox()
    driver.get("https://lobby.ogame.gameforge.com")
    time.sleep(T)

    login("correuobert15@gmail.com","Correuobert15")
    driver.get("https://s180-en.ogame.gameforge.com/game/index.php?page=ingame&component=overv  iew&relogin=1")
    time.sleep(T * 2)
else: #Register
    driver = webdriver.Firefox()
    driver.get("https://lobby.ogame.gameforge.com")
    time.sleep(T)

    register("correuobert15@gmail.com","Correuobert15")
    driver.get("https://s180-en.ogame.gameforge.com/game/index.php?page=ingame&component=overv  iew&relogin=1")
    time.sleep(T * 2)


resources()
click("/html/body/div[7]/div[3]/div[2]/div/div[2]/ul/li[1]/span")
time.sleep(T)
click("/html/body/div[7]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[4]/button")


print("aa")
time.sleep(60)
