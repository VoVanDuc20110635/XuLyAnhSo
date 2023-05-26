import streamlit as st


def display():
    st.title("Overfitting")
    tab1, tab2, tab3 = st.tabs(["Overfitting là gì", "Ví dụ", "Cách tránh Overfitting"])
    with tab1:
        import Overfitting.Theory
        Overfitting.Theory.display()
    with tab2:
        st.title("Ví dụ")
        option = st.selectbox("Chọn bậc của đa thức", [2, 4, 8, 16])
        if option == 2:
            import Overfitting.Bai01a
            Overfitting.Bai01a.display()
        elif option == 4:
            import Overfitting.Bai01b
            Overfitting.Bai01b.display()
        elif option == 8:
            import Overfitting.Bai01c
            Overfitting.Bai01c.display()
        elif option == 16:
            import Overfitting.Bai01d
            Overfitting.Bai01d.display()

    with tab3:
        import Overfitting.avoidOverfitting as avOf
        avOf.display()
