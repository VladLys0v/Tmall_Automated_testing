# Tmall_Automated_testing
Selenium/Python automated testing for Tmall/Aliexpress websites

Тестовые сценарии проверяют кликабельность кнопок, фильтры, строку поиска, возможность залогиниться и т.д. Проверяется также присутствие элементов на странице.
Названия тестов читаемы, также присутствует закоментированные описания. 
В конце login.py файла добавлена функция формирования HTML отчета. Отчет формируется по окончании запуска тестов и сохраняется в директории reports.
Для запуска теста необходимо знать путь до файла chromedriver.exe. Для этого в PyCharm в левой колонке находим файл chromedriver.exe, кликает по нему правой клавишей мыши, выбираем Copy Path --> Absolute Path.  В моем случае адрес следующий: C:/Users/Vlad/Desktop/TESTER/Tmall_Aliexpress_selenium_autotesting/chromedriver.exe
Команда для запуска указана ниже, но запускать кнопочно поклассово удобнее на мой взгляд: 
python -m pytest -v --html=.\reports\report.html --driver Chrome --driver-path C:/Users/Vlad/Desktop/TESTER/Tmall_Aliexpress_selenium_autotesting/chromedriver.exe Tests\login.py
(падает 32 тест - надо поменять xpath чтобы нацелить его на поиск title тега alt c названием "черный", чтобы провести проверку)
