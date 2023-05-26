import streamlit as st

def display():
    st.title("""Ví dụ minh họa""")
    st.header("""Support vector machine""")

    #lyThuyet ,tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5", "Ví dụ 6", "Ví dụ 7"])
    tab_titles = ["Các khái niệm", "Ví dụ 1", "Ví dụ 1a", "Ví dụ 2", "Plot LinearSVC Support Vector",]
    tabs = st.tabs(tab_titles)
    with tabs[0]:
        import SVM.Theory
        SVM.Theory.executeThisFunction()

    with tabs[1]:
        st.title("Ví dụ minh họa")
        import SVM.Bai01
        SVM.Bai01.executeThisFunction()

    with tabs[2]:
        st.title("Ví dụ minh họa")
        import SVM.Bai01a
        SVM.Bai01a.executeThisFunction()

    with tabs[3]:
        import SVM.Bai02
        st.title("Ví dụ minh họa")
        SVM.Bai02.executeThisFunction()

    with tabs[4]:
        st.title("Ví dụ minh họa")
        import SVM.plot_linearsvc_support_vectors
        SVM.plot_linearsvc_support_vectors.executeThisFunction()



