
	  
import time 
from progressbar import *
import sys
#wid = widgets[Bar(marker='#', left='|',right='|',fill_left=True)]
pbar = ProgressBar()
for i in pbar(range(100)): 
 time.sleep(0.04)
 
from pykeyboard import PyKeyboard
k = PyKeyboard()
import time
from SimpleCV import *
cam = Camera(0,{"width":320,"height":240})
paused = False
while True:
 img = cam.getImage().flipHorizontal()
 face_segment = HaarCascade("face.xml")
 gray = img.grayscale() 
 autoface = gray.findHaarFeatures(face_segment)
 if(autoface is not None):
  if paused:
   k.tap_key(k.space_key)
   paused = False
   #paused = False
   print "continuing"
   
 else:
  if not paused:
    k.tap_key(k.space_key)
	#Create an Alt+Tab combo
    #k.press_key(k.alt_key)
    #k.tap_key(k.functio)
    #k.release_key(k.alt_key)

    paused = True
    print "paused"	