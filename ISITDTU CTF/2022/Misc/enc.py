from PIL import Image
import random, time
from randcrack import RandCrack
rc = RandCrack()


def xor(a):
    return a[0] ^ a[1]


def xor_tuple(a, b):
    return tuple(i for i in map(xor, zip(*[a, b])))


def rgba2int(rgba: tuple):
    ret = 0
    for i in range(3, -1, -1):
        ret += rgba[i] << 8 * (3 - i)
    return ret


def int2rgba(n):
    r, g, b, a = tuple([(n >> 8 * i) & 0xff for i in range(3, -1, -1)])
    return (r, g, b, a)

# def getrandint(rgba: tuple, rgbax:tuple):
#     for i in range(3, -1, -1):

img = Image.open('flag.png').convert('RGBA')
print(img)

random.seed(time.time())

px = img.load()
print(px)
x_len, y_len = img.size

new = Image.new('RGBA', (x_len, y_len), 'white')
new.show()
px1 = new.load()
for i in range(624):
    rc.submit(random.getrandbits(32))

for y in range(y_len):
    for x in range(x_len):
        rand = random.getrandbits(32)
        print(rc.predict_getrandbits(32))
        print(rand)
        rr, rg, rb, ra = int2rgba(rand)
        print(rgba2int((rr, rg, rb, ra)))
        xyz = px[x, y]
        # print(f'{x=} {y=}  {xyz}')
        r, g, b, a = xyz
        new_pix = xor_tuple((rr, rg, rb, ra), (r, g, b, a))
        px1[x, y] = new_pix

new.save('out.png')
