#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""


NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1:0>6}!'
EMAIL = NEWS.format(NTYPE, RNUM, friend='Pat')
print EMAIL
