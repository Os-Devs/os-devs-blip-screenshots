from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # browser = playwright.chromium.launch()
    context = browser.new_context()

    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://unimedjp.blip.ai/login")

    page.wait_for_timeout(30000)

    page.locator("input[name=\"Username\"]").click()

    page.locator("input[name=\"Username\"]").fill("CREDENTIALUSERNAME")

    page.locator("input[name=\"Password\"]").click()

    page.locator("input[name=\"Password\"]").fill("CREDENTIALPASSWORD")

    page.locator("text=ou").click()

    page.locator("text=Entrar").click()

    page.wait_for_timeout(30000)

    page.goto("https://unimedjp.blip.ai/application/detail/telessaudeunimedjoaopessoa/analytics/dashboard")

    page.locator('id=7days').click()

    page.wait_for_timeout(30000)

    page.screenshot(path=f"./screenshots/dashboard_telessaude_{datetime.now().strftime('%d-%m-%Y_%H%M%S')}.png", full_page=True)

    page.locator("user-menu item-title >> text=NOMEDOINDIVIDUOLOGADO").click()

    page.locator("text=Sair").click()

    page.locator("text=ou").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
