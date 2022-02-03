import os
import pytest


def test_health(client):
  response = client.get("/")
  assert response.data == b'{"hello":"server up"}\n'