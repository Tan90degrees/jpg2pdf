import os
import sys
import re
import time
from PIL import Image

srcPATH = sys.argv[1]
if not os.path.isdir(srcPATH):
    print("error!!!")
    exit(1)
if len(sys.argv) == 3:
    dstPATH = sys.argv[2]
    if os.path.isdir(dstPATH):
        dstPATH = os.path.join(dstPATH, "out" + str(int(time.time()) >> 3) + ".pdf")
    elif not os.path.isfile(dstPATH):
        print("error!!!")
        exit(1)
else:
    dstPATH = os.getcwd()
    dstPATH = os.path.join(dstPATH, "out" + str(int(time.time()) >> 3) + ".pdf")

prog = re.compile("[a-zA-Z0-9_]+\.jpg")
files = os.listdir(srcPATH)

files = str(files)
jpgs = prog.findall(files)

dstFp = Image.open(os.path.join(srcPATH, jpgs[0]))
imgList = []
num = len(jpgs)
i = 1
while i < num:
    imgPath = os.path.join(srcPATH, jpgs[i])
    imgList.append(Image.open(imgPath))
    i += 1

dstFp.save(dstPATH, "PDF", resolution=100.0, save_all=True, append_images=imgList)
