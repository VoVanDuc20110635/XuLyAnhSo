import joblib
import os
import tensorflow as tf
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from tensorflow import keras

mnist = keras.datasets.mnist
(X_train , Y_train) , (X_test , Y_test) = mnist.load_data()

# 784 = 28x28
RESHAPED = 784
X_train = X_train.reshape(60000 , RESHAPED)
X_test = X_test.reshape(10000 , RESHAPED)

# now, let's take 10% of the training Data and use that for validation
(trainData , valData , trainLabels , valLabels) = train_test_split(X_train , Y_train , test_size=0.1 , random_state=84)

model = KNeighborsClassifier()
model.fit(trainData, trainLabels)

# save model, sau này ta sẽ load model để dùng
if os.path.exists("Model/knn_mnist.pkl"):
    os.remove("Model/knn_mnist.pkl")
joblib.dump(model, "Model/knn_mnist.pkl")

# Đánh giá trên tập validation
predicted = model.predict(valData)
do_chinh_xac = accuracy_score(valLabels , predicted)
print('Độ chính xác trên tập validation: %.0f%%' % (do_chinh_xac * 100))

# Đánh giá trên tập test
predicted = model.predict(X_test)
do_chinh_xac = accuracy_score(Y_test , predicted)
print('Độ chính xác trên tập test: %.0f%%' % (do_chinh_xac * 100))
