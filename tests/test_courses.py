from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        email_input.fill('testtest@ya.ru')
        user_name_input.fill('test')
        password_input.fill('testpassword')
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        context_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(context_header).to_be_visible()
        expect(context_header).to_have_text('Courses')
        block_result = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(block_result).to_be_visible()
        expect(block_result).to_have_text('There is no results')
        icon_block = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_block).to_be_visible()
        block_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(block_text).to_be_visible()
        expect(block_text).to_have_text('Results from the load test pipeline will be displayed here')
