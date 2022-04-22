from selenium import webdriver

region = {
    "Москва": "moskva",
    "Москва и Московская область": "moskva_i_mo",
    "Московская область": "moskovskaya_oblast",
    "Россия": "rossiya"
}

options = webdriver.ChromeOptions()

# user agent

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")

# disable webdriver mode

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/home/grindelwald/python_apps/bot/app/chromedriver",
    options=options
)

query = "asus f5r"

try:
    url = ""+region["Московская область"]+"?q=" + query
    driver.get(url)
    
    
    
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
