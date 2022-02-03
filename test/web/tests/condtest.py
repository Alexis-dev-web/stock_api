from __future__ import absolute_import

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import manage

from manage import app as testapp

import pytest


@pytest.fixture
def app():
    yield testapp
    return testapp


@pytest.fixture
def client(app):
    return app.test_client()
