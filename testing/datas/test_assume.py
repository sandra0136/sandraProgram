#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest


def test_a():
    pytest.assume(1 == 2)
    pytest.assume(False == True)
    pytest.assume(200 == 200)
