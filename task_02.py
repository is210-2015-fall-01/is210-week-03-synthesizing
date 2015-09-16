#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

INDEX_SPANISH = inquisition.SPANISH.index('Spanish')
LEN_SPANISH = len('Spanish')
SLICE_IN = inquisition.SPANISH[0:INDEX_SPANISH]
SLICE_LE = inquisition.SPANISH[INDEX_SPANISH + LEN_SPANISH:]
FLEMISH = SLICE_IN + 'Flemish' + SLICE_LE

print FLEMISH
