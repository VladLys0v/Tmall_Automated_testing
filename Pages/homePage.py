from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_menu_xpath = '//*[@id="nav-user-account"]/div[1]/div/span[2]/b'
        self.logout_btn_xpath = '//*[@id="nav-user-account"]/div[2]/div[1]/a'
        self.wishlist_link_text = 'Wish List'
        self.enter_link_text = 'Войти'
        self.my_data_xpath = '//*[@id="nav-user-account"]/div[2]/ul/li[1]/a'
        self.hello_message_xpath = '//*[@id="root"]/div[1]/div[1]/div'
        self.logo_btn_xpath = '//*[@id="header"]/div/div[1]/div/a/span'
        self.popular_button_xpath = '/html/body/div[2]/div[1]/div/div[2]/dl/dd/span/a[1]'
        self.cart_icon_button = '//*[@id="header"]/div/div[2]/div[1]/a'
        self.language_change_button = '//*[@id="switcher-info"]/span[3]'
        self.language_change_input_field = '//*[@id="nav-global"]/div[3]/div/div/div/div[2]/div/span'
        self.language_russian = '//*[@id="nav-global"]/div[3]/div/div/div/div[2]/div/ul/li[2]/a'
        self.apply_change_button = '//*[@id="nav-global"]/div[3]/div/div/div/div[4]/button'
        self.rewind_right_arrow = '//*[@id="7176050980"]/div/div/div/div/div[2]'
        self.clothes_bar_button = '//*[@id="7176050980"]/div/div/div/div/div[3]/a[6]'
        self.search_error_class_name = 'SearchHeader_StickyContainer__stickyContainer__1hf3t'
        self.search_error_message_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/span'
        self.search_field_xpath = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/form/div/div/input'
        self.search_button_class_name = 'SearchHeader_SearchSection__searchButton__4opvn'
        self.baby_prod_bar_xpath = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[1]'
        self.product_card_xpath = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[1]'
        self.add_to_cart_button_xpath = '//*[@id="#content"]/div[7]/div[2]/button'
        self.click_go_to_cart_button_xpath = '/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/a'
        self.choose_item_to_buy_class_name = 'ali-kit_Checkbox__wrapper__1ybo8o'
        self.buy_button_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/button'
        self.continue_button_xpath = '/html/body/div[6]/div[2]/div[2]/button'
        self.delete_item_button_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div[4]/div[1]/div/button[2]'
        self.click_ok_button_xpath = '/html/body/div[4]/div/div[2]/div[2]/button[1]'
        self.click_sort_by_number_of_orders_button_xpath = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/button[2]'
        self.click_black_checkbox_xpath = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[1]/div/div[1]/div[4]/ul/li[2]/label/span[1]'
        self.click_item_bar_xpath = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div/div[3]/div/div[1]'
        self.description_text_xpath = '//*[@id="__aer_root__"]/div/div/div[8]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/span'
        self.star_raiting_xpath = '//*[@id="__aer_root__"]/div/div/div[8]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]'
        self.recomendations_xpath = '//*[@id="__aer_root__"]/div/div/div[8]/div/div[2]/div/div[5]/div/h5'
        self.support_link_text = 'Служба поддержки'
        self.support_header_xpath = '//*[@id="ice-container"]/div/div/div[1]/div/h2'
        self.faq_xpath = '//*[@id="ice-container"]/div/div/div[5]/div[3]/div[1]/div/div/div/div[1]/h2'
        self.chat_button_xpath = '//*[@id="ice-container"]/div/div/div[5]/div[3]/div[3]/div/div/div[2]/div/div[1]/button'
        self.chat_field_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/textarea'
        self.chat_options_xpath = '//*[@id="root"]/div/div[1]/div[2]/div/div/div[3]/div[6]/div/div/div/div/div/div/div[2]/a[1]/div'
        self.details_button_xpath = '//*[@id="tabs-2-0"]/div[2]/div[1]/div[2]/div/div[1]/div[3]/button[1]'
        self.chat_send_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[3]/button'
        self.accept_cookie_button_xpath = '//*[@id="gdpr-new-container"]/div/div[2]/button[2]'
        self.contacts_button_xpath = '//*[@id="page-menu"]/div[4]/div'
        self.vk_xpath = '//*[@id="__aer_root__"]/div/div[4]/div[1]/div[2]/div[1]/div/a[2]'
        self.youtube_xpath = '//*[@id="__aer_root__"]/div/div[4]/div[1]/div[2]/div[1]/div/a[4]'
        self.clear_all_button_xpath = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[1]/div/div[1]/div[1]/div[1]/button'
        self.registr_btn_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[1]/div/div[1]/span'
        self.tlf_field_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div[2]/input'
        self.send_sms_btn = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/button'
        self.send_sms_btn_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/button'
        self.reg_by_email_btn_xpath = '//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[2]/div/div/div[2]/span'
        self.electronics_btn_xpath = '//*[@id="1408735750"]/div/div[1]/div/div/div[1]/a[1]'
        self.samsung_xpath = '//*[@id="7120684850"]/div/div/div/div/div/div/div/div/a[2]/img'
        self.no_btn_xpath = '/html/body/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/button[2]'
        self.ending_text = '//*[@id="__aer_root__"]/div/div[3]/div[1]/div[2]/div[1]/div[7]/form/div/textarea'

    def click_logout(self):
        welcome_menu = self.driver.find_element(By.XPATH, self.welcome_menu_xpath)
        logout_btn = self.driver.find_element(By.XPATH, self.logout_btn_xpath)
        # вызываем actions и выполняем действия с объявленными выше переменными
        actions = ActionChains(self.driver)
        # следующей командой наводим курсор на меню приветсвия пользователя
        actions.move_to_element(welcome_menu)
        actions.click(logout_btn)
        actions.perform()

    def click_wishlist(self):
        # проверка кликабельности кнопки Мои желания
        self.driver.find_element(By.LINK_TEXT, self.wishlist_link_text).click()

    def check_successful_logout_message(self):
        # проверка работы кнопки Выход
        msg = self.driver.find_element(By.LINK_TEXT, self.enter_link_text).text
        return msg

    def check_welcome_message(self):
        welcome_menu = self.driver.find_element(By.XPATH, self.welcome_menu_xpath)
        my_data = self.driver.find_element(By.XPATH, self.my_data_xpath)
        actions = ActionChains(self.driver)
        # следующей командой наводим курсор на меню приветсвия пользователя
        actions.move_to_element(welcome_menu)
        actions.click(my_data)
        actions.perform()
        msg = self.driver.find_element(By.XPATH, self.hello_message_xpath).text
        return msg

    def click_logo(self):
        self.driver.find_element(By.XPATH, self.logo_btn_xpath).click()

    def click_pupular_items_button(self):
        self.driver.execute_script("window.scrollTo(0, 20000)")
        self.driver.find_element(By.XPATH, self.popular_button_xpath).click()

    def click_cart_icon(self):
        self.driver.find_element(By.XPATH, self.cart_icon_button).click()
        self.driver.implicitly_wait(10)

    def click_language_change(self):
        self.driver.find_element(By.XPATH, self.language_change_button).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.language_change_input_field).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.language_russian).click()
        self.driver.find_element(By.XPATH, self.apply_change_button).click()

    def click_rewind_right(self):
        self.driver.set_window_size(1400, 1000)
        self.driver.execute_script("window.scrollTo(0, 21000)")
        self.driver.find_element(By.XPATH, self.rewind_right_arrow).click()

    def click_clothes_bar(self):
        self.driver.find_element(By.XPATH, self.clothes_bar_button).click()
        self.driver.maximize_window()

    def check_items(self):
        if self.driver.find_element(By.CLASS_NAME, self.search_error_class_name):
            msg = self.driver.find_element(By.XPATH, self.search_error_message_xpath).text
            print("Список товаров пуст")
            return msg
        else:
            self.driver.find_element(By.XPATH, self.baby_prod_bar_xpath).click()

    def insert_values_to_search(self, val):
        self.driver.find_element(By.XPATH, self.search_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_field_xpath).send_keys(val)

    def click_search(self):
        self.driver.find_element(By.CLASS_NAME, self.search_button_class_name).click()

    def click_product_card(self):
        if self.driver.find_element(By.XPATH, self.product_card_xpath).click():
            time.sleep(2)

    def click_add_to_cart(self):
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath).click()

    def click_go_to_cart(self):
        self.driver.find_element(By.XPATH, self.click_go_to_cart_button_xpath).click()

    def buy_item(self):
        self.driver.find_element(By.CLASS_NAME, self.choose_item_to_buy_class_name).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.buy_button_xpath).click()
        time.sleep(2)

    def click_continue(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.continue_button_xpath)))
        element.click()
        self.driver.implicitly_wait(10)

    def delete_item(self):
        self.driver.find_element(By.XPATH, self.delete_item_button_xpath).click()

    def click_ok(self):
        self.driver.find_element(By.XPATH, self.click_ok_button_xpath).click()

    def click_sort_by_number_of_orders(self):
        self.driver.find_element(By.XPATH, self.click_sort_by_number_of_orders_button_xpath).click()

    def sort_by_black_color(self):
        self.driver.find_element(By.XPATH, self.click_black_checkbox_xpath).click()

    def check_color_of_item(self):
        self.driver.find_element(By.XPATH, self.click_item_bar_xpath).click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 100)")
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//alt[contains(text(),"Черный")]'))):
            print('Черный на месте')
            return "Черный на месте"
        else:
            print('Что-то пошло не так, надо поправить xpath, чтобы найти черный цвет')
            return "Что-то пошло не так, надо поправить xpath, чтобы найти черный цвет"

    def check_description(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.implicitly_wait(5)
        msg = self.driver.find_element(By.XPATH, self.description_text_xpath)
        return msg

    def check_star_raiting(self):
        self.driver.execute_script("window.scrollTo(0, 6000)")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.star_raiting_xpath)))
        return element

    def check_recomendations_presence(self):
        # перематывает страницу в самый низ
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.recomendations_xpath)))
            return element.text
        except TimeoutException as e:
            print('не нашел рекомендации в конце страницы' + str(e))
            return 'не нашел рекомендации в конце страницы'

    def click_support(self):
        self.driver.find_element(By.LINK_TEXT, self.support_link_text).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.support_header_xpath)))
        return element

    def check_faq(self):
        msg = self.driver.find_element(By.XPATH, self.faq_xpath).text
        return msg

    def click_to_chat(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.chat_button_xpath).click()

    def write_to_chat(self, delivery):
        self.driver.find_element(By.XPATH, self.chat_field_xpath).click()
        self.driver.find_element(By.XPATH, self.chat_field_xpath).send_keys(delivery)
        self.driver.find_element(By.XPATH, self.chat_send_button_xpath).click()

    def choose_option(self):
        self.driver.find_element(By.XPATH, self.chat_options_xpath).click()
        time.sleep(2)

    def click_order_details(self):
        self.driver.find_element(By.XPATH, self.details_button_xpath).click()
        self.driver.close()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(10)

    def click_accept_cookie(self):
        self.driver.find_element(By.XPATH, self.accept_cookie_button_xpath).click()

    def click_contacts(self):
        self.driver.find_element(By.XPATH, self.contacts_button_xpath).click()

    def click_vk_icon(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.vk_xpath).click()
        time.sleep(2)

    def click_youtube_icon(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.youtube_xpath).click()
        time.sleep(2)

    def click_clear_all(self):
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,top)")
        self.driver.find_element(By.XPATH, self.clear_all_button_xpath).click()

    def click_registration(self):
        self.driver.find_element(By.XPATH, self.registr_btn_xpath).click()

    def enter_tlf(self, tlf):
        self.driver.find_element(By.XPATH, self.tlf_field_xpath).click()
        self.driver.find_element(By.XPATH, self.tlf_field_xpath).send_keys(tlf)
        self.driver.find_element(By.XPATH, self.send_sms_btn_xpath).click()
        time.sleep(5)

    def captcha_drag(self):
        # капча находится в iframe
        frame = self.driver.find_element(By.ID, 'baxia-dialog-content')
        if frame.is_displayed():
            self.driver.switch_to.frame(frame)
            # зажимаем левую клавишу и проводим на 300px направо
            drag = self.driver.find_element(By.ID, 'nc_1_n1z')
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(drag, 300, 0).perform()
            self.driver.switch_to.default_content()
            print('капча успешно пройдена')
            return 'вы не робот'
        else:
            print('капча не появилась')
            # нажимаем кнопку отправки смс
            self.driver.find_element(By.XPATH, self.send_sms_btn).click()
            time.sleep(5)
            self.driver.execute_script("window.history.go(-1)")
            self.driver.implicitly_wait(10)
            return 'осталось только ввести код с телефона'

    def click_registration_by_email(self):
        self.driver.find_element(By.XPATH, self.reg_by_email_btn_xpath).click()

    def click_electronics(self):
        self.driver.find_element(By.XPATH, self.electronics_btn_xpath).click()

    def click_samsung(self):
        self.driver.find_element(By.XPATH, self.samsung_xpath).click()

    def click_no(self, bye):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.no_btn_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.ending_text).send_keys(bye)
        time.sleep(5)
