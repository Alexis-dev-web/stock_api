from __future__ import absolute_import

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import manage

from manage import app as testapp, db

from app import app

import unittest


class BaseCase(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()
    self.db = db
    self.db.create_all()
    self.db.session.commit()

  def tearDown(self):
    # Delete Database collections after the test is complete
    self.db.session.remove()
    self.db.drop_all()