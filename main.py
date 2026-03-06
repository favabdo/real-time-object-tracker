import cv2
 
def drawing_box ( bounding_box , frame, text ="object"):
    x,y,w,h = map(int , bounding_box)
    cv2.rectangle(frame , (x,y),(x+w ,y+h), (0,255,0), 2)
    cv2.putText(frame, "object",( x , y - 10) ,cv2.FONT_ITALIC,0.6 ,(0,255,0),2 )
    return frame
    
def object_tracking():
    tracker = cv2.TrackerCSRT_create()
    video_cap =cv2.VideoCapture(0)
    is_tracking= False

    if not video_cap.isOpened():
        print("couldn't open Webcam" )
        return
    
    while True:
         ret,frame =video_cap.read()
         if not ret: 
            break
         
         if is_tracking:
            success ,bounding_box=tracker.update(frame)
            if success:
                frame=drawing_box(bounding_box,frame)
                cv2.putText(frame , "Tracking....(press R to reselect object or 'Esc' to Quit " 
                    ,(20,40), cv2.FONT_ITALIC,.6,(255,255,0),2)
                    
            else:
                cv2.putText(frame , "Tracking Lost (press R to reselect object )" 
                    ,(40,40), cv2.FONT_ITALIC,.8,(0,255,0),2)
         else :
                cv2.putText(frame , "press S to select object or 'Esc' to Quit )" 
                        ,(20,40), cv2.FONT_ITALIC,.6,(0,255,0),2)

         cv2.imshow("real-time tracker", frame)
         key = cv2.waitKey(1) & 0xff

         if key == ord('s') or key==ord('r'):
                bounding_box = cv2.selectROI("real-time tracker"
                                                    , frame ,fromCenter=False)
                if bounding_box != (0,0,0,0):
                        tracker=cv2.TrackerCSRT_create()
                        tracker.init(frame,bounding_box)
                        is_tracking =True

                        
         elif key ==27:
                break
    
    video_cap.release()
    cv2.destroyAllWindows()   

if __name__== "__main__":
    object_tracking()

        