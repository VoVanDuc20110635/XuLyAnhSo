import numpy as np
import matplotlib.pyplot as plt
import streamlit as st



def executeThisFunction():
    plt.clf()
    x = np.linspace(-2, 2, 21)
    y = np.linspace(-2, 2, 21)
    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + Y ** 2
    plt.contour(X, Y, Z, 10)
    st.pyplot(plt)

    code = '''x = np.linspace(-2, 2, 21)
    y = np.linspace(-2, 2, 21)'''
    st.code(code, language="python")
    st.write("Sử dụng linspace để tạo ra 1 mảng có giá trị bắt đầu từ -2 đến 2 và mảng chứa 21 phần tử")

    code = '''X, Y = np.meshgrid(x, y)'''
    st.code(code, language="python")
    st.write("Sử dụng meshgrid để tạo lưới hình chữ nhật với sự trợ giúp của các mảng 1-D đã cho đại diện cho lập chỉ mục Ma trận hoặc lập chỉ mục Đề-các")

    code = '''plt.contour(X, Y, Z, 10)'''
    st.code(code, language="python")
    st.write("Contour là “tập các điểm-liên-tục tạo thành một đường cong (curve) (boundary), và không có khoảng hở trong đường cong đó, đặc điểm chung trong một contour là các các điểm có cùng /gần xấu xỉ một giá trị màu, hoặc cùng mật độ. Sử dụng hàm plt.contour() để tìm ra những đường cong đó")

