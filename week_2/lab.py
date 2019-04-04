import math
import numpy as np
import sys
import time
from PIL import Image 

k = 0.5
b = 0.02
A = 1
#init

def f(x,a):
    return k * x - A * ( 1 / ( 1 + math.exp( -1 * x / b))) + a

def ly(x):
    return abs( k + A * math.exp( -1 * x / b) / ( b * ( 1 + math.exp( -1 * x / b ))**2))

def sigmoid(x):
    if -x/b >= 25:
        return 1/(1+math.exp(25))
    else:
        return 1/(1+math.exp(-x/b))

def number_to_image(a,id):
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
        string = str(id) + '.png'
        img.save( 'd:\Git\chaos\week_2\py2\\'+string, 'PNG')
        #img.show()


class ShowProcess():
        i = 0 #now
        max_steps = 0 #all times
        max_arrow = 20 #length of bar
        infoDone = 'done'

        def __init__(self,max_steps,infoDone = 'Done'):
                self.max_steps = max_steps
                self.i = 0
                self.infoDone = infoDone

        def show_process(self , i = None):
                if i is not None:
                        self.i = i
                else:
                        self.i += 1
                num_arrow = int(self.i * self.max_arrow / self.max_steps)
                num_line = self.max_arrow - num_arrow
                percent = self.i * 100.0 / self.max_steps
                process_bar = '[' + '#'*num_arrow + '-'*num_line + ']' + '%.2f' % percent +'%' + '\r'
                        
                sys.stdout.write(process_bar) 
                sys.stdout.flush()
                if self.i >= self.max_steps:
                        self.close()
        
        def close(self):
                print('')
                print(self.infoDone)
                self.i = 0

"""if __name__ == '__main__':
        max_steps = 100

        process_bar = ShowProcess(max_steps,'OK')

        for i in range(max_steps):
                process_bar.show_process()
                time.sleep(0.01)
"""
#test model