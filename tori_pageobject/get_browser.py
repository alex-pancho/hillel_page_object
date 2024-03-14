from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


def chrome(debug=False):
    options = ChromeOptions()
    # options.add_argument('--headless=new')
    driver_ch = webdriver.Chrome()if debug else \
        webdriver.Chrome(options=options)
    driver_ch.maximize_window()
    return driver_ch


if __name__ == "__main__":
    import pathlib

    driver = chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    screen_path = pathlib.Path(__file__).parent / "screenshot.png"
    driver.save_screenshot(f'{screen_path}')
    driver.close()
