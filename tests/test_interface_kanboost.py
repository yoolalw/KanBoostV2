import time

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

    # 1
    def test_displayed_items_in_homepage(self):
        time.sleep(3)

        self.chrome.find_element(By.ID, "regBtn").is_displayed()
        time.sleep(1)
        self.chrome.find_element(By.ID, "relBtn").is_displayed()
        time.sleep(1)
        self.chrome.find_element(By.ID, "kanBtn").is_displayed()

    # 2
    def test_click_in_register_button(self):
        time.sleep(3)
        self.chrome.find_element(By.ID, "regBtn").click()
        time.sleep(1)
        WebDriverWait(self.chrome, 4).until(
            ec.url_to_be('http://127.0.0.1:5500/registerPage.html')
        )

    # 3
    def test_error_msg(self):
        self.chrome.get('http://127.0.0.1:5500/registerPage.html')
        time.sleep(3)
        self.chrome.find_element(By.ID, 'button').click()
        time.sleep(1)
        WebDriverWait(self.chrome, 10).until(
            ec.visibility_of_element_located((By.ID, 'msg'))
        )
        time.sleep(1)
        msg = self.chrome.find_element(By.ID, 'msg')
        assert msg.text == 'Campo de cadastro vazio! Preencha-o e tente novamente.'

    # 4
    def test_inserting_itens_in_field(self):
        self.chrome.get('http://127.0.0.1:5500/registerPage.html')
        time.sleep(3)
        self.chrome.find_element(By.ID, 'input').send_keys('Atividade 1')
        time.sleep(1)
        self.chrome.find_element(By.ID, 'button').click()

    # 5
    def test_clicking_in_kanban_button(self):
        time.sleep(3)
        self.chrome.find_element(By.ID, 'kanBtn').click()
        time.sleep(1)
        WebDriverWait(self.chrome, 10).until(
            ec.url_to_be('http://127.0.0.1:5500/kanban.html')
        )

    # 6
    def test_verifyng_if_ativ_has_been_created(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)
        atividade = self.chrome.find_element(By.CLASS_NAME, "atividade")
        assert atividade.text == 'Atividade 1\nVoltar\nAvançar'

    # 7
    def test_moving_ativ_to_doing_column(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)
        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

    # 8
    def test_moving_ativ_to_done_column(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

    # 9
    def test_block_moving_ativ(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

    # 10
    def test_returns_ativ_to_doing_column(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        voltar = self.chrome.find_element(By.ID, "voltar")
        voltar.click()
        time.sleep(1)

    # 11
    def test_returns_ativ_to_todo_column(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        voltar = self.chrome.find_element(By.ID, "voltar")
        voltar.click()
        time.sleep(1)

        voltar = self.chrome.find_element(By.ID, "voltar")
        voltar.click()
        time.sleep(1)

    # 12
    def test_blocks_returns_ativ(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        voltar = self.chrome.find_element(By.ID, "voltar")
        voltar.click()
        time.sleep(1)

        voltar = self.chrome.find_element(By.ID, "voltar")
        voltar.click()
        time.sleep(1)

        voltar = self.chrome.find_element(By.ID, "voltar")
        voltar.click()
        time.sleep(1)

    # 13
    def test_inserting_multiples_ativs(self):
        self.chrome.get('http://127.0.0.1:5500/registerPage.html')

        time.sleep(3)
        self.chrome.find_element(By.ID, 'input').send_keys('Atividade 2')
        self.chrome.find_element(By.ID, 'button').click()
        time.sleep(1)
        self.chrome.find_element(By.ID, 'input').send_keys('Atividade 3')
        self.chrome.find_element(By.ID, 'button').click()

        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(1)
        self.chrome.find_element(By.CLASS_NAME, 'atividade').is_displayed()

    # 14
    def test_moving_multiples_ativs(self):
        self.chrome.get('http://127.0.0.1:5500/kanban.html')
        time.sleep(3)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

        avancar = self.chrome.find_element(By.ID, "avancar")
        avancar.click()
        time.sleep(1)

    # 15
    def test_click_in_button_for_generate_document(self):
        time.sleep(3)
        relBtn = self.chrome.find_element(By.ID, 'relBtn')
        relBtn.click()
        time.sleep(4)