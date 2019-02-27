#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

def get_page_data(num):
    offset = (num -1) * 10
    return  {
    'A1': offset + 1,
    'B1': offset + 2,
    'A2': offset + 3,
    'B2': offset + 4,
    'A3': offset + 5,
    'B3': offset + 6,
    'A4': offset + 7,
    'B4': offset + 8,
    'A5': offset + 9,
    'B5': offset + 10,
    }

with open('tickets-master.svg', 'r') as f:
    template = f.read()

for page in range(1, 13):
    print('generando página {}'.format(page), end=' ')
    data = get_page_data(page)
    salida = template
    for k in data:
        patron = '{{%s}}' % k
        salida = salida.replace(patron, str(data[k]))
    with open('salida.svg', 'w') as f:
        f.write(salida)
    subprocess.call([
        'inkscape',
        'salida.svg',
        '--export-pdf=tickets-{:02d}.pdf'.format(page),
        '--export-dpi=150',
        ])
    os.unlink('salida.svg')
    print('[OK]')








