#Fares Al Ghazy
#Simple motion detection using a usb camera
#Note : Alot of the code has been commented out, this is because they are most useful in debugging.
from SimpleCV import Camera, Display, Image, np
import time
#initialize camera and display
cam = Camera()
dis = Display()
#define a threshold to trigger a message, or ask user to do so
threshold = 0.009
#This depends on your camera, using a usb camera that costs about 10$, this is the value i found most suitable
noise_constant =30
cntr = 1
while True:
    #take first pic,display and allow time to see it
    img1 = cam.getImage()
    img1.save(dis)
    #print ("Image one")
    #it is useful to wait for a small amount of time between taking pictures, as it detects motion better
    time.sleep(0.01)
    #repeat as before
    img2 = cam.getImage()
    img2.save(dis)
    #print ("Image two")
    #time.sleep(1)
    #calculate difference in images 
    difference = img2 - img1
    #sometimes values appear black but are not, this makes them black since numbers less than 20 divided by 20 are 0 (remainder removed)
    difference = difference/noise_constant
    #the next lines make sure there is a difference, commented out as are only for testing
    #difference.show()
    #print("Image of difference")
    #time.sleep(1)
    #convert picture to 3d matrix
    matrix = difference.getNumpy()
    #convert matrix to 2d (remove rgb component)
    flat = matrix.flatten()
    #find out how much changed
    num_pixels_changed = np.count_nonzero(flat)
    #this next line is also for testing and hence commented out
    #print ("Number of changed pixels is : "),(num_pixels_changed)
    #time.sleep(1)
    #len(flat) finds the total number of items in the "flat" matrix created previously
    percent_change = float(num_pixels_changed) / float(len(flat))
    #print outcome
    #print ("Percentage change = "),(percent_change*100)
    if percent_change >= threshold:
        print ("Motion has been detected"),cntr
        cntr += 1
        #time.sleep(2)
    #if percent_change < threshold:
       #print ("No motion detected")
    #time.sleep(2)
