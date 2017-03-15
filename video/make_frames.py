#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
from filters import slugify

with open('charlas.txt', 'r') as f:
    titulos = [x.strip() for x in f.readlines()]

with open('frame-video-4-3.svg', 'r') as f:
    template = f.read()

for titulo in titulos:
    print('generando frame charla {}'.format(titulo), end=' ')
    salida = template.replace('{{titulo}}', titulo)
    with open('salida.svg', 'w') as f:
        f.write(salida)
    filename = '{}.png'.format(slugify(titulo))
    subprocess.call([
        'inkscape',
        'salida.svg',
        '--export-png={}'.format(filename),
        '--export-dpi=90',
        ])
    os.unlink('salida.svg')
    print('[OK]')



