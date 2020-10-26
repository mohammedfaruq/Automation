#! python3
#Omar series - https://www.islamicity.org/series/omar-ibn-khattab-series-episode-6-english-subtitles/
# This script automates the following:

#1. Open https://www.islamicity.org/series/omar-ibn-khattab-series-episode-6-english-subtitles/
#2. Click on episode link
#3. Make full screen
#4. Click Play





from selenium import webdriver
import pyinputplus as pyip
import time


print(
'''
 1 - Omar Ibn Khattab
 2 - Islam Begins
 3 - Muhammad's Message & Abu Lahab
 4 - Family Affairs, Torture and Boycott Muslims
 5 - Persecution of Muslims by the Meccans
 6 - Bilal ibn Rabah Gains Freedom and Embraces Islam
 7 - Migration to Abyssinia
 8 - Omar Embraces Islam, First Sermon
 9 - Boycott Against Muslims
 10 - Hijrah to Yathrib, Medina, Building Al-Masjid an-Nabawi
 11 - Battle of Badr, Death of Abu Jahl
 12 - Quraish Plan for the Second Battle Against Muslims
 13 - Battle of Uhud, Digging the Trench
 14 - Battle of Khandaq, Treaty of Hudaibiyah
 15 - The Year of Delegations, First Hajj
 16 - Khalid ibn al-Walid Embrace Islam, Conquest of Mecca
 17 - Abu Sufyan Embrace Islam, Death of Muhammad PBUH
 18 - Abu Bakr Becomes the First Caliph
 19 - Rise of Sajah, Ridda Wars
 20 - Battle of Yamama Against Musaylimah
 21 - Muslim Conquest of Persia
 22 - Death of Abu Bakr, Umar Becomes Caliph, Battle of Yarmouk
 23 - Battle of Yarmouk Against Theodore Trithyrius
 24 - Muslim Conquest of the Levant
 25 - Omar and his Subjects
 26 - Siege of Damascus
 27 - Battle of al-Qadisiyyah Against Sassanids
 28 - Siege of Jerusalem
 29 - Famine Year
 30 - Plague, Conquest of Egypt
 ''')






while True:
#enter episode number between 1-30
    episode = pyip.inputNum (prompt= "Enter episode number: ",min = 1, max = 30)
    
   


#open episode site
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get('https://www.islamicity.org/series/omar-ibn-khattab-series-episode-'+str(episode)+'-english-subtitles')
    time.sleep(5)


    try:
        #scroll down to make video player buttons visible
        browser.execute_script("window.scrollTo(0, 600)") 

        #switch focus to video player iframe
        browser.switch_to.frame(browser.find_element_by_xpath('/html/body/div[12]/div/div/div/main/article/div/div/div[2]/iframe'))
        FullScreen = browser.find_element_by_class_name('fullscreen')
        FullScreen.click()
        #print(FullScreen)

        #Play 
        PlayButton = browser.find_element_by_xpath('//*[@id="player"]/div[7]/div[3]/button')
        PlayButton.click()

        
    except:
       print(' Element not found')
    
