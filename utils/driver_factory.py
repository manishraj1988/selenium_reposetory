from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config import config


class DriverFactory:
    @staticmethod
    def get_driver(browser_name=None):
        browser = browser_name or config.BROWSER

        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if config.HEADLESS:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-blink-features=AutomationControlled")

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if config.HEADLESS:
                options.add_argument("--headless")

            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        elif browser.lower() == "edge":
            options = webdriver.EdgeOptions()
            if config.HEADLESS:
                options.add_argument("--headless=new")

            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver