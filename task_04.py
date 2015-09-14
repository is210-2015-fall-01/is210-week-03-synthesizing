#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
A = '{:06d}'.format(RNUM)
EMAIL = NEWS.format(NTYPE, A, friend=FNAME)
print EMAIL
