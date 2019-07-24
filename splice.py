from PIL import Image
import os, glob

Image.MAX_IMAGE_PIXELS = None
name = input('请输入图片名称：')
splice = input('请输入分段数（默认1）：')

if splice == '':
    splice = 1

folders = glob.glob(pathname='./images/*')
files = glob.glob(pathname='./images/0/*.jpg')
folderNum = len(folders)

for spliceIndex in range(0, int(splice)):
    perNum = len(files) // int(splice)
    startIndex = perNum * spliceIndex
    fileNum = perNum * (spliceIndex + 1)
    tmpImage = Image.new('RGB', (perNum * 256, folderNum * 256))

    def main():
        widthArr = []
        y = 0
        width = 0
        height = 0
        for i in range(0, folderNum):
            x = 0
            heightArr = []
            for j in range(startIndex, fileNum):
                print('合并第(%d/%d)部分，第(%d/%d)行，第(%d/%d)张图片' %(spliceIndex + 1, int(splice), i, folderNum, j, fileNum))
                read = Image.open('./images/%d/%d_%d.jpg' %(i, j, i))
                widthArr.append(read.size[0])
                heightArr.append(read.size[1])
                w = widthArr[j - startIndex]
                h = heightArr[j - startIndex]
                tmpImage.paste(read, (x, y))
                x = x + w
            y = y + h
            width = x
        height = y
        print('第%d部分合并结束' %(spliceIndex + 1))
        print('生成临时文件')
        filename = (str(name) if splice == '' else str(name) +'.'+ str(spliceIndex + 1))
        tmpImage.save(filename +'.tmp.jpg')
        final = Image.open(filename +'.tmp.jpg')
        print('裁剪图片 '+ str(width) +'x'+ str(height))
        finalImage = final.crop((0, 0, width, height))
        print('保存成功')
        finalImage.save(filename +'.jpg')
        print('移除临时文件')
        os.remove(filename +'.tmp.jpg')
    main()
print('执行完毕')