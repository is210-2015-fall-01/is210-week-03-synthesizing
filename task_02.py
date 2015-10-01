#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

REPLACE = 'Spanish'

LENGTH_REPLACE = len(REPLACE)

START = inquisition.SPANISH.index(REPLACE)

END = inquisition.SPANISH.index(REPLACE) + LENGTH_REPLACE

BEGINING = inquisition.SPANISH[0:START]

ENDING = inquisition.SPANISH[END:]

FLEMISH = BEGINING + 'Flemish' + ENDING
