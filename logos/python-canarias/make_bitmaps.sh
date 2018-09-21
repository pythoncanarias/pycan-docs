#!/usr/bin/env bash

function realpath()
{
    f=$@
    if [ -d "$f" ]; then
        base=""
        dir="$f"
    else
        base="/$(basename "$f")"
        dir=$(dirname "$f")
    fi
    dir=$(cd "$dir" && /bin/pwd)
    echo "$dir$base"
}

base_dir=$(dirname $(realpath $0))

# Color (with letters)

fn=logo-python-canarias-color
src=$base_dir/$fn
tgt=$base_dir/bitmaps/$fn

inkscape --file $src.svg  --export-png $tgt-372x128.png --export-width=372 --export-height=128 
inkscape --file $src.svg  --export-png $tgt-744x256.png --export-width=744 --export-height=256 
inkscape --file $src.svg  --export-png $tgt-1116x384.png --export-width=1116 --export-height=384 
inkscape --file $src.svg  --export-png $tgt-1488x512.png --export-width=1488 --export-height=512 

# Color (solo)

fn=logo-python-canarias-color-solo
src=$base_dir/$fn
tgt=$base_dir/bitmaps/$fn

inkscape --file $src.svg  --export-png $tgt-64x64.png --export-width=64 --export-height=64 
inkscape --file $src.svg  --export-png $tgt-128x128.png --export-width=128 --export-height=128 
inkscape --file $src.svg  --export-png $tgt-256x256.png --export-width=256 --export-height=256 
inkscape --file $src.svg  --export-png $tgt-512x512.png --export-width=512 --export-height=512 
inkscape --file $src.svg  --export-png $tgt-1024x1024.png --export-width=1024 --export-height=1024 

# Black on white (with letters)

fn=logo-python-canarias-black-on-white
src=$base_dir/$fn
tgt=$base_dir/bitmaps/$fn

inkscape --file $src.svg  --export-png $tgt-372x128.png --export-width=372 --export-height=128 
inkscape --file $src.svg  --export-png $tgt-744x256.png --export-width=744 --export-height=256 
inkscape --file $src.svg  --export-png $tgt-1116x384.png --export-width=1116 --export-height=384 
inkscape --file $src.svg  --export-png $tgt-1488x512.png --export-width=1488 --export-height=512 

# Black on white (solo)

fn=logo-python-canarias-black-on-white-solo
src=$base_dir/$fn
tgt=$base_dir/bitmaps/$fn

inkscape --file $src.svg  --export-png $tgt-64x64.png --export-width=64 --export-height=64 
inkscape --file $src.svg  --export-png $tgt-128x128.png --export-width=128 --export-height=128 
inkscape --file $src.svg  --export-png $tgt-256x256.png --export-width=256 --export-height=256 
inkscape --file $src.svg  --export-png $tgt-512x512.png --export-width=512 --export-height=512 
inkscape --file $src.svg  --export-png $tgt-1024x1024.png --export-width=1024 --export-height=1024 

# White on black (with letters)

fn=logo-python-canarias-white-on-black
src=$base_dir/$fn
tgt=$base_dir/bitmaps/$fn

inkscape --file $src.svg  --export-png $tgt-372x128.png --export-width=372 --export-height=128 
inkscape --file $src.svg  --export-png $tgt-744x256.png --export-width=744 --export-height=256 
inkscape --file $src.svg  --export-png $tgt-1116x384.png --export-width=1116 --export-height=384 
inkscape --file $src.svg  --export-png $tgt-1488x512.png --export-width=1488 --export-height=512 

# White on black (solo)

fn=logo-python-canarias-white-on-black-solo
src=$base_dir/$fn
tgt=$base_dir/bitmaps/$fn

inkscape --file $src.svg  --export-png $tgt-64x64.png --export-width=64 --export-height=64 
inkscape --file $src.svg  --export-png $tgt-128x128.png --export-width=128 --export-height=128 
inkscape --file $src.svg  --export-png $tgt-256x256.png --export-width=256 --export-height=256 
inkscape --file $src.svg  --export-png $tgt-512x512.png --export-width=512 --export-height=512 
inkscape --file $src.svg  --export-png $tgt-1024x1024.png --export-width=1024 --export-height=1024 

