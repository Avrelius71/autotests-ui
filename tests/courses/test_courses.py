from pathlib import Path

import pytest
from pages.courses.create_courses_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage

IMAGE_FILE = Path(__file__).resolve().parents[2] / "testdata" / "files" / "image.png"


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_create_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            description="",
            estimated_time="",
            max_score="0",
            min_score="0"
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
        create_course_page.image_upload_widget.upload_preview_image(str(IMAGE_FILE))
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index='0',
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page.image_upload_widget.upload_preview_image(str(IMAGE_FILE))
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.menu.click_edit(0)
        create_course_page.create_course_form.fill(
            title="Playwright-test",
            estimated_time="3 weeks",
            description="Playwright-test",
            max_score="200",
            min_score="20"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index='0',
            title="Playwright-test",
            estimated_time="3 weeks",
            max_score="200",
            min_score="20"
        )

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
        )
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()
        courses_list_page.navbar.check_visible("test")
        courses_list_page.sidebar.check_visible()