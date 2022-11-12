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

img_part = Image.open('part.png').convert('RGBA')
img_out = Image.open('out.png').convert('RGBA')

random.seed(time.time())

px_part = img_part.load()
px_out = img_out.load()
print(px_part)
x_len, y_len = img_part.size

new = Image.new('RGBA', (x_len, y_len), 'white')
new.show()
px1 = new.load()

for y in range(0, 1):
    for x in range(0, 624):
        in_r, in_g, in_b, in_a = xor_tuple(px_part[x,y], px_out[x,y])

        rand_number = rgba2int((in_r, in_g, in_b, in_a))
        rc.submit(rand_number)
        print(rand_number)
        # rand = random.getrandbits(32)
        # rr, rg, rb, ra = int2rgba(rand)
        # xyz = px_part[x, y]
        # # print(f'{x=} {y=}  {xyz}')
        # r, g, b, a = xyz
        # new_pix = xor_tuple((rr, rg, rb, ra), (r, g, b, a))
#         px1[x, y] = new_pix
#
# new.save('in.png')
for y in range(0, 1):
    for x in range(624, x_len):
        rand = rc.predict_getrandbits(32)
        # print()
        print(rand)
        rr, rg, rb, ra = int2rgba(rand)
        xyz = px_out[x, y]
        # print(f'{x=} {y=}  {xyz}')
        r, g, b, a = xyz
        new_pix = xor_tuple((rr, rg, rb, ra), (r, g, b, a))
        px1[x, y] = new_pix

for y in range(1, y_len):
    for x in range(x_len):
        rand = rc.predict_getrandbits(32)
        # print()
        print(rand)
        rr, rg, rb, ra = int2rgba(rand)
        xyz = px_out[x, y]
        # print(f'{x=} {y=}  {xyz}')
        r, g, b, a = xyz
        new_pix = xor_tuple((rr, rg, rb, ra), (r, g, b, a))
        px1[x, y] = new_pix

new.save('in.png')
