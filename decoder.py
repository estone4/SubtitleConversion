import codecs

input_file = open('A.Walk.to.Remember.2002.720p.BluRay.x264.YIFY 2.srt', 'rb')
raw_bytes = input_file.read()

print(raw_bytes)

try:
    decoded_bytes = str(raw_bytes.decode('utf-8'))
except Exception as e:
    print('Error decoding file as "UTF-8"!\n')
    print(e)
    print('Decoding file as "ISO-8859-9"\n')
    decoded_bytes = str(raw_bytes.decode('iso-8859-9'))

if decoded_bytes is not None:
    print(decoded_bytes)
