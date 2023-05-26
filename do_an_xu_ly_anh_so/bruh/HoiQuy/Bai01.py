import numpy as np
import streamlit as st


def display():
    # height (cm), input Data, each row is a Data point
    # X là ma trận chiều cao
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]])

    # Tạo chuỗi các phần tử = 1 với kích thước bằng với shape của X
    one = np.ones((1, X.shape[1]))

    # Nối chuỗi one với chuỗi X theo chiều dọc
    Xbar = np.concatenate((one, X), axis=0)  # each point is one row

    # y là ma trận cân nặng, theo chiều chuyển vị với X
    y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

    # Tích vô hướng Xbar với Xbar chuyển vị
    A = np.dot(Xbar, Xbar.T)

    # Tích vô hướng Xbar với y chuyển vị
    b = np.dot(Xbar, y)

    w = np.dot(np.linalg.pinv(A), b)

    # weights
    w_0, w_1 = w[0], w[1]
    print(w_0, w_1)

    y1 = w_1 * 155 + w_0
    y2 = w_1 * 160 + w_0

    print('Input 155cm, true output 52kg, predicted output %.2fkg' % y1)
    print('Input 160cm, true output 56kg, predicted output %.2fkg' % y2)

    x_input = 0
    x_input = st.number_input("Nhập chiều cao để dự đoán cân nặng: ")

    if (x_input <= 0):
        st.warning("Chiều cao phải là số dương")
    else:
        y_output = w_1 * x_input + w_0
        st.success("Với chiều cao vừa nhập, cân nặng được dự đoán là %.2fkg" % y_output)
