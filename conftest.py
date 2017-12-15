# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseURL')
    if fixture is None:
        fixture = Application(browser, base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser, base_url)
    fixture.session.ensure_login(login="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseURL', action='store', default='http://localhost/addressbook/')
