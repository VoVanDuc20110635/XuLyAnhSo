import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

import streamlit as st

def executeThisFunction():
    plt.clf()
    ax = plt.axes(projection="3d")

    X = np.linspace(-2, 2, 21)
    Y = np.linspace(-2, 2, 21)
    X, Y = np.meshgrid(X, Y)
    Z = X * X + Y * Y
    ax.plot_wireframe(X, Y, Z)
    # placeholder = st.empty()
    # placeholder.pyplot(plt)
    # st.plotly_chart(plt, use_container_width=True)
    st.pyplot(plt)

    #plt.show()

    code = '''x = np.linspace(-2, 2, 21)
        y = np.linspace(-2, 2, 21)'''
    st.code(code, language="python")
    st.write("Sử dụng linspace để tạo ra 1 mảng có giá trị bắt đầu từ -2 đến 2 và mảng chứa 21 phần tử")

    code = '''X, Y = np.meshgrid(x, y)'''
    st.code(code, language="python")
    st.write(
        "Sử dụng meshgrid để tạo lưới hình chữ nhật với sự trợ giúp của các mảng 1-D đã cho đại diện cho lập chỉ mục Ma trận hoặc lập chỉ mục Đề-các")

    code = '''ax.plot_wireframe(X, Y, Z)'''
    st.code(code, language="python")
    st.write("Sử dụng ax.plot_wireframe() lấy một lưới các giá trị và chiếu nó lên bề mặt ba chiều được chỉ định và có thể làm cho các dạng ba chiều kết quả khá dễ hình dung.")


# if __name__ == "__main__":
#     executeThisFunction()