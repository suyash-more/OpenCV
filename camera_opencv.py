import cv2
# ipv4 address
ipv4_url = 'http://192.168.189.228:8080'
# read video
cam = f'{ipv4_url}/video'
cap = cv2.VideoCapture(cam)
while True:
    # read each frame from video
    ret, frame = cap.read()
    # resize frames
    frame = cv2.resize(frame, (600, 600))
    # display frames
    cv2.imshow("Mobile Camera", frame)
    # press q to break the loop
    if cv2.waitKey(1) == ord('q'):
        break
# release camera
cap.release()
# distroy windows
cv2.destroyAllWindows()