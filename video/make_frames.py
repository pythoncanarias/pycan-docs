#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
from filters import slugify

def make_png(template, titulo, tag):
    with open('salida.svg', 'w') as f:
        f.write(template.replace('{{titulo}}', titulo))
    filename = '{}-{}.png'.format(slugify(titulo), tag)
    subprocess.call([
        'inkscape',
        'salida.svg',
        '--export-png={}'.format(filename),
        '--export-dpi=90',
        ])
    os.unlink('salida.svg')


with open('charlas.txt', 'r') as f:
    titulos = [x.strip() for x in f.readlines() if x.strip()]

with open('frame-video-4-3.svg', 'r') as f:
    template_4_3 = f.read()

with open('frame-video-16-9.svg', 'r') as f:
    template_16_9 = f.read()

for titulo in titulos:
    print('generando frames charla {}'.format(titulo), end=' ')
    make_png(template_4_3, titulo, '4-3')
    make_png(template_16_9, titulo, '16-9')
    print('[OK]')



