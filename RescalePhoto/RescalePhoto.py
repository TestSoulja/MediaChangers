import os
from PIL import Image

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), "")

q = 4

n1 = 128
n2 = 256
n3 = 240
n4 = 480
n5 = 108
n6 = 81
n7 = 192
n8 = 144
n9 = 96
n10 = 72
n11 = 48
n12 = 36
n13 = 87
n14 = 58
n15 = 29
n16 = 60
n17 = 40
n18 = 20
n19 = 102
n20 = 192
n21 = 1024
n23 = 324
n24 = 216
n25 = 162
n26 = 108
n27 = 1024
n28 = 1024
n29 = 216
n30 = 162
n31 = 108
n32 = 1024
n33 = 1024

m1 = 1334
m1_1 = 750
m2 = 1136
m2_1 = 640
m3 = 1920
m3_1 = 1080

m4 = 1024
m4_1 = 1024
m5 = 108
m5_1 = 108
m6 = 60
m6_1 = 60
m7 = 72
m7_1 = 72
m8 = 76
m8_1 = 76
m9 = 80
m9_1 = 80
m10 = 87
m10_1 = 87
m11 = 114
m11_1 = 114
m12 = 120
m12_1 = 120
m13 = 144
m13_1 = 144
m14 = 152
m14_1 = 152
m15 = 167
m15_1 = 167
m16 = 180
m16_1 = 180
m17 = 1024
m17_1 = 1024
m18 = 157
m18_1 = 157
m19 = 180
m19_1 = 180
m20 = 192
m20_1 = 192
m21 = 1024
m21_1 = 1024
m22 = 432
m22_1 = 432
m23 = 324
m23_1 = 324
m24 = 216
m24_1 = 216
m25 = 162
m25_1 = 162
m26 = 108
m26_1 = 108
m27 = 1024
m27_1 = 1024
m28 = 1024
m28_1 = 1024
m29 = 216
m29_1 = 216
m30 = 162
m30_1 = 162
m31 = 108
m31_1 = 108
m32 = 1024
m32_1 = 1024
m33 = 1024
m33_1 = 1024

image_path = c + '/1.png'

img = Image.open(image_path)

# для квадратов

for i in range(q+1):
    if i == 1:
        new_image = img.resize((n1, n1))
        n1= str(n1)
        new_image.save(c+"Exit/" + n1 + "x" + n1 + '.png')
    elif i == 2:
        new_image = img.resize((n2, n2))
        n2 = str(n2)
        new_image.save(c+"Exit/" + n2 + "x" + n2 + '.png')
    elif i == 3:
        new_image = img.resize((n3, n3))
        n3= str(n3)
        new_image.save(c+"Exit/" + n3 + "x" + n3 + '.png')
    elif i == 4:
        new_image = img.resize((n4, n4))
        n4= str(n4)
        new_image.save(c+"Exit/" + n4 + "x" + n4 + '.png')
    elif i == 5:
        new_image = img.resize((n5, n5))
        n5= str(n5)
        new_image.save(c+"Exit/" + n5 + "x" + n5 + '.png')
    elif i == 6:
        new_image = img.resize((n6, n6))
        n6= str(n6)
        new_image.save(c+"Exit/" + n6 + "x" + n6 + '.png')
    elif i == 7:
        new_image = img.resize((n7, n7))
        n7= str(n7)
        new_image.save(c+"Exit/" + n7 + "x" + n7 + '.png')
    elif i == 8:
        new_image = img.resize((n8, n8))
        n8= str(n8)
        new_image.save(c+"Exit/" + n8 + "x" + n8 + '.png')
    elif i == 9:
        new_image = img.resize((n9, n9))
        n9= str(n9)
        new_image.save(c+"Exit/" + n9 + "x" + n9 + '.png')
    elif i == 10:
        new_image = img.resize((n10, n10))
        n10= str(n10)
        new_image.save(c+"Exit/" + n10 + "x" + n10 + '.png')
    elif i == 11:
        new_image = img.resize((n11, n11))
        n11= str(n11)
        new_image.save(c+"Exit/" + n11 + "x" + n11 + '.png')
    elif i == 12:
        new_image = img.resize((n12, n12))
        n12= str(n12)
        new_image.save(c+"Exit/" + n12 + "x" + n12 + '.png')
    elif i == 13:
        new_image = img.resize((n13, n13))
        n13= str(n13)
        new_image.save(c+"Exit/" + n13 + "x" + n13 + '.png')
    elif i == 14:
        new_image = img.resize((n14, n14))
        n14= str(n14)
        new_image.save(c+"Exit/" + n14 + "x" + n14 + '.png')
    elif i == 15:
        new_image = img.resize((n15, n15))
        n15= str(n15)
        new_image.save(c+"Exit/" + n15 + "x" + n15 + '.png')
    elif i == 16:
        new_image = img.resize((n16, n16))
        n16= str(n16)
        new_image.save(c+"Exit/" + n16 + "x" + n16 + '.png')
    elif i == 17:
        new_image = img.resize((n17, n17))
        n17= str(n17)
        new_image.save(c+"Exit/" + n17 + "x" + n17 + '.png')
    elif i == 18:
        new_image = img.resize((n18, n18))
        n18= str(n18)
        new_image.save(c+"Exit/" + n18 + "x" + n18 + '.png')
    elif i == 19:
        new_image = img.resize((n19, n19))
        n19= str(n19)
        new_image.save(c+"Exit/" + n19 + "x" + n19 + '.png')
    elif i == 20:
        new_image = img.resize((n20, n20))
        n20= str(n20)
        new_image.save(c+"Exit/" + n20 + "x" + n20 + '.png')
    elif i == 21:
        new_image = img.resize((n21, n21))
        n21= str(n21)
        new_image.save(c+"Exit/" + n21 + "x" + n21 + '.png')
    elif i == 22:
        new_image = img.resize((n22, n22))
        n22 = str(n22)
        new_image.save(c+"Exit/" + n22 + "x" + n22 + '.png')
    elif i == 23:
        new_image = img.resize((n23, n23))
        n23= str(n23)
        new_image.save(c+"Exit/" + n23 + "x" + n23 + '.png')
    elif i == 24:
        new_image = img.resize((n24, n24))
        n24= str(n24)
        new_image.save(c+"Exit/" + n24 + "x" + n24 + '.png')
    elif i == 25:
        new_image = img.resize((n25, n25))
        n25= str(n25)
        new_image.save(c+"Exit/" + n25 + "x" + n25 + '.png')
    elif i == 26:
        new_image = img.resize((n26, n26))
        n26= str(n26)
        new_image.save(c+"Exit/" + n26 + "x" + n26 + '.png')
    elif i == 27:
        new_image = img.resize((n27, n27))
        n27= str(n27)
        new_image.save(c+"Exit/" + n27 + "x" + n27 + '.png')
    elif i == 28:
        new_image = img.resize((n28, n28))
        n28= str(n28)
        new_image.save(c+"Exit/" + n28 + "x" + n28 + '.png')
    elif i == 29:
        new_image = img.resize((n29, n29))
        n29= str(n29)
        new_image.save(c+"Exit/" + n29 + "x" + n29 + '.png')
    elif i == 30:
        new_image = img.resize((n30, n30))
        n30= str(n30)
        new_image.save(c+"Exit/" + n30 + "x" + n30 + '.png')
    elif i == 31:
        new_image = img.resize((n31, n31))
        n31= str(n31)
        new_image.save(c+"Exit/" + n31 + "x" + n31 + '.png')
    elif i == 32:
        new_image = img.resize((n32, n32))
        n32= str(n32)
        new_image.save(c+"Exit/" + n32 + "x" + n32 + '.png')
    elif i == 33:
        new_image = img.resize((n33, n33))
        n33= str(n33)
        new_image.save(c+"Exit/" + n33 + "x" + n33 + '.png')

# для норм фото

# for i in range(q+1):
#     if i == 1:
#         new_image = img.resize((m1, m1_1))
#         m1= str(m1)
#         m1_1= str(m1_1)
#         new_image.save(c+"Exit/" + m1 + "x" + m1_1 + '.png')
#     elif i == 2:
#         new_image = img.resize((m2, m2_1))
#         m2 = str(m2)
#         m2_1 = str(m2_1)
#         new_image.save(c+"Exit/" + m2 + "x" + m2_1 + '.png')
#     elif i == 3:
#         new_image = img.resize((m3, m3_1))
#         m3= str(m3)
#         m3_1= str(m3_1)
#         new_image.save(c+"Exit/" + m3 + "x" + m3_1 + '.png')
#     elif i == 4:
#         new_image = img.resize((m4, m4_1))
#         m4= str(m4)
#         m4_1= str(m4_1)
#         new_image.save(c+"Exit/" + m4 + "x" + m4_1 + '.png')
#     elif i == 5:
#         new_image = img.resize((m5, m5_1))
#         m5= str(m5)
#         m5_1= str(m5_1)
#         new_image.save(c+"Exit/" + m5 + "x" + m5_1 + '.png')
#     elif i == 6:
#         new_image = img.resize((m6, m6_1))
#         m6= str(m6)
#         m6_1= str(m6_1)
#         new_image.save(c+"Exit/" + m6 + "x" + m6_1 + '.png')
#     elif i == 7:
#         new_image = img.resize((m7, m7_1))
#         m7= str(m7)
#         m7_1= str(m7_1)
#         new_image.save(c+"Exit/" + m7 + "x" + m7_1 + '.png')
#     elif i == 8:
#         new_image = img.resize((m8, m8_1))
#         m8= str(m8)
#         m8_1= str(m8_1)
#         new_image.save(c+"Exit/" + m8 + "x" + m8_1 + '.png')
#     elif i == 9:
#         new_image = img.resize((m9, m9_1))
#         m9= str(m9)
#         m9_1= str(m9_1)
#         new_image.save(c+"Exit/" + m9 + "x" + m9_1 + '.png')
#     elif i == 10:
#         new_image = img.resize((m10, m10_1))
#         m10= str(m10)
#         m10_1= str(m10_1)
#         new_image.save(c+"Exit/" + m10 + "x" + m10_1 + '.png')
#     elif i == 11:
#         new_image = img.resize((m11, m11_1))
#         m11= str(m11)
#         m11_1= str(m11_1)
#         new_image.save(c+"Exit/" + m11 + "x" + m11_1 + '.png')
#     elif i == 12:
#         new_image = img.resize((m12, m12_1))
#         m12= str(m12)
#         m12_1= str(m12_1)
#         new_image.save(c+"Exit/" + m12 + "x" + m12_1 + '.png')
#     elif i == 13:
#         new_image = img.resize((m13, m13_1))
#         m13= str(m13)
#         m13_1= str(m13_1)
#         new_image.save(c+"Exit/" + m13 + "x" + m13_1 + '.png')
#     elif i == 14:
#         new_image = img.resize((m14, m14_1))
#         m41= str(m14)
#         m41_1= str(m14_1)
#         new_image.save(c+"Exit/" + m14 + "x" + m14_1 + '.png')
#     elif i == 15:
#         new_image = img.resize((m15, m15_1))
#         m15= str(m15)
#         m15_1= str(m15_1)
#         new_image.save(c+"Exit/" + m15 + "x" + m15_1 + '.png')
#     elif i == 16:
#         new_image = img.resize((m16, m16_1))
#         m16= str(m16)
#         m16_1= str(m16_1)
#         new_image.save(c+"Exit/" + m16 + "x" + m16_1 + '.png')
#     elif i == 17:
#         new_image = img.resize((m17, m17_1))
#         m17= str(m17)
#         m17_1= str(m17_1)
#         new_image.save(c+"Exit/" + m17 + "x" + m17_1 + '.png')
#     elif i == 18:
#         new_image = img.resize((m18, m18_1))
#         m18= str(m18)
#         m18_1= str(m18_1)
#         new_image.save(c+"Exit/" + m18 + "x" + m18_1 + '.png')
#     elif i == 19:
#         new_image = img.resize((m19, m19_1))
#         m19= str(m19)
#         m19_1= str(m19_1)
#         new_image.save(c+"Exit/" + m19 + "x" + m19_1 + '.png')
#     elif i == 20:
#         new_image = img.resize((m20, m20_1))
#         m20= str(m20)
#         m20_1= str(m20_1)
#         new_image.save(c+"Exit/" + m20 + "x" + m20_1 + '.png')
#     elif i == 21:
#         new_image = img.resize((m21, m21_1))
#         m21= str(m21)
#         m21_1= str(m21_1)
#         new_image.save(c+"Exit/" + m21 + "x" + m21_1 + '.png')
#     elif i == 22:
#         new_image = img.resize((m22, m22_1))
#         m22 = str(m22)
#         m22_1 = str(m22_1)
#         new_image.save(c+"Exit/" + m22 + "x" + m22_1 + '.png')
#     elif i == 23:
#         new_image = img.resize((m23, m23_1))
#         m23= str(m23)
#         m23_1= str(m23_1)
#         new_image.save(c+"Exit/" + m23 + "x" + m23_1 + '.png')
#     elif i == 24:
#         new_image = img.resize((m24, m24_1))
#         m24= str(m24)
#         m24_1= str(m24_1)
#         new_image.save(c+"Exit/" + m24 + "x" + m24_1 + '.png')
#     elif i == 25:
#         new_image = img.resize((m25, m25_1))
#         m25= str(m25)
#         m25_1= str(m25_1)
#         new_image.save(c+"Exit/" + m25 + "x" + m25_1 + '.png')
#     elif i == 26:
#         new_image = img.resize((m26, m26_1))
#         m26= str(m26)
#         m26_1= str(m26_1)
#         new_image.save(c+"Exit/" + m26 + "x" + m26_1 + '.png')
#     elif i == 27:
#         new_image = img.resize((m27, m27_1))
#         m27= str(m27)
#         m27_1= str(m27_1)
#         new_image.save(c+"Exit/" + m27 + "x" + m27_1 + '.png')
#     elif i == 28:
#         new_image = img.resize((m28, m28_1))
#         m28= str(m28)
#         m28_1= str(m28_1)
#         new_image.save(c+"Exit/" + m28 + "x" + m28_1 + '.png')
#     elif i == 29:
#         new_image = img.resize((m29, m29_1))
#         m29= str(m29)
#         m29_1= str(m29_1)
#         new_image.save(c+"Exit/" + m29 + "x" + m29_1 + '.png')
#     elif i == 30:
#         new_image = img.resize((m30, m30_1))
#         m30= str(m30)
#         m30_1= str(m30_1)
#         new_image.save(c+"Exit/" + m30 + "x" + m30_1 + '.png')
#     elif i == 31:
#         new_image = img.resize((m31, m31_1))
#         m31= str(m31)
#         m31_1= str(m31_1)
#         new_image.save(c+"Exit/" + m31 + "x" + m31_1 + '.png')
#     elif i == 32:
#         new_image = img.resize((m32, m32_1))
#         m32= str(m32)
#         m32_1= str(m32_1)
#         new_image.save(c+"Exit/" + m32 + "x" + m32_1 + '.png')
#     elif i == 33:
#         new_image = img.resize((m33, m33_1))
#         m33= str(m33)
#         m33_1= str(m33_1)
#         new_image.save(c+"Exit/" + m33 + "x" + m33_1 + '.png')