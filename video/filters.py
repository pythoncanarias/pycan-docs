#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import re

_slugify_mapa = {
     10: 45,    # Carriage return -> hyphen
     13: 45,    # Line feed -> hyphen
     32: 45,    # space -> hyphen 
     33: None,  # exclamation mark
     34: None,  # double quotes
     35: None,  # hash
     36: None,  # dollar
     37: None,  # percent
     38: None,  # ampersand
     39: None,  # simple quote
     40: None,  # open par
     41: None,  # close par
     42: None,  # asterisk
     43: 45,    # plus -> hyphen
     44: None,  # comma
     46: None,  # dot or full stop
     47: 45,    # slash -> hyphen
     58: 45,    # colon -> hyphen
     59: 45,    # semicolon -> hyphen
     60: None,  # open angled bracket
     61: 45,    # equals -> hyphen
     62: None,  # close angled bracket
     63: None,  # question mark
     64: 45,    # @ -> hyphen
     91: None,  # open bracket
     92: 45,    # backslash -> hyphen
     93: None,  # close bracket
     94: 45,    # caret -> hyphen
     95: 45,    # underscore -> hyphen
     96: None,  # grave accent
    123: None,  # open brace
    124: 45,    # pipe -> hyphen
    125: None,  # close brace
    126: 45,    # equivalency sign (~) -> hyphen
    133: 45,    # ellipsis 
    191: None,  # open question mark
    193: 65,
    201: 69,
    205: 73,
    209: 78,
    211: 79,
    218: 85,
    220: 85,
    225: 97,  # a
    233: 101,
    237: 105,
    241: 110,
    243: 111,
    250: 117,
    252: 117,
    8230: 45   # ellipsis
    }

_slugify_pat_multiple_hyphens = re.compile('--+')

def slugify(s):
    global _slugify_pat_multiple_hyphens, _slugify_mapa
    s = s.lower()
    s = s.replace('ñ', 'ni')
    s = s.replace('€', '-euros')
    # logger.debug('s antes   = "{}"'.format(s))
    s = s.translate(_slugify_mapa)
    # logger.debug('s después = "{}"'.format(s))
    s = ''.join([_ for _ in s if ord(_) < 129])
    s = _slugify_pat_multiple_hyphens.sub('-', s)
    return s
