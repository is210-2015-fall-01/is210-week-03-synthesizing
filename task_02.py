#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FIRST = inquisition.SPANISH.index('Spanish')
SECOND = len('Spanish')
THIRD = inquisition.SPANISH[:FIRST]
FOURTH = inquisition.SPANISH[(FIRST+SECOND):]
FIFTH = 'Flemish'
FLEMISH = str(THIRD) + str(FIFTH) + str(FOURTH)
