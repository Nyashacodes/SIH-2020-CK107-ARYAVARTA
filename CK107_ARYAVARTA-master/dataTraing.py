import cv2
import os
import pickle
import numpy as np
# from PIL import  Image
import tkinter.messagebox as tmsg


def alertModel():
    tmsg.showinfo("model Info","Model training Complete")



def dataTrain():
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    image_dir = os.path.join(BASE_DIR, 'dataSet')

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith(".jpg"):
                path = os.path.join(root, file)
                # labels from directory
                label = os.path.basename(os.path.dirname(path))
                # print(path, label)

                if label not in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]

                img_arr = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                size = (200, 200)
                final_image = cv2.resize(img_arr, size)

                image_array = np.array(final_image, "uint8")
                # print(image_array)

                x_train.append(image_array)
                y_labels.append(id_)

        # print(x_train)
        # print(y_labels)
    with open("label.pickle", 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainer.yml")
    # print("model trained complete")
    alertModel()