import cv2
from datetime import datetime
'''
The script intended to collect images from camera
Mouse klick will grab frame from camera and save it to file.
'''

def MouseEventCallback(event, x, y, flags, param):
    global dataready
    if event == cv2.EVENT_LBUTTONUP:
        dataready=True

def main(argv=None):
    global dataready 
    img_counter=1
    cam = cv2.VideoCapture(0)
    windowName = 'Drawing'
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, MouseEventCallback)
    while (True):
      _, img = cam.read()  
      if dataready:
         now = datetime.now() 
         img_name = now.strftime("%m%d%Y%H%M%S")+".png"
         cv2.imwrite(img_name, img)
         print("{} written!".format(img_name))
         img_counter += 1
         dataready=False
      cv2.imshow(windowName, img)
      key=cv2.waitKey(1) & 0xFF
      if key== ord('x'):
         break
    cv2.destroyAllWindows()

'''
'''
dataready=False
if __name__ == "__main__":
   main()   
