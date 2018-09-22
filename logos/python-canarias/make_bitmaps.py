import subprocess
from pathlib import Path


FULL_BITMAP_SIZES = (
    (372, 128),
    (744, 256),
    (1116, 384),
    (1488, 512)
)

SOLO_BITMAP_SIZES = (
    (64, 64),
    (128, 128),
    (256, 256),
    (512, 512),
    (1024, 1024)
)


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


def build(output_dir='bitmaps'):
    cwd = Path('.')
    output_path = cwd / output_dir
    output_path.mkdir(exist_ok=True)

    for file in cwd.glob('*.svg'):
        if file.stem.endswith('solo'):
            sizes = SOLO_BITMAP_SIZES
        else:
            sizes = FULL_BITMAP_SIZES
        for size in sizes:
            logo = SvgLogo(file, *size, output_path)
            logo.topng()


if __name__ == '__main__':
    build()
