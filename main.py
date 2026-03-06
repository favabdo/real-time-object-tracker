import cv2
 
def drawing_box ( bounding_box , frame, text ="object"):
    x,y,w,h = map(int , bounding_box)
    cv2.rectangle(frame , (x,y),(x+w ,y+h), (0,255,0), 2)
    cv2.putText(frame, "object",( x , y - 10) ,cv2.FONT_ITALIC,2 )
    return frame
    