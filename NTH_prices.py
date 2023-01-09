import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
urun = input("Ürün adı: ")
detailProduct = input("Ürün modeli: ")


def trendyol():
    driver.get("https://www.google.com/")
    search = driver.find_element(By.CSS_SELECTOR,".gLFyf")
    search.send_keys(f"{urun} {detailProduct}  site:trendyol.com")
    search.send_keys(Keys.ENTER)
    site = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/a/h3")
    site.click()
    time.sleep(2)
    productName = driver.find_element(By.CLASS_NAME,"pr-new-br").text
    productPrice = driver.find_element(By.CLASS_NAME,"pr-bx-w").text
    print(f"Trendyol : {productName}")
    print(f"Fiyatı: {productPrice}")

def n11():
    driver.get("https://www.google.com/")
    search = driver.find_element(By.CSS_SELECTOR,".gLFyf")
    search.send_keys(f"{urun} {detailProduct}  site:n11.com")
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    site = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/a/h3")
    site.click()
    time.sleep(2)
    productName = driver.find_element(By.CLASS_NAME,"nameHolder").text
    productPrice = driver.find_element(By.CLASS_NAME,"newPrice").text
    print(f"N11 : {productName}")
    print(f"Fiyatı : {productPrice}")

def hepsiburada():
    driver.get("https://www.google.com/")
    search = driver.find_element(By.CSS_SELECTOR,".gLFyf")
    search.send_keys(f"{urun} {detailProduct}  site:hepsiburada.com")
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    site = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/a/h3")
    site.click()
    time.sleep(2)
    productName = driver.find_element(By.ID,"product-name").text
    productPrice = driver.find_element(By.ID,"offering-price").text
    print(f"Hepsiburada : {productName}")
    print(f"Fiyatı : {productPrice}")

def whichSite():
    try: 
        print("Hangi sitedeki fiyatı öğrenmek istiyorsunuz(n11-trendyol-hepsiburada) hepsini öğrenmek istiyorsanız 'hepsi' yazın")
        sites = input(": ")
        if sites == "n11":
            n11()
        elif sites == "trendyol":
            trendyol()
        elif sites == "hepsiburada":
            hepsiburada()
        elif sites == "hepsi":
            trendyol()
            print(" ")
            n11()
            print(" ")
            hepsiburada()
        else:
            print("Hata geçersiz site ismi!!")
            print("Tekrar deneyiniz")
            print("...")
            time.sleep(2)
            whichSite()

    except Exception as e:
        print(f"Hata: {e}")

whichSite()



