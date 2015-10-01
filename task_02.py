#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

REPLACE = 'Spanish'
START = inquisition.SPANISH.index('Spanish')
END = int(START) + len(REPLACE)
PART1 = inquisition.SPANISH[:START]
PART2 = inquisition.SPANISH[END:]
FLEMISH = PART1 + 'Flemish' + PART2
