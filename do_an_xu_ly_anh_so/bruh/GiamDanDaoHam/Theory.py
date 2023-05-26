import streamlit as st
import os
from PIL import Image

def executeThisFunction():
    st.title("""Giới thiệu""")
    currentDir = os.path.abspath(os.path.dirname(__file__))

    # filepath = os.path.join(currentDir, "GioiThieuGiamDanDaoHam.png")
    # image = Image.open(filepath)
    # st.image(image, caption='', use_column_width=True)
    st.write("      Trong machine learning nói riêng và toán tối ưu nói chung, chúng ta thường xuyên phải tìm các giá trị lớn nhất hoặc nhỏ nhất của một hàm số. Nếu chỉ xét riêng các hàm khả vi liên tục, việc giải phương trình đạo hàm bằng không thường rất phức tạp hoặc có thể ra vô số nghiệm. Thay vào đó, người ta thường cố gắng tìm các điểm local minimum, và ở một mức độ nào đó, coi đó là một nghiệm cần tìm của bài toán.")
    st.write("      Các điểm local minimum là nghiệm của phương trình đạo hàm bằng không (ta vẫn đang giả sử rằng các hàm này liên tục và khả vi). Nếu bằng một cách nào đó có thể tìm được toàn bộ (hữu hạn) các điểm cực tiểu, ta chỉ cần thay từng điểm local minimum đó vào hàm số rồi tìm điểm làm cho hàm có giá trị nhỏ nhất. Tuy nhiên, trong hầu hết các trường hợp, việc giải phương trình đạo hàm bằng không là bất khả thi.")
    filepath = os.path.join(currentDir, "AnhGiamDanDaoHamGioiThieu.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.write("      Nguyên nhân có thể đến từ sự phức tạp của dạng của đạo hàm, từ việc các điểm dữ liệu có số chiều lớn, hoặc từ việc có quá nhiều điểm dữ liệu. Thực tế cho thấy, trong nhiều bài toán machine learning, các nghiệm local minimum thường đã cho kết quả tốt, đặc biệt là trong neural networks.")
    st.write("      Hướng tiếp cận phổ biến nhất để giải quyết các bài toán tối ưu là xuất phát từ một điểm được coi là gần với nghiệm của bài toán, sau đó dùng một phép toán lặp để tiến dần đến điểm cần tìm, tức đến khi đạo hàm gần với không. Gradient descent (GD) và các biến thể của nó là một trong những phương pháp được dùng nhiều nhất.")

    st.subheader(" GD cho hàm một biến")
    st.write("Xét các hàm số một biến f : R → R. Quay trở lại Hình 12.1 và một vài quan sát đã nêu. Giả sử xt là điểm tìm được sau vòng lặp thứ t. Ta cần tìm một thuật toán để đưa xt về càng gần x ∗ càng tốt. Có hai quan sát sau đây: ")
    st.write("1. Nếu đạo hàm của hàm số tại xt là dương (f 0 (xt) > 0) thì xt nằm về bên phải so với x ∗ , và ngược lại. Để điểm tiếp theo xt+1 gần với x ∗ hơn, chúng ta cần di chuyển xt về phía bên trái, tức về phía âm. Nói các khác, ta cần di chuyển ngược dấu với đạo hàm:")

    filepath = os.path.join(currentDir, "congThuc1LT.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    st.write("2. xt càng xa x ∗ về phía bên phải thì f 0 (xt) càng lớn hơn 0 (và ngược lại). Vậy, lượng di chuyển ∆, một cách tự nhiên nhất, là tỉ lệ thuận với −f 0 (xt).")
    filepath = os.path.join(currentDir, "congThuc2LT.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)

    # filepath = os.path.join(currentDir, "GDHamMotBien.png")
    # image = Image.open(filepath)
    # st.image(image, caption='', use_column_width=True)
