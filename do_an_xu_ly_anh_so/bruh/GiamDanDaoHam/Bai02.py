
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
import os
from PIL import Image

def executeThisFunction():

    X = np.random.rand(1000)
    y = 4 + 3 * X + .5*np.random.randn(1000)

    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y.reshape(-1, 1))
    w, b = model.coef_[0][0], model.intercept_[0]
    x0 = 0
    x1 = 1
    y0 = w*x0 + b
    y1 = w*x1 + b

    plt.clf()
    plt.plot(X, y, 'bo', markersize = 2)
    plt.plot([x0, x1], [y0, y1], 'r')

    st.pyplot(plt)

    st.subheader("GD cho hàm nhiều biến")
    st.write("Giả sử ta cần tìm global minimum cho hàm f(θ) trong đó θ là tập hợp các tham số cần tối ưu. Đạo hàm của hàm số đó tại một điểm θ bất kỳ được ký hiệu là ∇θf(θ). Tương tự như hàm một biến, thuật toán GD cho hàm nhiều biến cũng bắt đầu bằng một điểm dự đoán θ0, sau đó, ở vòng lặp thứ t, quy tắc cập nhật là")
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(currentDir, "congthucHamGDNhieuBienpng.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)

    st.write("Trước hết, chúng ta tạo 1000 điểm dữ liệu được chọn gần với đường thẳng y = 4 + 3x")
    code = '''from sklearn.linear_model import LinearRegression
X = np.random.rand(1000)
y = 4 + 3 * X + .5*np.random.randn(1000) # noise added
model = LinearRegression()
model.fit(X.reshape(-1, 1), y.reshape(-1, 1))
w, b = model.coef_[0][0], model.intercept_[0]
sol_sklearn = np.array([b, w])
print(sol_sklearn)
'''
    st.code(code, language='python')

    st.write("Kết quả:")
    code = '''Solution found by sklearn: [ 3.94323245 3.12067542]'''
    st.code(code, language='python')
    st.write("")
    st.write("")

    st.write("Các điểm dữ liệu và đường thẳng tìm được bằng linear regression có phương trình y ≈ 3.94 + 3.12x được minh hoạ trong Hình 12.6. Nghiệm tìm được rất gần với mong đợi.")