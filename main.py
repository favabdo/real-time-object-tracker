import cv2
 
def drawing_box ( bounding_box , frame, text ="object"):
    x,y,w,h = map(int , bounding_box)
    cv2.rectangle(frame , (x,y),(x+w ,y+h), (0,255,0), 2)
    cv2.putText(frame, "object",( x , y - 10) ,cv2.FONT_ITALIC,2 )
    return frame
    
def object_tracking():
    tracker = cv2.TrackerCSRT_create()
    video_cap =cv2.VideoCapture(0)


    if not video_cap.isOpened():
        print("couldn't open Webcam" )
        return
    
    while True:
        ret , frame = video_cap.read()
        if not ret :
            break

        cv2.imshow("real-time tracker", frame)
        cv2.putText("press S to select object or Esc to Quit" 
                    ,(20.40), cv2.FONT_ITALIC,.4,(0,255,0),1)
        key = cv2.waitKey(1) & 0xff

        if key == ord('s'):
            bounding_box = cv2.selectROI("real-time tracker"
                                         , frame ,fromCenter=False)
            if bounding_box != (0,0,0,0):
                tracker.init(frame,bounding_box)

                x,y,w,h = map(int , bounding_box)
                templet = frame[ y:y+h , x:x+w]
                break
        elif key ==27:
            video_cap.release()
            cv2.destroyAllWindows()
            return
    
    while True :
        ret,frame = video_cap.read()
        if not ret :
            break

        is_tracking ,bounding_box = tracker.update(frame)

        if is_tracking:
            frame= drawing_box(bounding_box,frame)
            lost_time=None

            cv2.putText(frame ,"press R to reselect object or Esc to Quit"
            ,(20,40), cv2.FONT_ITALIC ,.4 ,(255,0,0),1 )
        
        else :

             cv2.putText(frame ,"  Trackion lost (Searching) "
             ,(50,40), cv2.FONT_ITALIC ,.8 ,(0,0,255),2)

        if key == ord('r'):
            bounding_box = cv2.selectROI("real-time tracker"
                                         , frame ,fromCenter=False)
            if bounding_box != (0,0,0,0):
                tracker.init(frame,bounding_box)

                x,y,w,h = map(int , bounding_box)
                templet = frame[ y:y+h , x:x+w]
                break
        elif key ==27:
            video_cap.release()
            cv2.destroyAllWindows()
            return

if __name__== "__main__":
    object_tracking()

        