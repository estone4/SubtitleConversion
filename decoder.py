import codecs

input_file = open('A.Walk.to.Remember.2002.720p.BluRay.x264.YIFY 2.srt', 'rb')
raw_bytes = input_file.read()

print(raw_bytes)

unicode_byte_count = 0
unicode_index = []
mask = 0x80

for byte in raw_bytes:
    if mask & byte:
        print("high bit set for %c" % byte)
        if mask >> 1 & byte:
            print("Found 2nd high bit")
            if mask >> 2 & byte:
                print("3rd high bit set")
            else:
                print("3rd high bit NOT set")
        unicode_byte_count += 1
        unicode_index.append(byte)

print(unicode_byte_count)
# print(unicode_index)

# try:
#     decoded_bytes = str(raw_bytes.decode('utf-8'))
# except Exception as e:
#     print('Error decoding file as "UTF-8"!\n')
#     print(e)
#     print('Decoding file as "ISO-8859-9"\n')
#     decoded_bytes = str(raw_bytes.decode('iso-8859-9'))
#
# if decoded_bytes is not None:
#     print(decoded_bytes)
