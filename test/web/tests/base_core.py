from __future__ import absolute_import

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import manage

from manage import app as testapp

from app import app

import unittest


class BaseCore(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()
