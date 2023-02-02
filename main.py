from selenium import webdriver
from bs4 import BeautifulSoup as BS
from decouple import config
from datetime import datetime
from peewee import *
from urllib3.exceptions import MaxRetryError
import datetime
import time

db = PostgresqlDatabase(
    config('DB_NAME'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST')
)

class Hotel(Model):
    image = CharField()
    price = CharField()
    day = CharField()

    class Meta:
        database = db

db.create_tables([Hotel])


def get_data(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url=url)
        time.sleep(5)
        soup = BS(driver.page_source, 'lxml')
        
        with open('test.html', 'w') as f:
            f.write(str(soup))    
    except Exception as ex:
        print(ex) 
    finally:
        driver.close()
        driver.quit()
        
    with open('test.html') as f:
        src = f.read()   
    soup = BS(src, 'lxml')
    
    hotels_page = soup.find('main')
    hotels = hotels_page.find_all('div', class_='search-item')
    if hotels:
        for hotel in hotels:
            try:
                image = hotel.find('div', class_='image').find('img')['data-src']
                price = hotel.find('div', class_='price').text.strip()
                day = hotel.find('div', class_='location').find('span', class_='date-posted').text
                if 'minutes' in day or 'hours' in day:
                    day = datetime.datetime.now().date()
                    day = day.strftime('%d/%m/%Y')
                if 'Yesterday' in day:
                    day = datetime.datetime.now() - datetime.timedelta(days=1)
                    day = day.strftime('%d/%m/%Y')
                info = Hotel(
                            image=image, 
                            price=price, 
                            day=day
                            )
                info.save()
            except Exception as e:
                print(e) 


def main():
    try:
        for i in range(1, 101):
            url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273'
            get_data(url)
    except MaxRetryError:
        print('Operation is stopped')

 
    
if __name__ == '__main__':
    main()       