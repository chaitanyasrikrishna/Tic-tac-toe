import cv2
import numpy as np
def func():
    func.counter+=1
    return func.counter
func.counter=0

def check():
    a1=img[50,5]
    b1=img[50,50]
    a2=img[150,5]
    b2=img[150,50]
    a3=img[250,5]
    b3=img[250,50]
    a4=img[50,105]
    b4=img[50,150]
    a5=img[150,105]
    b5=img[150,150]
    a6=img[250,105]
    b6=img[250,150]
    a7=img[50,205]
    b7=img[50,250]
    a8=img[150,205]
    b8=img[150,250]
    a9=img[250,205]
    b9=img[250,250]
    if a1[1]==a2[1]and a2[1]==a3[1] and a1[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b1[1]==b2[1] and b2[1]==b3[1] and b1[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a4[1]==a5[1]and a5[1]==a6[1] and a4[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b4[1]==b5[1] and b5[1]==b6[1] and b6[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a7[1]==a8[1]and a8[1]==a9[1] and a8[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b7[1]==b8[1] and b8[1]==b9[1] and b9[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a1[1]==a4[1]and a1[1]==a7[1] and a1[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b1[1]==b7[1] and b4[1]==b7[1] and b1[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a5[1]==a2[1]and a2[1]==a8[1] and a2[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b8[1]==b2[1] and b2[1]==b5[1] and b2[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a3[1]==a9[1]and a6[1]==a3[1] and a3[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b9[1]==b6[1] and b6[1]==b3[1] and b3[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a1[1]==a5[1]and a1[1]==a9[1] and a1[1]==255:
        print ' player _O_ won'
        
        cv2.destroyAllWindows()
    elif b1[1]==b5[1] and b5[1]==b9[1] and b1[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    elif a3[1]==a5[1]and a5[1]==a7[1] and a3[1]==255:
        print ' player _O_ won'
        cv2.destroyAllWindows()
    elif b7[1]==b3[1] and b5[1]==b3[1] and b3[1]==255:
        print 'player _X_ won'
        cv2.destroyAllWindows()
    else:
        if func.counter==9:
            print 'Tie'
            cv2.destroyAllWindows()
    if (a1[1]==b1[1] and a1[1]==255)or(a2[1]==b2[1] and a2[1]==255)or(a3[1]==b3[1] and a3[1]==255)or(a4[1]==b4[1] and a4[1]==255)or(a5[1]==b5[1] and a5[1]==255)or(a6[1]==b6[1] and a6[1]==255)or(a7[1]==b7[1] and a7[1]==255)or(a8[1]==b8[1] and a8[1]==255)or(a9[1]==b9[1] and a9[1]==255):
        print 'invalid input'
        cv2.destroyAllWindows()
    

def clicked (event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONUP:                
        c=func()
        print x,y,c
        i=x/100
        j=y/100
        if i<3:
            if j<3:
                if c%2!=0:
                    cv2.circle(img,(50*((2*i)+1),50*((2*j)+1)),45,(0,255,0),4)  
                else:
                    cv2.line(img,(100*i+20,100*j+20),(100*(i+1)-20,100*(j+1)-20),(0,255,0),4)
                    cv2.line(img,(100*i+20,100*(j+1)-20),(100*(i+1)-20,100*j+20),(0,255,0),4)
        cv2.imshow('TIC TAC TOE',img)
        check()
                

img=np.zeros((300,300,3),np.uint8)
cv2.line(img,(0,100),(300,100),(0,0,255),4)
cv2.line(img,(0,200),(300,200),(0,0,255),4)
cv2.line(img,(100,0),(100,300),(0,0,255),4)
cv2.line(img,(200,0),(200,300),(0,0,255),4)
cv2.imshow('TIC TAC TOE' ,img)
cv2.setMouseCallback('TIC TAC TOE',clicked)
cv2.waitKey(0)
cv2.destroyAllWindows()

