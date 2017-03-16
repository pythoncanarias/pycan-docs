#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import subprocess
import os
from filters import slugify
import json


def load_charlas():
    with open('charlas.json') as f:
        charlas = json.load(f)
    return charlas


def make_png(template, data):
    data['pwd'] = os.getcwd()
    titulo = data['titulo']
    with open('salida.svg', 'w') as f:
        for key in data:
            template = template.replace(
                '{{%s}}' % key, 
                data[key]
                )
        f.write(template)
    filename = 'entradilla-{}.png'.format(slugify(titulo))
    subprocess.call([
        'inkscape',
        'salida.svg',
        '--export-png={}'.format(filename),
        '--export-dpi=90',
        ])
    os.unlink('salida.svg')
    return filename

with open('entradilla-master.svg', 'r') as f:
    template = f.read()

charlas = load_charlas()
for (i, charla) in enumerate(charlas):
    titulo = charla['titulo']
    print('generando entradilla charla {}'.format(titulo), end=' ')
    print(make_png(template, charla), end=' ')
    print('[OK]')



