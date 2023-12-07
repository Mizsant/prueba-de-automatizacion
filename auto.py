import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Ruta al controlador WebDriver de Brave (Chromium)
    driver_path = '/ruta/al/controlador/webdriver'

    # Opciones específicas de Brave
    options = webdriver.ChromeOptions()
    options.binary_location = '/ruta/a/brave-browser'

    # Iniciar el navegador Brave con las opciones
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    yield driver
    driver.quit()

def test_login_to_pintopaq(browser):
    # Navegar a la página de inicio de sesión
    browser.get("https://pintopaq-online.iplus.com.do/lg-es/ut/login.aspx")

    # Encontrar los campos de usuario y contraseña, y el botón de inicio de sesión
    username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_LoginUser_UserName"))
    )
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_LoginUser_Password"))
    )
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_LoginUser_LoginButton"))
    )

    # Introducir credenciales
    username_input.send_keys("tu_usuario")
    password_input.send_keys("tu_contraseña")

    # Hacer clic en el botón de inicio de sesión
    login_button.click()

    # Validar que el inicio de sesión fue exitoso (usando alguna condición específica)
    # Por ejemplo, puedes verificar la presencia de algún elemento en la página después del inicio de sesión
    # Esperar a que aparezca algún elemento después del inicio de sesión
    try:
        element_after_login = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "elemento_despues_del_login"))
        )
        assert "Página después del login" in browser.title
    except Exception as e:
        # Si no se encuentra el elemento esperado, se asume que el inicio de sesión falló
        pytest.fail(f"El inicio de sesión falló: {e}")