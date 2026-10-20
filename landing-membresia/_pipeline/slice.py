import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
f=sys.argv[1]; im=Image.open(f); w,h=im.size; n=0
for y in range(0,h,2400):
    im.crop((0,y,w,min(h,y+2400))).save(f.replace('.png',f'-{n:02d}.png')); n+=1
print(f,w,h,n,'trozos')
