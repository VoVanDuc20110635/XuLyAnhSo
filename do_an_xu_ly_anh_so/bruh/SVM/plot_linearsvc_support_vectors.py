"""
=====================================
Plot the support vectors in LinearSVC
=====================================

Unlike SVC (based on LIBSVM), LinearSVC (based on LIBLINEAR) does not provide
the support vectors. This example demonstrates how to obtain the support
vectors in LinearSVC.

"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC
from sklearn.inspection import DecisionBoundaryDisplay
import streamlit as st
import os
from PIL import Image

def executeThisFunction():
    plt.clf()
    X, y = make_blobs(n_samples=40, centers=2, random_state=0)

    plt.figure(figsize=(10, 5))
    # "hinge" is the standard SVM loss
    clf = LinearSVC(C=100, loss="hinge", random_state=42).fit(X, y)
    # obtain the support vectors through the decision function
    decision_function = clf.decision_function(X)
    # we can also calculate the decision function manually
    # decision_function = np.dot(X, clf.coef_[0]) + clf.intercept_[0]
    # The support vectors are the samples that lie within the margin
    # boundaries, whose size is conventionally constrained to 1
    support_vector_indices = np.where(np.abs(decision_function) <= 1 + 1e-15)[0]
    support_vectors = X[support_vector_indices]

    plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
    ax = plt.gca()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        ax=ax,
        grid_resolution=50,
        plot_method="contour",
        colors="k",
        levels=[-1, 0, 1],
        alpha=0.5,
        linestyles=["--", "-", "--"],
    )
    plt.scatter(
        support_vectors[:, 0],
        support_vectors[:, 1],
        s=100,
        linewidth=1,
        facecolors="none",
        edgecolors="k",
    )
    plt.title("C = 100")

    plt.tight_layout()
    # plt.show()

    st.pyplot(plt)

    code = '''X, y = make_blobs(n_samples=40, centers=2, random_state=0)'''
    st.code(code, language="python")
    st.write(
        "Sử dụng make_blobs để tạo các đốm màu với phân phối Gaussian. Bạn có thể kiểm soát số lượng đốm màu sẽ tạo và số lượng mẫu sẽ tạo, cũng như một loạt các thuộc tính khác.")
    code = '''clf = LinearSVC(C=100, loss="hinge", random_state=42).fit(X, y)'''
    st.code(code, language="python")
    st.write("hinge là standard SVM loss. Linear Support Vector Machine (Linear SVC) là một thuật toán cố gắng tìm một siêu phẳng để tối đa hóa khoảng cách giữa các mẫu được phân loại.")
    code = '''support_vector_indices = np.where(np.abs(decision_function) <= 1 + 1e-15)[0]'''
    st.code(code, language="python")
    st.write("Sử dụng một mảng support vector indices để lưu những điểm có khoảng cách với boundary nhỏ hơn 1 + 1e-15")
    code = '''plt.scatter(
        support_vectors[:, 0],
        support_vectors[:, 1],
        s=100,
        linewidth=1,
        facecolors="none",
        edgecolors="k",
    )'''
    st.code(code, language = "python")
    st.write("Biểu đồ phân tán là biểu đồ trong đó mỗi giá trị trong tập dữ liệu được biểu thị bằng một dấu chấm. Mô-đun Matplotlib có một phương thức để vẽ các biểu đồ phân tán, nó cần hai mảng có cùng độ dài, một cho các giá trị của trục x và một cho các giá trị của trục y: x = [5,7,8, 7,2,17,2,9,4,11,12,9,6]")
