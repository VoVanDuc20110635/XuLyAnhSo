from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
import os
from PIL import Image

def executeThisFunction():
    st.title("""Giới thiệu""")

    st.write("Trước hết, cùng nhắc lại thuật toán GD để tối ưu hàm mất mát J(θ):")
    st.write("1. Dự đoán một điểm khởi tạo θ = θ0.")
    st.write("2. Cập nhật θ đến khi đạt được kết quả chấp nhận được:")
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(currentDir, "congThucMomentum.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.write("với ∇θJ(θ) là đạo hàm của hàm mất mát tại θ.")
    st.write("Trong GD, chúng ta cần tính lượng thay đổi ở thời điểm t để cập nhật vị trí mới cho nghiệm (tức hòn bi). Nếu chúng ta coi đại lượng này như vận tốc vt trong vật lý, vị trí mới của hòn bi sẽ là θt+1 = θt −vt , với giả sử rằng mỗi vòng lặp là một đơn vị thời gian. Dấu trừ thể hiện việc phải di chuyển ngược với đạo hàm. Việc tiếp theo là tính đại lượng vt sao cho nó vừa mang thông tin của độ dốc (tức đạo hàm), vừa mang thông tin của đà, tức vận tốc trước đó vt−1 (với giả sử rằng vận tốc ban đầu v0 = 0). Một cách đơn giản nhất, ta có thể lấy tổng có trọng số của chúng:")
    filepath = os.path.join(currentDir, "congThucMomentum2.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.write("Trong đó γ thường được chọn là một giá trị nhỏ hơn gần bằng một, thường là khoảng 0.9, vt−1 là vận tốc tại thời điểm trước đó, ∇θJ(θ) chính là độ dốc của điểm trước đó. Sau đó, vị trí mới của hòn bi được xác định bởi")
    filepath = os.path.join(currentDir, "congThucMomentum3.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.write("Sự khác nhau giữa GD thông thường và GD với momentem chỉ nằm ở thành phần cuối cùng của (12.8). Thuật toán đơn giản này tỏ ra rất hiệu quả trong các bài toán thực tế. Dưới đây là một ví dụ trong không gian một chiều. Xét một hàm đơn giản có hai điểm local minimum, trong đó một điểm là global minimum")
    filepath = os.path.join(currentDir, "congThucMomentum4.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.write("Gradient descent is an optimization algorithm that follows the negative gradient of an objective function in order to locate the minimum of the function.")
    st.write("A problem with gradient descent is that it can bounce around the search space on optimization problems that have large amounts of curvature or noisy gradients, and it can get stuck in flat spots in the search space that have no gradient.")
    st.write("Momentum is an extension to the gradient descent optimization algorithm that allows the search to build inertia in a direction in the search space and overcome the oscillations of noisy gradients and coast across flat spots of the search space.")
    st.write("In this tutorial, you will discover the gradient descent with momentum algorithm. After completing this tutorial, you will know:")
    filepath = os.path.join(currentDir, "LT1.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.subheader("Momentum")
    st.write("It is designed to accelerate the optimization process, e.g. decrease the number of function evaluations required to reach the optima, or to improve the capability of the optimization algorithm, e.g. result in a better final result.")
    st.write("A problem with the gradient descent algorithm is that the progression of the search can bounce around the search space based on the gradient. For example, the search may progress downhill towards the minima, but during this progression, it may move in another direction, even uphill, depending on the gradient of specific points (sets of parameters) encountered during the search.")
    st.write("Momentum involves adding an additional hyperparameter that controls the amount of history (momentum) to include in the update equation, i.e. the step to a new point in the search space. The value for the hyperparameter is defined in the range 0.0 to 1.0 and often has a value close to 1.0, such as 0.8, 0.9, or 0.99. A momentum of 0.0 is the same as gradient descent without momentum.")