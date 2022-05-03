import HtmlTestRunner
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Vlad/Desktop/TESTER/Tmall_Aliexpress_selenium_autotesting/chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_01_password_invalid(self):
        driver = self.driver
        driver.get("https://login.aliexpress.ru/?spm=a2g0o.tm800006433.1000002.8.79447bda4YVVOG&return=https%3A%2F%2Fpromotion.aliexpress.ru%2Fwow%2Fgcp%2Faer%2Fchannel%2Faer%2Ftmall_localization%2F7pcZWCh8tW%3Fwh_weex%3Dtrue%26_immersiveMode%3Dtrue%26wx_navbar_hidden%3Dtrue%26wx_navbar_transparent%3Dtrue%26ignoreNavigationBar%3Dtrue%26wx_statusbar_hidden%3Dtrue&from=lighthouse&_ga=2.180832871.1548761681.1650904559-5240418.1645310182")
        login = LoginPage(driver)
        login.enter_username("kirdgach@gmail.com")
        login.enter_password("11111111111111111")
        login.click_login()
        driver.implicitly_wait(10)
        message = login.check_invalid_password_message()
        self.assertEqual(message, "Ваши учетное имя или пароль неправильные.")
        time.sleep(2)

    def test_02_login_invalid(self):
        driver = self.driver
        driver.get("https://login.aliexpress.ru/?spm=a2g0o.tm800006433.1000002.8.79447bda4YVVOG&return=https%3A%2F%2Fpromotion.aliexpress.ru%2Fwow%2Fgcp%2Faer%2Fchannel%2Faer%2Ftmall_localization%2F7pcZWCh8tW%3Fwh_weex%3Dtrue%26_immersiveMode%3Dtrue%26wx_navbar_hidden%3Dtrue%26wx_navbar_transparent%3Dtrue%26ignoreNavigationBar%3Dtrue%26wx_statusbar_hidden%3Dtrue&from=lighthouse&_ga=2.180832871.1548761681.1650904559-5240418.1645310182")
        login = LoginPage(driver)
        login.enter_username("1q1q1q1q1q1q@gmail.com")
        login.enter_password("Kirdg@ch444")
        login.click_login()
        message1 = login.check_invalid_login_message()
        self.assertEqual(message1, "Ваши учетное имя или пароль неправильные.")
        time.sleep(2)

    def test_03_login_and_password_invalid(self):
        driver = self.driver
        driver.get("https://login.aliexpress.ru/?spm=a2g0o.tm800006433.1000002.8.79447bda4YVVOG&return=https%3A%2F%2Fpromotion.aliexpress.ru%2Fwow%2Fgcp%2Faer%2Fchannel%2Faer%2Ftmall_localization%2F7pcZWCh8tW%3Fwh_weex%3Dtrue%26_immersiveMode%3Dtrue%26wx_navbar_hidden%3Dtrue%26wx_navbar_transparent%3Dtrue%26ignoreNavigationBar%3Dtrue%26wx_statusbar_hidden%3Dtrue&from=lighthouse&_ga=2.180832871.1548761681.1650904559-5240418.1645310182")
        login = LoginPage(driver)
        login.enter_username("1")
        login.enter_password("1")
        login.click_login()
        driver.implicitly_wait(10)
        message = login.check_invalid_password_message()
        message1 = login.check_invalid_login_message()
        self.assertEqual(message, "Ваши учетное имя или пароль неправильные.")
        self.assertEqual(message1, "Ваши учетное имя или пароль неправильные.")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
       cls.driver.close()
       cls.driver.quit()
       print("Tests are done")


class ScenarioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Vlad/Desktop/TESTER/Tmall_Aliexpress_selenium_autotesting/chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_04_login_valid(self):
        driver = self.driver
        driver.get("https://login.aliexpress.ru/?spm=a2g0o.tm800006433.1000002.8.79447bda4YVVOG&return=https%3A%2F%2Fpromotion.aliexpress.ru%2Fwow%2Fgcp%2Faer%2Fchannel%2Faer%2Ftmall_localization%2F7pcZWCh8tW%3Fwh_weex%3Dtrue%26_immersiveMode%3Dtrue%26wx_navbar_hidden%3Dtrue%26wx_navbar_transparent%3Dtrue%26ignoreNavigationBar%3Dtrue%26wx_statusbar_hidden%3Dtrue&from=lighthouse&_ga=2.180832871.1548761681.1650904559-5240418.1645310182")
        login = LoginPage(driver)
        login.enter_username("kirdgach@gmail.com")
        login.enter_password("Kirdg@ch444")
        login.click_login()
        time.sleep(2)
        homepage = HomePage(driver)
        # проверка авторизации пользователя
        message = homepage.check_welcome_message()
        self.assertEqual(message, 'Vlad Smekalin')
        time.sleep(2)

    def test_05_click_wishlist(self):
        driver = self.driver
        """ чтобы запустить тест отдельно необходимо добавить строки из login_valid теста,
        а также поменять self.wishlist_link_text в homePage.py на "Мои жeлания" """
        homepage = HomePage(driver)
        homepage.click_wishlist()
        # проверка изменения API страницы на Wishlist
        new_driver = driver.current_url
        wishlist_url = str(new_driver)
        self.assertIn("https://my.aliexpress.com/wishlist/wish_list_product_list.", wishlist_url)

    def test_06_click_logo(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_logo()
        # проверка перехода на страницу Ali
        new_driver = driver.current_url
        ali_url = str(new_driver)
        self.assertIn("https://pl.aliexpress.com/?gatewayAdapt", ali_url)
        time.sleep(2)

    def test_07_logout(self):
       driver = self.driver
       driver.execute_script("window.history.go(-3)")
       time.sleep(2)
       homepage = HomePage(driver)
       homepage.click_logout()
       message = homepage.check_successful_logout_message()
       self.assertEqual(message, "Войти")

    def test_08_popular_items_button(self):
        """проверка кликабельности кнопки "популярные" в подвале главной страницы"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_pupular_items_button()
        # проверка открытия новой страницы с популярными товарами
        new_driver = driver.current_url
        popular_url = str(new_driver)
        self.assertIn("https://www.aliexpress.com/popular", popular_url)
        # возвравт на 1 страницу назад (на главную) с прокруткой в начало страницы
        driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.scrollTo(0, top)")
        time.sleep(2)

    def test_09_cart_icon(self):
        """проверка кликабельности кнопки "популярные" в подвале главной страницы"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_cart_icon()
        # проверка открытия новой страницы с популярными товарами
        new_driver = driver.current_url
        cart_url = str(new_driver)
        self.assertIn("https://shoppingcart.aliexpress.com/shopcart/", cart_url)
        time.sleep(2)

    def test_10_language_change(self):
        """проверка возможности смены языка"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_language_change()
        time.sleep(2)
        driver.implicitly_wait(10)
        message = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/h2').text
        driver.implicitly_wait(15)
        self.assertEqual(message, 'Ваша Корзина пуста')
        driver.execute_script("window.history.go(-1)")

    def test_11_rewind_right(self):
        """проверка работы кнопки перемотки вправо"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_rewind_right()

    def test_12_clothes_bar(self):
        """проверка кликабельности карточек товаров"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_clothes_bar()
        # проверка открытия новой страницы с детской одеждой
        new_driver = driver.current_url
        clothes_url = str(new_driver)
        self.assertIn("https://aliexpress.ru/category/202000215/mother-kids.html", clothes_url)

    def test_13_items_presence(self):
        """проверка наличия контента на странице карточки товара"""
        driver = self.driver
        homepage = HomePage(driver)
        message = homepage.check_items()
        self.assertEqual('Извините, мы не нашли товаров по Вашему запросу "". Пожалуйста, попробуйте поискать снова.', message)

    def test_14_search(self):
        """проверка работы поиска"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.insert_values_to_search("одежда для собак")
        homepage.click_search()
        new_driver = driver.current_url
        dog_clothes_url = str(new_driver)
        msg = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div/div[1]/h1').text
        self.assertIn("https://aliexpress.ru/wholesale?catId=&SearchText=", dog_clothes_url)
        self.assertEqual('одежда для собак', msg)

    def test_15_check_product_card(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_product_card()
        time.sleep(2)
        # перенос внимание сценария на новую открытую вкладку браузера
        driver.switch_to.window(driver.window_handles[1])
        driver.execute_script("window.scrollTo(0, 1000)")
        msg = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div/div[8]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span').text
        self.assertEqual('ОБЩАЯ ИНФОРМАЦИЯ', msg)

    def test_16_add_to_cart(self):
        """проверка добавления товара в корзину"""
        driver = self.driver
        homepage = HomePage(driver)
        driver.execute_script("window.scrollTo(0, top)")
        homepage.click_add_to_cart()
        msg = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/div[2]/span').text
        self.assertIn('Товар был добавлен', msg)

    def test_17_item_present_in_cart(self):
        """проверка наличия товаров в корзине после добавления"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_go_to_cart()
        msg = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div/div[1]/div/div[2]')
        self.assertIsNotNone(msg, "cart is empty")
        time.sleep(2)

    def test_18_buy_item_unauthorised(self):
        """проверка кнопки 'купить' в неавторизованном режиме"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.buy_item()
        msg = driver.find_element(By.XPATH, '//*[@id="modal-popup-zh"]/div[2]/div/div[2]/div[1]/div/div[2]/span').text
        self.assertEqual('ВХОД', msg)
        time.sleep(2)

    def test_19_buy_item_authorise(self):
        """проверка возможности авторизоваться для покупки"""
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("kirdgach@gmail.com")
        login.enter_password("Kirdg@ch444")
        login.click_login_on_pop_up()
        msg = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div').text
        self.assertIn('перенаправлены', msg)
        time.sleep(2)

    def test_20_redirect_to_buy(self):
        """проверка кликабельности кнопки переносящей на страницу Aliexpress для покупки"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_continue()
        new_driver = driver.current_url
        ali_url = str(new_driver)
        self.assertIn("https://shoppingcart.aliexpress.com/orders.htm", ali_url)

    def test_21_delete_item_from_cart(self):
        """проверка возможности удалить товар из корзины"""
        driver = self.driver
        homepage = HomePage(driver)
        driver.execute_script("window.history.go(-2)")
        time.sleep(2)
        homepage.delete_item()
        time.sleep(2)
        msg = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/button[1]').text
        self.assertEqual('OK', msg)

    def test_22_approve_deleting(self):
        """проверка на отсутствие удаленного товара в корзине"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_ok()
        time.sleep(2)
        msg = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/p').text
        self.assertIn("Ваша Корзина пуста", msg)

    def test_23_sorting_by_number_of_orders(self):
        """проверка сортировки товаров по количеству заказов"""
        driver = self.driver
        homepage = HomePage(driver)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        homepage.click_sort_by_number_of_orders()
        time.sleep(2)

    def test_24_sorting_by_color(self):
        """проверка сортировки товаров по цвету"""
        driver = self.driver
        homepage = HomePage(driver)
        driver.execute_script("window.scrollTo(0, 500)")
        homepage.sort_by_black_color()

    def test_25_item_has_black_color(self):
        """проверка на присутствие черного цвета в фильтруемом по черному цвету товаре"""
        driver = self.driver
        homepage = HomePage(driver)
        driver.execute_script("window.scrollTo(0, top)")
        homepage.check_color_of_item()
        time.sleep(2)

    def test_26_description_is_present(self):
        """проверка на наличие описания товара"""
        driver = self.driver
        homepage = HomePage(driver)
        message = homepage.check_description()
        self.assertIsNotNone(message, 'описание товара пусто')

    def test_27_star_raiting_is_present(self):
        """проверка на наличие рейтинга товара (звезд)"""
        driver = self.driver
        homepage = HomePage(driver)
        message = homepage.check_star_raiting()
        self.assertIsNotNone(message, 'рейтинг товара пуст')

    def test_28_recomendations_are_present(self):
        """проверка присутствия рекомендаций на похожие товары в подвале страницы"""
        driver = self.driver
        homepage = HomePage(driver)
        message = homepage.check_recomendations_presence()
        self.assertEqual('Похожие предложения', message)

    def test_29_support_is_clickable(self):
        """проверка кликабельности кнопки Служба поддержки"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_support()
        message = driver.find_element(By.XPATH, '//*[@id="ice-container"]/div/div/div[1]/div/h2').text
        self.assertEqual('Сервис Покупателя', message)

    def test_30_FAQ_is_present(self):
        """Проверка на наличие Часто задаваемых вопросов"""
        driver = self.driver
        homepage = HomePage(driver)
        message = homepage.check_faq()
        self.assertEqual('Часто задаваемые вопросы', message)

    def test_31_open_chat(self):
        """Проверка кликабельности кнопки чата"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_to_chat()
        new_driver = driver.current_url
        chat_url = str(new_driver)
        self.assertIn("https://h5-global.alimebot.aliexpress.com/", chat_url)

    def test_32_write_to_chat(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.write_to_chat('По доставке')
        message = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div/div[3]/div[5]/div/div/p').text
        self.assertEqual('По доставке', message)

    def test_33_chat_options(self):
        """проверка кликабельности опций предоставляемых виртуальным помощником"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.choose_option()
        message = driver.find_element(By.ID, 'modal-0').text
        self.assertEqual('Выберите интересующий заказ', message)

    def test_34_finished_order_details(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_order_details()
        message = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[1]').text
        self.assertIn('5017151218553672', message)

    def test_35_accept_cookie(self):
        """проверка кликабельности принятия куки"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_accept_cookie()
        cookie_container = driver.find_element(By.ID, 'gdpr-new-container')
        if cookie_container.is_displayed():
            print('куки не были приняты')
        else:
            print('куки приняты')

    def test_36_contacts_button(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_contacts()
        new_driver = driver.current_url
        management_url = str(new_driver)
        self.assertIn("https://feedback.aliexpress.com/management", management_url)

    def test_37_vk_icons(self):
        driver = self.driver
        homepage = HomePage(driver)
        driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        homepage.click_vk_icon()
        new_driver = driver.current_url
        vk_url = str(new_driver)
        self.assertIn("https://vk.com/", vk_url)

    def test_38_youtube_icon(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_youtube_icon()
        new_driver = driver.current_url
        youtube_url = str(new_driver)
        self.assertIn("youtube", youtube_url)

    def test_39_clear_filter(self):
        """проверка работы кнопки очистить фильтры"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_clear_all()
        message = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[1]/div/div[1]/div[1]/div[2]').text
        self.assertNotIn('Черный', message)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Tests are done")


class RegisTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Vlad/Desktop/Tmall_Aliexpress_selenium_autotesting/chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_40_registration(self):
        driver = self.driver
        homepage = HomePage(driver)
        driver.get('https://login.aliexpress.ru/?spm=a2g0o.tm800006433.1000002.8.79447bda4YVVOG&return=https%3A%2F%2Fpromotion.aliexpress.ru%2Fwow%2Fgcp%2Faer%2Fchannel%2Faer%2Ftmall_localization%2F7pcZWCh8tW%3Fwh_weex%3Dtrue%26_immersiveMode%3Dtrue%26wx_navbar_hidden%3Dtrue%26wx_navbar_transparent%3Dtrue%26ignoreNavigationBar%3Dtrue%26wx_statusbar_hidden%3Dtrue&from=lighthouse&_ga=2.180832871.1548761681.1650904559-5240418.1645310182')
        driver.implicitly_wait(10)
        homepage.click_registration()
        message = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/span').text
        self.assertEqual('Зарегистрироваться по Email', message)

    def test_41_send_sms_with_code(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.enter_tlf('9648955900')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[5]/span')))
        self.assertIn('Проведите для входа', element.text)

    def test_42_captcha(self):
        """проверка работы капчи"""
        driver = self.driver
        homepage = HomePage(driver)
        homepage.captcha_drag()

    def test_43_registration_by_email(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_registration_by_email()
        email_field = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[2]/input')
        self.assertIsNotNone(email_field, 'поле для ввода email отсутствует')

    def test_44_invalid_registration_email(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_reg_email('svoboda.ru')
        login.enter_reg_password('UuuU#$#$1281O0')
        login.click_enter_reg()
        msg = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/span').text
        self.assertIn('Такого адреса почты не существует', msg)

    def test_45_invalid_registration_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_reg_email('svoboda_vsem_daromm@yandex.ru')
        login.enter_reg_password('0007')
        login.click_enter_reg()
        error = driver.find_element(By.CLASS_NAME, 'batman-v2_index__error__15m07o').is_displayed()
        self.assertTrue(error)

    def test_46_valid_credentials_for_registration(self):
        """проверка заполнения формы корректными данными"""
        driver = self.driver
        login = LoginPage(driver)
        login.enter_reg_email('svoboda_vsem_daromm@yandex.ru')
        login.enter_reg_password('UuuU#$#$1281O0')
        login.click_enter_reg()
        msg = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div/div[2]/div/div/h1').text
        self.assertIn('Добро пожаловать!', msg)

    def test_47_change_email_btn(self):
        """проверка работы кнопки смены email"""
        driver = self.driver
        login = LoginPage(driver)
        login.click_change_email_btn()
        email_field = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[2]/input').is_displayed()
        self.assertTrue(email_field)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Tests are done")


class TmallTest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Vlad/Desktop/TESTER/Tmall_Aliexpress_selenium_autotesting/chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_48_electronics_btn(self):
        driver = self.driver
        homepage = HomePage(driver)
        driver.get('https://promotion.aliexpress.ru/wow/gcp/aer/channel/aer/tmall_localization/7pcZWCh8tW?wh_weex=true&_immersiveMode=true&wx_navbar_hidden=true&wx_navbar_transparent=true&ignoreNavigationBar=true&wx_statusbar_hidden=true')
        driver.implicitly_wait(10)
        homepage.click_electronics()
        tlf = driver.find_element(By.XPATH, '//*[@id="tab-container-id"]/div[1]/div/div/div/div/div[1]/span').is_enabled()
        self.assertTrue(tlf)

    def test_49_brand_type(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_samsung()
        msg = driver.find_element(By.CLASS_NAME, 'SearchBreadcrumbs_SearchBreadcrumbs__query__b61od').text
        self.assertIn('"samsung"', msg)

    def test_50_searchpool_form(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_no('НА ЭТОМ ВСЕ!!!!')
        form = driver.find_element(By.XPATH, '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[7]/form')
        form.is_displayed()
        self.assertTrue(form)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Tests are done")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Vlad/Desktop/TESTER/Tmall_Aliexpress_selenium_autotesting/reports'))
