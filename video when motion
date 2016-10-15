from SimpleCV import Camera, Display, Image, np, VideoStream
import time
#Program by Fares Al Ghazy, 15/8/2016
#A thanks to the FaceBook group " Raspberry pi" which was very helpful
#A special thanks to Martin Jenkins for giving alot of his time, knowledge and support
#This code is not supposed to be used commercially
#Do not use program before checking with local laws

#This program is not meant to run instantly, try to understand it then use it :)
#initialize camera
cam = Camera()
#threshold between 0 and 1
def detectmotion(threshold,noise_constant):
    
    #take 2 images
    img1 = cam.getImage()
    #wait before taking next image, some time diff ==> greater difference ==> better detection
    time.sleep()
    img2 = cam.getImage()
    #find difference between images
    difference = img2 - img1
    #since this uses integer division, pixels close to 0 will become 0, this depends on camera quality
    difference = difference/noise_constant
    #convert difference to matrix
    matrix = difference.getNumpy()
    #flatten matrix
    flat = matrix.flatten()
    #nonzero pixels are ones that have gone through motion (for more info on this, look into image arithmetics)
    num_pixels_changed = np.count_nonzero(flat)
    percent_change = float(num_pixels_changed) / float(len(flat))
    if percent_change >= threshold:
        return True
    else:
        return False
#initialize videostream
#choose video format
format = ""
#create file name
name = "" + time.strftime("%d_%m")+ time.strftime("%H_%M") +format
#determine file path
path = ""+name
 
vs = VideoStream(path, fps = )
while True:
    print("Program started,waiting for motion")
    motion = detectmotion()
    if motion:
        print("Motion detected, capturing video")
        start_time = time.time()
        mins = 0
        #determine video length and take video
        while(mins <= ):
            image=cam.getImage()
            image.save(vs)
            mins = (time.time() - start_time) / 60
        print("Video captured and saved")
       
        time.sleep()

