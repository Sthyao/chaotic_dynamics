from PIL import Image
import numpy as np

a = [
       1,1,0,0,0,0,0,0,1,1,
        0,1,1,0,0,0,0,1,1,0,
        0,0,1,1,0,0,1,1,0,0,
        0,0,0,1,1,1,1,0,0,0,
        0,0,0,0,1,1,0,0,0,0,
        0,0,0,1,1,1,1,0,0,0,
        0,0,1,1,0,0,1,1,0,0,
        0,1,1,0,0,0,0,1,1,0,
        1,1,0,0,0,0,0,0,1,1,
        0,0,0,0,0,0,0,0,0,0
]


def number_to_image(a):
        img = Image.new("RGB",(100,100))
        pixTupleB = (0,0,0,15)
        pixTupleW = (255,255,255,15)
        if a[0] >= 0.5:
                sum_ = np.ones((10,10))
        else:
                sum_ = np.zeros((10,10))
        for j in range(1,10):
                if a[j] >= 0.5 :
                        temp = np.ones((10,10))
                else:
                        temp = np.zeros((10,10))
                sum_ = np.hstack((sum_,temp))
        sum_0 = sum_
        for i in range(1,10):
                if a[i*10] >= 0.5:
                                sum_ = np.ones((10,10))
                else:
                        sum_ = np.zeros((10,10))
                for j in range(1,10):
                        if a[i*10+j] >= 0.5:
                                temp = np.ones((10,10))
                        else:
                                temp = np.zeros((10,10))
                        sum_ = np.hstack((sum_,temp))
                sum_0 = np.vstack((sum_0,sum_))
        for i in range(100):
                for j in range(100):
                        if sum_0[j][i] == 1:
                                img.putpixel((i,j),pixTupleB)
                        else:
                                img.putpixel((i,j),pixTupleW)
        img.show()


number_to_image(a)

