import subprocess
from pathlib import Path
import yaml


class SvgLogo():
    def __init__(self, svg_path, width, height, output_path):
        self.width, self.height = width, height
        self.svg_path = Path(svg_path)
        file = f'{self.svg_path.stem}-{self.width}x{self.height}.png'
        self.png_path = output_path / file

    def topng(self):
        subprocess.call(
            f'inkscape --file {self.svg_path} --export-png {self.png_path} \
                --export-width={self.width} --export-height={self.height}',
            shell=True
        )


def build():
    with open('config.yaml') as f:
        try:
            config = yaml.load(f)
        except yaml.YAMLError as err:
            print(err)
    cwd = Path('.')
    output_path = cwd / config.get('output_dir', 'bitmaps')
    output_path.mkdir(exist_ok=True)

    for file in cwd.glob('*.svg'):
        if file.stem.endswith('solo'):
            sizes = config['bitmap_sizes']['solo']
        else:
            sizes = config['bitmap_sizes']['full']
        for size in sizes:
            logo = SvgLogo(file, *size, output_path)
            logo.topng()


if __name__ == '__main__':
    build()
