import pickle
import cv2


def identification():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    # labels = {"person_name": 1}
    with open("label.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            # print(x, y, w, h)
            roi_gray = gray[y:y + h, x:x + w]

            # recognize ? deep learned model predict keras tensorflow pytorch scikit learn

            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45:
                print(id_)
                print(labels[id_])
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, color, stroke, cv2.LINE_AA)
                # cv2.putText(frame, str(ttm), (100, 450), font, 1, (250, 120, 0), 1)
            cv2.putText(frame, str(conf), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 120, 255), 2)
            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
            subitems_faces = eye_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
            for (sx, sy, sw, sh) in subitems_faces:
                cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
