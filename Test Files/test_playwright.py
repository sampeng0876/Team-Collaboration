from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill("斗破苍穹")
    page.get_by_placeholder("Search").press("Enter")
    page.get_by_role("link", name="【斗破苍穹年番】超前爆料 | 第44话 💥给老师报仇，战韩枫！ 1080P | Battle Through the Heavens #斗破苍穹 by 动漫嗨翻天 2 hours ago 1 minute, 4 seconds 5,227 views").click()
    page.get_by_role("button", name="Skip Ad").click()
    page.get_by_role("button", name="Dismiss").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
