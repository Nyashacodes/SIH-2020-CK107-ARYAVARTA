import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # _, binary = cv2.threshold(greyImg, 125, 150, cv2.THRESH_BINARY_INV)

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of contours = " + str(len(contours)))
    print(contours[0])

    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Image', img)
    cv2.imshow('Image GRAY', imgray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

