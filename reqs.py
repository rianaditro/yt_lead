from playwright.sync_api import sync_playwright

import time


def do(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 1080})
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.keyboard.press("End")
        time.sleep(3)
        browser.close()


if __name__ == "__main__":
    url = "https://www.youtube.com/results?search_query=real+estate&sp=CAMSAhAC"
    do(url)