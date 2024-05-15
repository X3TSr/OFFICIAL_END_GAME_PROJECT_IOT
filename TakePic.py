import cv2
import base64

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def takePic():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    cv2.imwrite('trash.jpg', image)
    
    # img = base64.b64encode(image).decode('utf-8')
    img = encode_image('/home/kylian/Apps/OFFICIAL_END_GAME_PROJECT_IOT/trash.jpg')
    
    cam.release()
    cv2.destroyAllWindows()
    return img
takePic()
