#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPANISH = "Spanish"

SPANISH_START = inquisition.SPANISH.index(SPANISH)
SPANISH_END = SPANISH_START + len(SPANISH)
BEGINNING = inquisition.SPANISH[0:SPANISH_START]
ENDING = inquisition.SPANISH[SPANISH_END:]
FLEMISH = BEGINNING + "Flemish" + ENDING
