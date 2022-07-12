from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    #browser = playwright.chromium.launch()
    context = browser.new_context()

    page = context.new_page()
    #page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://unimedjp.blip.ai/application/detail/telessaudeunimedjoaopessoa/analytics/dashboard")

    page.goto("https://unimedjp.blip.ai/login")

    page.goto("https://account.blip.ai/login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dblip-portal%26redirect_uri%3Dhttps%253A%252F%252Funimedjp.blip.ai%252Fauthorize%26response_type%3Did_token%2520token%26scope%3Doffline_access%2520openid%2520profile%2520email%2520api-msging-hub.full_access%2520api-payment-service.full_access%26state%3D479aac861a904912b6238ab38b125bfc%26nonce%3D14e15551ac9f4fc7894bb04dc7bc5058")

    page.locator("input[name=\"Username\"]").click()

    page.locator("input[name=\"Username\"]").fill("CREDENTIALUSERNAME")

    page.locator("input[name=\"Password\"]").click()

    page.locator("input[name=\"Password\"]").fill("CREDENTIALPASSWORD")

    page.locator("text=ou").click()

    page.locator("text=Entrar").click()

    page.goto("https://unimedjp.blip.ai/application/detail/telessaudeunimedjoaopessoa/analytics/dashboard")

    page.locator('id=7days').click()

    page.wait_for_timeout(20000)

    page.screenshot(path=f"./screenshots/dashboard_telessaude_{datetime.now().strftime('%d-%m-%Y_%H%M%S')}.png", full_page=True)

    page.locator("user-menu item-title >> text=NOMEDOINDIVIDUOLOGADO").click()

    page.locator("text=Sair").click()

    page.goto(
        "https://account.blip.ai/login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dblip-portal%26redirect_uri%3Dhttps%253A%252F%252Funimedjp.blip.ai%252Fauthorize%26response_type%3Did_token%2520token%26scope%3Doffline_access%2520openid%2520profile%2520email%2520api-msging-hub.full_access%2520api-payment-service.full_access%26state%3Da7e97765dc7a47328f0c6ed218c6b492%26nonce%3D436b62973e7f43e1ac08063812687d46")

    page.locator("text=ou").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
