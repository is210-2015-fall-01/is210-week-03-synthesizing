#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
EMAIL = NEWS.format('*amazing*', '{:06d}'.format(42), friend='Pat')
print EMAIL

# RNUM = 42
# A = '{:06d}'.format(RNUM)
# FNAME = 'Pat'
# NTYPE = '*amazing*'
