# Main Concept

- Steganography
- Brute Forcing

## Explanation

This challenge involves **steganography** using `magick`. The commands related to enciphering and deciphering can be found in the official documentation at [usage.imagemagick.org](https://usage.imagemagick.org/transform/#stegano).

```sh
# Enciphering
magick composite build/message.gif mikumikubeam.png -stegano $offset build/mikumikusteg.png
# Deciphering
magick -size $msgsize$offset stegano:$steg_img ${output_dir}/${width}x${height}_${x}_${y}.gif
```

Although I am not very familiar with magick, testing various width, height, and offset values revealed the following patterns:

1. When `x=0`, the hidden text becomes visible if the width is a multiple of a specific value.
2. The height affects how the hidden text is divided, appearing in `height * n` segments.
3. Offset x also follows a specific multiple pattern, making the hidden text readable.
4. Offset y has little impact on readability.

Using these observations, I brute-forced width, height, and x values on `mikumikusteg.png` to recover the flag.
