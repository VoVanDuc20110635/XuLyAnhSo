import streamlit as st


def display():
    st.title("""Các phương pháp tránh overfitting""")

    st.header("1. Gather more data")
    st.markdown \
        ("""
        Dữ liệu ít là 1 trong trong những nguyên nhân khiến model bị overfitting. Vì vậy chúng ta cần tăng thêm dữ liệu để tăng độ đa dạng, phong phú của dữ liệu ( tức là giảm variance).
\nMột số phương pháp tăng dữ liệu:

- **Thu thập thêm dữ liệu** : chúng ta phải craw thêm dữ liệu hay tới thực tiễn để thu thập, quay video, chụp ảnh,...Tuy nhiên trong nhiều trường hợp thì việc thu thập thêm dữ liệu là infeasible nên phương pháp này không được khuyến khích.
- **Data Augmentation** : Augmentation là 1 phương thức tăng thêm dữ liệu từ dữ liệu có sẵn bằng cách rotation, flip, scale, skew,... images. Phương pháp này được sử dụng rất phổ biến trong xử lý ảnh cho Deep learning.
        """)
    st.image("bruh/assets/images/overfitting/1.png")
    st.markdown\
        ("""- **GAN:** GAN ( Generative Adverserial Network) là mô hình học không giám sát dùng để sinh dữ liệu từ nhiễu (noise). Nó là sự kết hợp của 2 model : Generative dùng để sinh ảnh từ nhiễu và Discriminator dùng để check ảnh được sinh ra có giống ảnh real hay không? GAN là mô hình hiên nay đang được sử dụng rất phổ biến và tính ứng dụng rất cao. Hiện có rất nhiều mô hình GAN như : CGAN, StyleGAN, StarGAN, CycleGAN,...""")

    st.header("2. Simple model")
    st.markdown\
        ("""
        Một trong những nguyên nhân khiến model của bạn trở nên overfitting là: model của bạn quá sâu, phức tạp ( chẳng hạn như nhiều layer, node) trong khi chỉ có chút xíu dữ liệu. Ví dụ như bạn chỉ có <1 triệu nhưng bạn đòi mua nhà thì chịu...

Cách giải quyết ở đây : một là tăng thêm dữ liệu như ở trên, 2 giảm độ phức tạp của model bằng cách bỏ đi 1 số layer, node. Còn bỏ bao nhiêu layer, node thì dựa vào kinh nghiệm hoặc 'try and change'.
        """)

    st.header("3. Use Regularization")
    st.markdown\
        ("""
        Kĩ thuật regularization là thêm vào hàm mất lát ( loss) một đại lượng nữa.
        """)
    st.image("bruh/assets/images/overfitting/2.png")
    st.markdown\
        ("""
        Đại lượng này sẽ tác động đến hàm loss. Cụ thể : nếu lamda lớn thì ảnh hưởng của đại lượng thêm vào lên hàm loss cũng lớn và ngược lại nếu lamda nhỏ thì ảnh hưởng của nó lên hàm loss cũng nhỏ. Nhưng lamda cũng không được quá lớn vì nếu quá lớn thì đại lượng thêm vào sẽ lấn át loss => mô hình xây dựng sẽ bị sai ( underfitting).

. **l2 regularization:**
        """)

    st.image("bruh/assets/images/overfitting/3.png")
    st.markdown("""Suy ra loss :""")
    st.image("bruh/assets/images/overfitting/4.png")
    st.markdown\
        ("""
        Việc tối ưu hóa model cũng đồng nghĩa với việc làm giảm hàm mất mát ( loss ) => giảm weight . Nên norm2 regularization còn được gọi là 'weight decay' ( trọng số tiêu biến ).

**l1 regularization**:Về cơ bản norm1 regularization cũng tương tự như chuẩn norm2 regularization. Nhưng đại lượng được thêm vào là tổng trị tuyệt đối của tất cả các phần tử.
        """)
    st.image("bruh/assets/images/overfitting/5.png")
    st.markdown\
        ("""
        Tóm lại: regularization là 1 kĩ thuật tránh overfitting bằng cách thêm vào hàm loss 1 đại lượng lamda. f(weight)
=> Tối ưu model ( giảm hàm loss ) => giảm weight => mô hình bớt phức tạp => tránh overfitting.
        """)

    st.header("4. Use Dropout")
    st.image("bruh/assets/images/overfitting/6.png")
    st.markdown(""""Dropout là kĩ thuật giúp tránh overfitting cũng gần giống như regularization bằng cách bỏ đi random p% node của layer => giúp cho mô hình bớt phức tạp (p thuộc [0.2, 0.5]).""")

    st.header("5. Early stoping")
    st.image("bruh/assets/images/overfitting/7.png")
    st.markdown\
        ("""
        Khi training model thì không phải lúc nào (hàm mất mát) loss của tập train và tập test cũng đồng thời giảm, tới một epoch nào đó thì loss của tập train sẽ tiếp tục giảm nhưng loss của tập test không giảm mà tăng trở lại => Đó là hiện tượng overfitting. 

Vì vậy để ngăn chặn nó, thì ngay tại thời điểm đó người ta sẽ dừng việc training (vì để chương trình tiếp tục training thì cũng không cải thiện được gì mà lại tốn tài nguyên).

# ****Kết luận****

Hiện tượng overfitting là hiện tượng rất phổ biến trong việc training model nên việc gặp phải (mắc phải) thì là điều hết sức bình thường. Không có gì phải sợ cả, các bạn hãy thử 1 vài phương pháp trên kết hợp lại như : Dropout + Regularization + Augmentation.
        """)