#!/bin/sh
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "Script dir: $SCRIPT_DIR"
steg_img=$SCRIPT_DIR/mikumikusteg.png
output_dir="build"

mkdir -p ${output_dir}1
mkdir -p ${output_dir}2
mkdir -p ${output_dir}3
mkdir -p ${output_dir}4

# img height, width = (331, 842)

# Find width // multiples of 96
height=331
x=0
y=0
for width in $(seq 30 1 100); do
    msgsize="${width}x${height}"

    offset="+${x}+${y}"

    echo "Trying size: $msgsize, offset: $offset"
    magick -size $msgsize$offset stegano:$steg_img ${output_dir}1/${width}x${height}_${x}_${y}.gif
done

# Find exact width // 192
height=331
x=0
y=0
for width in $(seq 96 96 842); do
    msgsize="${width}x${height}"

    offset="+${x}+${y}"

    echo "Trying size: $msgsize, offset: $offset"
    magick -size $msgsize$offset stegano:$steg_img ${output_dir}2/${width}x${height}_${x}_${y}.gif
done

# Find exact height // 115
width=192
x=0
y=0
for height in $(seq 100 1 150); do
    msgsize="${width}x${height}"
    offset="+${x}+${y}"

    echo "Trying size: $msgsize, offset: $offset"
    magick -size $msgsize$offset stegano:$steg_img ${output_dir}3/${width}x${height}_${x}_${y}.gif
done

# Find exact x // multiples of 3
# x = 51
width=192
height=115
for x in $(seq 0 1 100); do
    msgsize="${width}x${height}"

    y=0
    offset="+${x}+${y}"

    echo "Trying size: $msgsize, offset: $offset"
    magick -size $msgsize$offset stegano:$steg_img ${output_dir}4/${width}x${height}_${x}_${y}.gif
done