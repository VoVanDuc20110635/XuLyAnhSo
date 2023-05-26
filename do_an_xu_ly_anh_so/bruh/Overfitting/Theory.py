import streamlit as st


def display():
    st.title("""Các khái niệm""")

    st.markdown\
        ("""
        # Giới thiệu

Linear regression là một thuật toán supervised (học có giám sát), ở đó quan hệ  giữa đầu vào và đầu ra được mô tả bởi 1 hàm tuyến tính. Thuật toán này còn được gọi là linear fitting hoặc linear least square

Xét bài toán ước lượng giá của một căn nhà rộng x1m2, có x2 phòng ngủ và cách trung tâm thành phố x3 km. Giả sử ta đã thu thập được số liệu từ 1000 căn nhà trong thành phố đó, liệu rằng khi có một căn nhà mới với các thông số về diện tích x1, số phòng ngủ x2 và khoảng cách tới trung tâm x3, chúng ta có thể dự đoán được giá y của căn nhà đó không?
        """)