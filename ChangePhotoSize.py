from PIL import Image
from colorama import Fore
import os.path

directory = r'D:\_Test\End\3'
files = os.listdir(directory)

counter = 0

for filename in os.listdir(directory):
    # print(filename)
    # print(directory+'\\'+filename)

    image = Image.open(directory+'\\'+filename)
    new_image = image.resize((2160, 3840))
    new_image.save(r'D:\_Test\End\23'+'\\'+filename)
    
    print(Fore.YELLOW + f'\r[+] Сохраняю: {round(counter*100/len(files), 2)}/{100}', end='')
    counter += 1

print("OK")
    


# anime style, anime, beautiful, girl, good quality, detailed face

# ugly, bad hands, extra hands, bad quality, ugly face, bad anatomy

# 1080

# 1920

# 17
# 0.45