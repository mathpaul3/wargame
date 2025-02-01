## 주요 개념

- File Format(PNG)

## 풀이

PNG의 구조를 알면 쉽게 해결할 수 있는 문제이다. [PNG Wikipedia](https://en.wikipedia.org/wiki/PNG)  
Hex editor를 통해 png 파일의 height 속성을 2배로 늘려준다.

- PNG Signature (8bytes): `89504E47 0D0A1A0A`

- IHDR Chunk Length (4bytes; Chunk Name 제외 길이): `0D (13)`
- IHDR(Header) Chunk

  - Chunk Name (4bytes): `49484452 (IHDR)`
  - Chunk Data
    - Width (4bytes)
    - Height (4bytes)
    - Bit Depth (1byte) `values 1, 2, 4, 8, or 16`
    - Color Type (1byte) `values 0, 2, 3, 4, or 6`
    - Compression Method (1byte): `00`
    - Filter Method (1byte): `00`
    - Interlace Method (1byte): `00`
  - Chunk CRC (4byte; Chunk Name 포함)

- IDAT Chunk Length (4bytes; Chunk Name 제외 길이)
- IDAT(Data) Chunk

  - Chunk Name (4bytes): `49444154 (IDAT)`
  - Compression Method:
    - DEFLATE Compression Method (1byte)
    - ZLIB FCHECK value (1byte)
  - Chunk Data
    - ...
  - ZLIB check value (4bytes)
  - Chunk CRC (4bytes; Chunk Name 포함)

- IEND Chunk Length (4bytes; Chunk Name 제외 길이): `0`
- IEND
  - Chunk Name (4bytes): `49454E44 (IEND)`
  - Chunk CRC (4bytes; Chunk Name 포함): `AE426082`

CRC 알고리즘: **CRC-32/ISO-HDLC**
