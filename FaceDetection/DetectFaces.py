import cv2

print('hello this is object detection project')

# Load the pre-trained classifier: Like OpenCV library
model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image
img = cv2.imread('group.JPEG')

# Convert image to grayscale by cv2 (Haar cascade works better in grayscale)
# Haar cascade for faster detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

# Draw rectangles around faces 5 arguments
# '(x, y): Top-left corner, (x+w, y+h): Bottom-right, calc based on h, w'
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

# Display the image with detected faces
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

# 'keywait=0 means key press from the user'
cv2.waitKey(0)
cv2.destroyAllWindows()