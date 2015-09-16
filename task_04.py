#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
RNUM = 42
A = ('{0:06d}'.format(RNUM))
EMAIL = NEWS.format('*amazing*', A, friend='Pat')
print EMAIL

# RNUM = 42
# A = '{0:06d}'.format(RNUM)
# FNAME = 'Pat'
# NTYPE = '*amazing*'
# A = '{0:06d}'.format(RNUM)
# When I replace 42 with 5678, I get the correct 005678, just like the
# nosetests says I should get. Nosetest passed!!! Yay.
