from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st



def executeThisFunction():
    plt.clf()
    X = np.random.rand(1000)
    y = 4 + 3 * X + .5 * np.random.randn(1000)  # noise added

    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y.reshape(-1, 1))

    w, b = model.coef_[0][0], model.intercept_[0]
    sol_sklearn = np.array([b, w])


    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X.reshape(-1, 1)), axis=1)

    def grad(w):
        N = Xbar.shape[0]
        return 1 / N * Xbar.T.dot(Xbar.dot(w) - y)

    def cost(w):
        N = Xbar.shape[0]
        return .5 / N * np.linalg.norm(y - Xbar.dot(w)) ** 2

    def myGD(w_init, eta):
        w = [w_init]
        for it in range(100):
            w_new = w[-1] - eta * grad(w[-1])
            if np.linalg.norm(grad(w_new)) / len(w_new) < 1e-3:
                break
            w.append(w_new)
        return (w, it)

    w_init = np.array([0, 0])
    (w1, it1) = myGD(w_init, 1)
    st.write('Solution found by sklearn:', sol_sklearn)
    st.write('Sol found by GD: w = ', w1[-1], ',\nafter %d iterations.' % (it1 + 1))

    code = '''X = np.random.rand(1000)
    y = 4 + 3 * X + .5 * np.random.randn(1000)'''
    st.code(code, language = "python")
    st.write("Tạo ra một bộ sinh số ngẫu nhiên X có một ngàn phần tử và tương ứng là bộ y có giá trị đã được tính ra từ công thức với biến X")

    code = '''model = LinearRegression()
    model.fit(X.reshape(-1, 1), y.reshape(-1, 1))'''
    st.code(code, language="python")
    st.write("Sử dụng hàm reshape để chuyển các mảng X,Y từ mảng thành mảng 2 chiều")

    code = ''' def grad(w):
        N = Xbar.shape[0]
        return 1 / N * Xbar.T.dot(Xbar.dot(w) - y)'''
    st.code(code, language="python")
    st.write("Sử dụng hàm grad để tính đạo hàm.")
    code  = '''    def cost(w):
        N = Xbar.shape[0]
        return .5 / N * np.linalg.norm(y - Xbar.dot(w)) ** 2'''
    st.code(code, language="python")
    st.write("Sử dụng cost để tính giá trị của hàm số. Hàm này không sử dụng trong thuật toán nhưng thường được dùng để kiểm tra việc tính đạo hàm của đúng không hoặc để xem giá trị của hàm số có giảm theo mỗi vòng lặp hay không.")
    st.write("")
    st.write("")
    code = '''    def myGD(w_init, eta):
        w = [w_init]
        for it in range(100):
            w_new = w[-1] - eta * grad(w[-1])
            if np.linalg.norm(grad(w_new)) / len(w_new) < 1e-3:
                break
            w.append(w_new)
        return (w, it)'''
    st.code(code, language = "python")
    st.write("myGD là phần chính thực hiện thuật toán Gradient Desent nêu phía trên. Đầu vào của hàm số này là learning rate và điểm bắt đầu. Thuật toán dừng lại khi đạo hàm có độ lớn đủ nhỏ.")



