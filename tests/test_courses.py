from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    context_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(context_header).to_be_visible()
    expect(context_header).to_have_text('Courses')
    block_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_result).to_be_visible()
    expect(block_result).to_have_text('There is no results')
    icon_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_block).to_be_visible()
    block_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_text).to_be_visible()
    expect(block_text).to_have_text('Results from the load test pipeline will be displayed here')
