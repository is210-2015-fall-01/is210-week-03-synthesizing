#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

OLDWORD = len('Spanish')
LENGTH = len(inquisition.SPANISH)
COUNT = inquisition.SPANISH.index('Spanish')
START = inquisition.SPANISH[0:19]
END = inquisition.SPANISH[-392:]
FLEMISH = START + 'Flemish' + END
