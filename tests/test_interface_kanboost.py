import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def chrome(request):
    service = webdriver.ChromeService()
    chrome = webdriver.Chrome(service=service)
    request.cls.chrome = chrome
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()


@pytest.mark.usefixtures("chrome")
class TestPages:

    def setup_method(self):
        self.chrome.get('http://127.0.0.1:5500/homepage.html')

    def test_displayed_items_in_homepage(self):
        self.chrome.find_element(By.ID, "regBtn").is_displayed()
        self.chrome.find_element(By.ID, "relBtn").is_displayed()
        self.chrome.find_element(By.ID, "kanBtn").is_displayed()

    def test_click_in_register_button(self):
        self.chrome.find_element(By.ID, "regBtn").click()
        WebDriverWait(self.chrome, 4).until(
            ec.url_to_be('http://127.0.0.1:5500/registerPage.html')
        )

    def test_error_msg(self):
        self.chrome.get('http://127.0.0.1:5500/registerPage.html')
        self.chrome.find_element(By.ID, 'button').click()
        WebDriverWait(self.chrome, 10).until(
            ec.visibility_of_element_located((By.ID, 'msg'))
        )
        msg = self.chrome.find_element(By.ID, 'msg')
        assert msg.text == 'Campo de cadastro vazio! Preencha-o e tente novamente.'

    def test_inserting_itens_in_field(self):
        self.chrome.get('http://127.0.0.1:5500/registerPage.html')
        self.chrome.find_element(By.ID, 'input').send_keys('Atividade 1')
        self.chrome.find_element(By.ID, 'button').click()

    def test_verifying_if_ativ_has_been_created(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        atividade = self.chrome.find_element(By.CLASS_NAME, "atividade")
        assert atividade.text == 'Atividade 1\nVoltar\nAvançar'