from PIL import Image
import os, sys, glob

name = input('请输入图片名称：')
tmpImage = Image.new('RGB', (30000, 2000))
folders = glob.glob(pathname='./images/*')
files = glob.glob(pathname='./images/0/*.jpg')
folderNum = len(folders)
fileNum = len(files)

def main():
    widthArr = []
    y = 0
    width = 0
    height = 0
    for i in range(0, folderNum):
        x = 0
        heightArr = []
        for j in range(0, fileNum):
            print('合并第%d行，第%d张图片' %(i, j))
            read = Image.open('./images/%d/%d_%d.jpg' %(i, j, i))
            widthArr.append(read.size[0])
            heightArr.append(read.size[1])
            w = widthArr[j]
            h = heightArr[j]
            tmpImage.paste(read, (x, y))
            x = x + w
        y = y + h
        width = x
    height = y
    print('合并结束')
    print('生成临时文件')
    tmpImage.save(str(name) + '.tmp.jpg')
    final = Image.open(str(name) + '.tmp.jpg')
    print('裁剪图片 '+ str(width) +'x'+ str(height))
    finalImage = final.crop((0, 0, width, height))
    print('保存成功')
    finalImage.save(str(name) +'.jpg')
    print('移除临时文件')
    os.remove(str(name) + '.tmp.jpg')

main()

# 29817x1410