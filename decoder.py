import codecs
import os

#print(os.sys.platform)

input_file = open('Test2.srt', 'rb')
byte = input_file.read(1).decode()

mask = b"0x80"
while byte:
    if byte & mask.decode():
        print("High bit set for {}.".format(byte))

#print(raw_bytes)

unicode_byte_count = 0
unicode_index = []
byte_index = 0  # Counts the number of bytes read to tack the location


# need to figure out how to check each byte to s

for byte in raw_bytes:
    print("Byte #: {0}".format(byte))
    byte_index += 1
    if mask & byte:  # checks if the byte starts with the left most bit (bit 7) set  (This should indicate unicode)
        print("high bit set for {0} at pos: {1}".format(byte, byte_index))
        if mask >> 1 & byte:  # should be checking if bit 6 is also set
            # (This lets us know how many remaining bytes to look for the rest of the unicode
            print("Found 2nd high bit for %c at pos: %d" % (byte, byte_index))
            if mask >> 2 & byte:  # should be checking if bit 5 is set
                print("3rd high bit set")
            else:
                print("3rd high bit NOT set")
        unicode_byte_count += 1
        unicode_index.append(byte_index)

print(unicode_byte_count)
print(unicode_index)
# print(unicode_index)
print("Byte index: %d" % byte_index)

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


if byte_index > len(raw_bytes):
    print("ERROR Reading file")
else:
    print(len(raw_bytes))
