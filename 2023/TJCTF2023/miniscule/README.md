# miniscule

## Flag
tjctf{zlib_compression_bad_9c8b342}

## Solution

The PNG file cannot be opened, so we use `pngcheck` for seeing the error message and see that "compression method" is set to an invalid value.

From http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html:
> Compression method is a single-byte integer that indicates the method used to compress the image data. At present, only compression method 0 (deflate/inflate compression with a sliding window of at most 32768 bytes) is defined. All standard PNG images must be compressed with this scheme. The compression method field is provided for possible future expansion or proprietary variants. Decoders must check this byte and report an error if it holds an unrecognized code. See Deflate/Inflate Compression for details.

We use a hex editor to change the value of "compression method" to 0 and also set the CRC32 value according to the error message shown by `pngcheck`.
However, we can still not open the file, since the compressed stream contains invalid data.

Then, we use the following Python script for extracting the compressed stream:

```Python
import zlib

image = open('miniscule.png', 'rb').read()

ihdr_index = image.find(b'IHDR')
idat_index = image.find(b'IDAT')
length = int.from_bytes(image[idat_index-4:idat_index], byteorder='big')

data = image[idat_index+4:idat_index+4+length]
open('compressed_data', 'wb').write(data)
```

We use the following command for knowing the format of the compressed stream:
```shell
file compressed_data
compressed_data: Zstandard compressed data (v0.8+), Dictionary ID: None
```

We rename the file "compressed_data" to "compressed_data.zst" and execute the following command `unzstd compressed_data.zst -o decompressed_data`.

Now, we use the following Python script for correcting the values in the IHDR chunk, compressing the data correctly
and inserting it in the IDAT header with the correct CRC32 value.
Then, we can open the image and find the flag.

```
import zlib

image = open('miniscule.png', 'rb').read()
ihdr_index = image.find(b'IHDR')
idat_index = image.find(b'IDAT')
length = int.from_bytes(image[idat_index-4:idat_index], byteorder='big')

decompressed_data = open('decompressed_data', 'rb').read()
data = zlib.compress(decompressed_data)
idat = b'IDAT'+data
idat += int.to_bytes(zlib.crc32(idat), length=4, byteorder='big')
image = image[0:idat_index-4]+int.to_bytes(len(data), length=4, byteorder='big')+idat+image[idat_index+8+length:len(image)]

image = image[0:ihdr_index+14]+b'\x00'+image[ihdr_index+15:len(image)]
crc32 = int.to_bytes(zlib.crc32(image[ihdr_index:ihdr_index+17]), length=4, byteorder='big')
image = image[0:ihdr_index+17]+crc32+image[ihdr_index+21:len(image)]
open('image.png', 'wb').write(image)
```
