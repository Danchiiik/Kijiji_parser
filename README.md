## Kijiji parser
Был сделан парсинг [сайта Kijiji](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273).
Были спарсены URL картинок, дата публикации поста и цена с валютой.

***

Для парсинга использовались:
* Selenium
* BeautifulSoup
* lxml


Как СУБД использовался __peewee__, как база данных __PostgreSQL__.

***

#### Как запустить проект
1. Скопируй репозиторий
    * ``` git clone git@github.com:Danchiiik/Kijiji_parser.git ```
2. Создай и активируй виртуальное окружение
    * ``` python -m venv <venv name> ```
    * ``` . <venv name>/bin/activate ```
3. Загрузи все зависимости из __requirements.txt__
    * ``` pip install -r requirements.txt ```
4. Создай .env файл и запиши свои данные как в env_example
5. Запусти проект
    * ``` python main.py ```

