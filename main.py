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
    for x in range(top,bottom+1):
        for y in range(left,right+1):

            alpha = area_triangle([x,y],l1[0],l1[1])/t_area
            beta = area_triangle([x,y],l1[1],l1[2])/t_area
            gamma = area_triangle([x,y],l1[2],l1[0])/t_area

            if alpha>0 and alpha<1 and beta>0 and beta<1 and gamma>0 and gamma<1:
                new_img.putpixel((x,y),(255,255,255))

def world_to_screen(l1):
    znear=0.1
    f=1/(tan(60/2))
    p=np.array([[f,0,0,0],
                [0,f,0,0],
                [0,f,-1,-2*znear],
                [0,0,-1,0]
    ])
    new_col=np.array([[1],[1],[1]])
    l1=np.append(l1,new_col,axis=1)
    l2=[]
    for i in range(3):
        ans=p@l1[i].T
        print(ans)
        l2.append(ans)
    return l2

def trial(x,y,z):
    x = x/z
    y = y/z
    screenx = (x + 1.0) * 0.5 * 64
    screeny = (1 - y) * 0.5 * 64
    return round(screenx),round(screeny)

new_img=Image.new("RGB",(64,64),color='black')
new_img.putpixel((7,3),(255,255,255))
new_img.putpixel((62,53),(255,255,255))
new_img.putpixel((12,37),(255,255,255))
l1=np.array([[7,3,0],[12,37,38],[62,53,52]])


# draw_triangle(l1)
# fill_triangle(l1)
# l2=np.array([world_to_screen(l1)])
x1,y1=trial(-1,-1,10)
x2,y2=trial(1,-1,10)
x3,y3=trial(0,0,10)

l1=np.array([[x1,y1],[x2,y2],[x3,y3]])
draw_triangle(l1)
fill_triangle(l1)
new_img.save("out_img.bmp")
