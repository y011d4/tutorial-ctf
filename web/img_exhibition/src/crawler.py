from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from secret import FLAG


def crawl(url, title):

    options = Options()
    options.add_argument("headless")
    options.add_argument("no-sandbox")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("disable-infobars")
    options.add_argument("disable-background-networking")
    options.add_argument("disable-default-apps")
    options.add_argument("disable-extensions")
    options.add_argument("disable-gpu")
    options.add_argument("disable-sync")
    options.add_argument("disable-translate")
    options.add_argument("hide-scrollbars")
    options.add_argument("metrics-recording-only")
    options.add_argument("mute-audio")
    options.add_argument("no-first-run")
    options.add_argument("dns-prefetch-disable")
    options.add_argument("safebrowsing-disable-auto-update")
    options.add_argument("media-cache-size=1")
    options.add_argument("disk-cache-size=1")
    options.add_argument("user-agent=admin")
    browser = webdriver.Chrome(
        "chromedriver",
        options=options,
        service_args=["--verbose", "--log-path=/tmp/chromedriver.log"],
    )

    browser.get("http://127.0.0.1:1337/")

    browser.add_cookie({"name": "flag", "value": FLAG})

    try:
        page_url = f"http://127.0.0.1:1337/preview?url={url}&title={title}"
        print(page_url)
        browser.get(page_url)
        WebDriverWait(browser, 5).until(
            lambda r: r.execute_script("return document.readyState") == "complete"
        )
    except Exception as e:
        print(e)
    finally:
        browser.quit()
