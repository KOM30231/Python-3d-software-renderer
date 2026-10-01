
from PIL import Image
import numpy as np
from math import tan

def draw_line(a,b,c=(255,255,255)):
	t=0
	while t<=1:
		x = round(a[0]+t*(b[0]-a[0]))
		y = round(a[1]+t*(b[1]-a[1]))

		new_img.putpixel((x,y),(255,255,255))
		t+=0.02

def draw_triangle(trig):
	for i in range(len(trig)):
		draw_line(trig[i-1],trig[i],(0,0,0))


def area_triangle(a,b,c):
    return 0.5 * ((b[1]-a[1])*(b[0]+a[0]) + (c[1]-b[1])*(c[0]+b[0]) + (a[1]-c[1])*(a[0]+c[0]))

def fill_triangle(l1):
    t_area = area_triangle(l1[0],l1[1],l1[2])
    top,bottom,left,right=64,0,64,0
    for i in l1:
        if i[0]<top:
            top=i[0]
        if i[0]>bottom:
            bottom=i[0]
        if i[1]<left:
            left=i[1]
        if i[1]>right:
            right=i[1]
    for x in range(int(top),int(bottom+1)):
        for y in range(int(left),int(right+1)):

            alpha = area_triangle([x,y],l1[0],l1[1])/t_area
            beta = area_triangle([x,y],l1[1],l1[2])/t_area
            gamma = area_triangle([x,y],l1[2],l1[0])/t_area

            if alpha>0 and alpha<1 and beta>0 and beta<1 and gamma>0 and gamma<1:
                
                new_img.putpixel((x,y),(255,255,255))


def world_to_screen(l1):
    znear = 1
    zfar = 10
    f = 1/(tan(90/2))
    l1 = np.hstack((l1,np.ones((l1.shape[0],1))))
    p = np.array([
                [1,0,0,0],
                [0,1,0,0],
                [0,0,(zfar+znear)/(znear-zfar), (2*zfar*znear)/(znear-zfar)],
                [0,0,-1,0]
    ])
    clip = p@l1.T
    l2=[]
    for i in range(3):
        temp=[]
        for j in range(3):
            temp.append(clip[j,i]/clip[3,1])
        l2.append(temp)
    for i in l2:
        i[0] = round(((i[0]+1) / 2) * 64)
        i[1] = round(((1-i[1]) / 2) * 64)
    l2=np.array(l2)
    return l2



new_img=Image.new("RGB",(64,64),color='black')
new_img.putpixel((7,3),(255,255,255))
new_img.putpixel((62,53),(255,255,255))
new_img.putpixel((12,37),(255,255,255))
l1=np.array([[2,1,5],[4,1,5],[3,3,5]])


# draw_triangle(l1)
# fill_triangle(l1)
# l2=np.array([world_to_screen(l1)])


l2=world_to_screen(l1)
draw_triangle(l2)
fill_triangle(l2)
new_img.save("out_img.bmp")
