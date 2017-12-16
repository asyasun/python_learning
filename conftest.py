# -*- coding: utf-8 -*-
import pytest
import json
import os.path
from fixture.Application import Application

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
    if target is None:
        with open(config_file) as f:
            target = json.load(f)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseURL'])
    fixture.session.ensure_login(login=target['login'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')
