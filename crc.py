from zlib import crc32

def getCRC32(filename):
    with open(filename, 'rb') as f:
        return crc32(f.read())

def getCRC32line(filename, len):
    f = open(filename, 'rb')
    data = f.read(len)
    while(data):
        print '0x%x' % (crc32(data) & 0xffffffff)
        print '\n'
        f.seek(len, 1)
        data = f.read(len)
    f.close()
    return crc32(data)

print 'CRC data is 0x%x'% getCRC32(r'E:/Programma Study/HTML/htmlTest.html')

print 'line CRC data is 0x%x' % getCRC32line(r'E:/Programma Study/HTML/htmlTest.html', 40)
