import os
import cv2
def getLab(dir):
    #dir = raw_input("input file's path:")
    #label = raw_input('input lable of images:')
    files = os.listdir(dir)
    files.sort()
    print '****************'
    print 'input :',dir
    print 'start...'

    for root,dirs,files in os.walk(dir):
        for file in files:
            image_file = os.path.join(root,file).decode('gbk').encode('utf-8')
    	    print file
            img = cv2.imread(image_file)
    	   # img1 = img.copy()
            lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    	    l,a,b = cv2.split(lab)
    	    cv2.imwrite(image_file, l)
    print 'down!'
    print '****************'    
    
if __name__ == '__main__':
    #dir = raw_input("input file's path:")
    #dir = cvLoadImage("3.jpeg")
    getLab('data/train')   
