from PIL import Image
import os, sys, glob

name = input('请输入图片名称：')
size = input('请输入最终图的宽高（256x256）：')
wh = str(size).split('x')
width = wh[0]
height = wh[1]
output = Image.new('RGB', (int(width), int(height)))
folders = glob.glob(pathname='./images/*')
files = glob.glob(pathname='./images/0/*.jpg')
folderNum = len(folders)
fileNum = len(files)

def main():
    widthArr = []
    heightArr = []
    y = 0
    for i in range(0, folderNum):
        x = 0
        for j in range(0, fileNum):
            print('合并第%d行第%d张图' %(i, j))
            read = Image.open('./images/%d/%d_%d.jpg' %(i, j, i))
            print(read.size)
            widthArr.append(read.size[0])
            heightArr.append(read.size[1])
            if i == 0:
                w = 0
                h = 0
            else:
                w = widthArr[i]
                h = heightArr[j]
            output.paste(read, (x, y))
            x = x + w
        y = y + h
    print('合并结束')
    output.save(str(name) + '.jpg')
main()