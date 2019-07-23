from PIL import Image
import os, sys, glob

# name = input('请输入图片名称：')
# size = input('请输入最终图的宽高（256x256）：')
# width = size.split('x')[0]
# height = size.split('x')[1]
# output = Image.new('RGB', int(width), int(height))
folders = glob.glob(pathname='./image/*')
folderNum = len(folders)
def main():
    w = 258
    h = 258
    y = 0
    for i in range(0, 7):
        x = 0
        for j in range(0, 161):
            print('合并第%d行第%d张图' %(i, j))
            read = Image.open('./image/%d_%d.jpg' %(j, i))
            output.paste(read, (x, y))
            x = x + w
        y = y + h
    print('合并结束')
    output.save('1.jpg')
# get()