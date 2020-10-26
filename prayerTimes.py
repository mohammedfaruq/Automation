#! python3

#get prayer times from east london mosque website.

import requests, logging, bs4, time, lxml

#enable logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start')

#download East London Mosque home page
rawELMPage = requests.get('https://www.eastlondonmosque.org.uk/prayer-times')
logging.info('Downloaded')
time.sleep(5)

rawELMPage.raise_for_status()

ELMPage = bs4.BeautifulSoup(rawELMPage.text, 'lxml')

logging.info('Textified')



#PrayerTimes = ELMPage.select('div.salah-time-row.time-start')
#PrayerTimes = ELMPage.select('#pageHeader > div.content.headerContent > div > div.salah-block-content.mceNonEditable > div.salah-times > div.salah-time-row.time-start > span.col2')
PrayerTimes = ELMPage.select('#pageHeader > div.content.headerContent > div > div.salah-block-content.mceNonEditable > div.salah-times > div.salah-time-row.time-start > span.col3.pi1.col-s.fajr')

type(PrayerTimes)



print(PrayerTimes[0].text)
#Fajr = PrayerTimes[0].getText()


