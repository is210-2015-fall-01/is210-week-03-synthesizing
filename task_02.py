#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPANISH = inquisition.SPANISH
S = SPANISH.index('Spanish', 1)
P = len('Spanish')
A = len(SPANISH)
FLEMISH = SPANISH[0:S] + 'Flemish' + SPANISH[S+P:A]

print FLEMISH
