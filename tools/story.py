from enum import Enum


class AllureStory(str, Enum):
    AUTHORIZATION = 'Authorization'
    REGISTRATION = 'Registration'
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
