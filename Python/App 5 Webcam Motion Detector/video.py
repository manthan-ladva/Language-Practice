import cv2                                                  #--------------------------------Importing Librabies
import time                                                 #--------------------------------Importing Librabies
import pandas                                               #--------------------------------Importing Librabies
from datetime import datetime                               #--------------------------------Importing Librabies

video = cv2.VideoCapture(0)                                                  #--------------------------------Laptop Camera Start
status_list = [None, None]                                                   #----------------Connected to status so that time will be obtained with the refrence of this
times = []                                                                   #--------------------------------List of time will be obtained from this
first_frame = None                                                           #--------------------------------Delcaring Variable
df = pandas.DataFrame(columns = ["Start", "End"])                            #--------------------------------Declaration of DataFrame

while True:
    check, frame = video.read()                                                  #--------------------------------Read the images from the Camera
    status = 0                                                                   #--------------------------------Delcaring Variable

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)                                              #--------------------------------Transfers the images to gray color
    gray = cv2.GaussianBlur(gray, (21, 21), 0)                                                  #--------------------------------Blur the image

    if first_frame is None:                                                  #--------------------------------Continues the telecast
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)                                                 #--------------------------------Make the difference
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]                     #--------------------------------Black and white image screen
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)                                #--------------------------------Smooth the B & W screen

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)           #--------------------------------Face recognitions
    for contour in cnts:
        if cv2.contourArea(contour) < 9500:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)

    status_list.append(status)                                                                   #--------------------------------Writing in Status_list
    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2] == 0:                               #--------------------------------Jyare achanak bdlai che tyare e time record kre che
        times.append(datetime.now())                                 #--------------------------------Only two times will be recordedthat is incoming & outgoing
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)                                                  #--------------------------------Image showing in the screen
    cv2.imshow("Delta Frame", delta_frame)                                          #--------------------------------Image showing in the screen
    cv2.imshow("Threshold Frame", thresh_frame)                                     #--------------------------------Image showing in the screen
    cv2.imshow("Color Frame", frame)                                                #--------------------------------Image showing in the screen

    key = cv2.waitKey(1)                                                  #--------------------------------Trigger to stop
    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break


print(status_list)
for z in times:
    print(z)

for i in range(0, len(times), 2):                                     #--------------------------------Writing in DataFrame
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index = True)
#--------------------------------Range will start with 0 and will end at n-1 and 3rd digit is for between gap which will added in the first place of the Range i.e. "0"
#--------------------------------"ignore_index = True" <--- is applied when there is not available any Series name.   If dout, Remove it and try

df.to_csv("Times.csv")                                    #--------------------------------Formation of csv file. It will erase previous details and make new details

video.release()
cv2.destroyAllWindows()
