from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def executeThisFunction():
    plt.clf()
    np.random.seed(100)
    N = 1000
    X = np.random.rand(N)
    y = 4 + 3 * X + .5 * np.random.randn(N)

    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y.reshape(-1, 1))
    w, b = model.coef_[0][0], model.intercept_[0]
    print('b = %.4f va w = %.4f' % (b, w))

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
    print('Sol found by GD: w = ', w1[-1], ',\nafter %d iterations.' % (it1 + 1))
    for item in w1:
        print(item, cost(item))

    print(len(w1))

    A = N / (2 * N)
    B = np.sum(X * X) / (2 * N)
    C = -np.sum(y) / (2 * N)
    D = -np.sum(X * y) / (2 * N)
    E = np.sum(X) / (2 * N)
    F = np.sum(y * y) / (2 * N)

    b = np.linspace(0, 6, 21)
    w = np.linspace(0, 6, 21)
    b, w = np.meshgrid(b, w)
    z = A * b * b + B * w * w + C * b * 2 + D * w * 2 + E * b * w * 2 + F

    plt.contour(b, w, z, 45)
    bdata = []
    wdata = []
    for item in w1:
        plt.plot(item[0], item[1], 'ro', markersize=3)
        bdata.append(item[0])
        wdata.append(item[1])

    plt.plot(bdata, wdata, color='b')

    plt.xlabel('b')
    plt.ylabel('w')
    plt.axis('square')
    st.pyplot(plt)

    st.write("")
    st.write("")
    st.write("Ta sẽ thực hiện tìm nghiệm của linear regression sử dụng GD")
    code = '''def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)
    def cost(w):
    N = Xbar.shape[0]
    return .5/N*np.linalg.norm(y - Xbar.dot(w))**2
    '''
    st.code(code, language='python')
    st.write("")
    st.write("")
    st.write("Dưới đây là thuật toán GD cho bài toán.")
    code = '''def myGD(w_init, grad, eta):
    w = [w_init]
    for it in range(100):
    w_new = w[-1] - eta*grad(w[-1])
    if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:
    break
    w.append(w_new)
    return (w, it)
    one = np.ones((X.shape[0],1))
    Xbar = np.concatenate((one, X.reshape(-1, 1)), axis = 1)
    w_init = np.array([[2], [1]])
    (w1, it1) = myGD(w_init, grad, 1)
    print(’Sol found by GD: w = ’, w1[-1].T, ’,\nafter %d iterations.’ %(it1+1))
    '''
    st.code(code, language='python')
    st.write("")
    st.write("")
    st.write("Kết quả:")
    code = '''Sol found by GD: w = [ 3.99026984 2.98702942] ,
    after 49 iterations.
    '''
    st.code(code, language='python')

    st.write("")
    st.write("")
    st.write("Ở đây, chúng ta cùng làm quen với một khái niệm quan trọng: đường đồng mức (level sets).")
    st.write("Ta thường gặp khái niệm đường đồng mức trong các bản đồ tự nhiên. Các điểm có cùng độ cao so với mực nước biển thường được nối với nhau. Với các ngọn núi, đường đồng mức thường là các đường kín bao quanh đỉnh núi. Khái niệm tương tự cũng được sử dụng trong tối ưu. Đường đồng mức hay level sets của một hàm số là tập hợp các điểm làm cho hàm số có cùng giá trị. Tưởng tượng một hàm số với hai biến, đồ thị của nó là một bề mặt (surface) trong không gian ba chiều. Đường đồng mức có thể được xác định bằng cách cắt bề mặt này bằng một mặt phẳng song song với đáy và lấy giao điểm của chúng. Với dữ liệu hai chiều, hàm mất mát của linear regression là một hàm bậc hai của hai thành phần trong vector hệ số w. Đồ thị của nó là một bề mặt parabolic. Vì vậy, các đường đồng mức của hàm này là các đường ellipse có cùng tâm như trên Hình 12.7. Tâm này chính là đáy của parabolic và là giá trị nhỏ nhất của hàm mất mát. Các đường đồng mức được biểu diễn bởi các màu khác nhau với màu từ lam đậm đến lục, vàng, cam, đỏ, đỏ đậm thể hiện giá trị tăng dần.")
