import cv2 

space = cv2.imread('solar-system.jpg')
cv2.putText(space,"Sun",(90,100),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Mercury",(120,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Venus",(200,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Earth",(270,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Mars",(380,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Jupiter",(570,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Saturn",(700,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Uranus",(900,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.putText(space,"Neptune",(1100,200),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(255,255,255))
cv2.imshow('solar system',space)
cv2.waitKey(10000)