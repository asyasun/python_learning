# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
