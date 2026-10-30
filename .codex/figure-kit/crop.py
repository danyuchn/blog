import sys, io
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); w,h=im.size
px=im.load()
y=h-1
while y>0 and all(px[x,y]==(255,255,255) for x in range(0,w,4)): y-=1
pad=int(sys.argv[3]) if len(sys.argv)>3 else 0
im=im.crop((0,0,w,min(h,y+1+pad)))
# quality 85, stepped down until the file is under 400KB
for q in range(85,69,-3):
    b=io.BytesIO(); im.save(b,'JPEG',quality=q)
    if b.tell()<=400_000: break
open(sys.argv[2],'wb').write(b.getvalue())
print(sys.argv[2],im.size,q,b.tell())
