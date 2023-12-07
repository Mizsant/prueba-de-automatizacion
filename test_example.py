from selenium.webdriver.chrome.webdriver import WebDriver
import yaml
import pytest
from selenium import webdriver

# Cargar datos desde un archivo YAML
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Fixture para iniciar y cerrar el navegador
@pytest.fixture
def browser():
    # Ruta al controlador WebDriver de Brave (Chromium)
    driver_path = 'C:\chromedriver'

    # Opciones específicas de Brave
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\Program Files\BraveSoftware\Brave-Browser\Application'

    # Iniciar el navegador Brave con las opciones
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    yield driver
    driver.quit()

# Ejemplo de prueba
def test_brave_browser(browser: WebDriver):
    # Cargar datos de prueba desde un archivo YAML
    test_data = load_test_data('datos_prueba.yaml')

    # Acceder a una URL utilizando el navegador Brave
    browser.get(test_data['url'])

    # Realizar alguna acción de prueba
    # ...

    # Afirmaciones o validaciones
    assert browser.title == test_data['expected_title']

    # Otras acciones o validaciones
    # ...

    # Generar un reporte HTML con pytest-html
    pytest_html = browser.get_driver_log('browser')
    return pytest_html

