import pymsgbox
import cv2


mouse_is_pressing = False
start_x, starty = -1, -1

def mouse_callback(event, x, y, flags, param):
    global start_x, start_y, mouse_is_pressing

    img_result = img_color.copy()

    if event == cv2.EVENT_LBUTTONDOWN:

        mouse_is_pressing = True
        start_x, start_y = x, y

        cv2.circle(img_result, (x,y), 10, (0, 255, 0), -1)

        cv2.imshow("img_color", img_result)

    elif event == cv2.EVENT_MOUSEMOVE:

        if mouse_is_pressing:
            cv2.rectangle(img_result, (start_x, start_y), (x, y), (0, 255, 0), 3)

            cv2.imshow("img_color", img_result)

    elif event == cv2.EVENT_LBUTTONUP:

        mouse_is_pressing = False
        img_cat = cv2.rectangle(img_result, (start_x, start_y), (x, y), (0, 255, 0), 1)
        dir = "//141.223.65.90/fi lab share backup/temp/YOGO_Cloud/new/unknown/img/"
        #cv2.imwrite('opencv' + str(i) + '.png', image)
        obj_name = pymsgbox.prompt('What is the name of this object?','YOGO:Manual Detection')
        filename = obj_name + "1"
        cv2.imwrite(dir+filename+'.jpg', img_cat)
        f = open(dir+filename+'.txt', 'w')
        f.write(obj_name+'\n')
        f.write(str((start_x,start_y)) + '\n')
        f.write(str((x,y)) + '\n')
        f.close()

        #cv2.imshow("img_result", img_cat)


cam = cv2.VideoCapture(1)
ret, img_color = cam.read()
cam.release()
cv2.imshow("img_color", img_color)
cv2.setMouseCallback('img_color', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
