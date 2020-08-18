import cv2
import os

face_classifier = cv2.CascadeClassifier('haarFiles/haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is []:
        return None

    for (x, y, w, h) in faces:
        croppedFace = img[y:y + h, x:x + w]
        # print(x, y, w, h)
        return croppedFace


def dataCollect(name):
    #   Configure our Camera
    cap = cv2.VideoCapture(0)
    count = 0
    while cap:
        ret, img = cap.read()
        if face_extractor(img) is not None:
            count += 1
            face = cv2.resize(face_extractor(img), (200, 200))
            grayFace = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            if os.path.exists(os.getcwd() + '/dataSet/' + name):
                pass
            else:
                os.mkdir('dataSet/' + name)

            filePath = 'dataSet/' + name + '/user' + str(count) + '.jpg'
            cv2.imwrite(filePath, grayFace)
            cv2.imshow('img', img)
            cv2.imshow('face cropper', face)
            if (cv2.waitKey(1) == 13 & 0xFF == ord('q')) or count == 100:
                break

    cap.release()
    cv2.destroyAllWindows()
    return
