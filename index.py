from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service("./driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()

bot.get("https://www.viajesexito.com/")
time.sleep(3)

try:
    iframe = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[contains(@class, "bhr-iframe-holder--custom")]'))
    )
    bot.switch_to.frame(iframe)


    close_button = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]'))
    )
    close_button.click()

    bot.switch_to.default_content()

    packages = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]')
    time.sleep(1)
    packages.click()
    time.sleep(1)

    searchorigin = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]')
    searchorigin.click()
    time.sleep(1)
    originInput = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    originInput.click()
    time.sleep(1)
    originInput.send_keys('eldorado')
    time.sleep(1)

    originOption = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li[1]')
    originOption.click()
    time.sleep(1)

    searchDestination = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div')
    searchDestination.click()
    time.sleep(1)
    destinationInput = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    destinationInput .click()
    time.sleep(1)
    destinationInput .send_keys('punta cana')
    time.sleep(1)

    originOption = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li')
    originOption.click()
    time.sleep(1)

    dates = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div') 
    dates.click()
    time.sleep(1)

    departureData = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[4]/div[2]') 
    departureData.click()
    time.sleep(1)

    returnData = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]') 
    returnData.click()
    time.sleep(1)

    accept = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/button[2]') 
    accept.click()
    time.sleep(1)

    guests = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div') 
    guests.click()
    time.sleep(2)

    addRoom = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]') 
    addRoom.click()
    time.sleep(2)

    take = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button') 
    take.click()
    time.sleep(2)


    search = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]') 
    search.click()
    time.sleep(20)

    original_window = bot.current_window_handle
    all_windows = bot.window_handles

    for window in all_windows:
        if window != original_window:
            bot.switch_to.window(window)
            break

    # Esperar a que aparezca el precio
    price = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))
    ).text
    print(price)

    price2 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price2)

    price3 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price3)

    price4 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price4)

    price5 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price5)

    price6 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price6)

    price7 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price7)

    price8 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price8)

    price9 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price9)

    price10 = bot.find_element(By.XPATH , "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    print(price10)

    AdvanceOptions = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a') 
    AdvanceOptions.click()
    time.sleep(2)

    airline = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input') 
    airline.click()
    time.sleep(2)
    airline.send_keys('copa airlines')
    time.sleep(1)

    copaAirline = bot.find_element(By.XPATH, '/html/body/ul[3]/li') 
    copaAirline.click()
    time.sleep(2)

    searchAirline = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input') 
    searchAirline.click()
    time.sleep(20)

    departureDate = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div').text
    returnDate=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div').text
    depPlace=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div[3]').text
    arrivalPlace=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/div[2]').text
    depTime=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]').text
    arrivalTime=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[2]').text

    depTime2=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]').text
    arrivalTime2=  bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[2]').text
    time.sleep(2)

    text = f'''Best package deal with copa Airline.
    
    Departure Date : {departureDate}
    Return Date : {returnDate}
    Total cost: {price}
    
    Outbound Flight:
        Departure Place : {depPlace}
        Arrival Place : {arrivalPlace}
        Departure Time : {depTime}
        Arrival Time : {arrivalTime}

    Return Flight:
        Departure Place : {arrivalPlace}
        Arrival PLace : {depPlace}
        Departure Time : {depTime2}
        Arrival Time : {arrivalTime2}
    '''

    with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(text)

    bot.save_screenshot('screenshot.png')

except Exception as e:
    print("error:", e)

time.sleep(3)
bot.quit()