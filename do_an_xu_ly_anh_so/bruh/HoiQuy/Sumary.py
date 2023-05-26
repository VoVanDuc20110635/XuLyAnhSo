import streamlit as st


def display():
    st.title("Hồi quy tuyến tính")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5"])
    with tab1:
        import HoiQuy.Theory
        HoiQuy.Theory.display()
    with tab2:
        st.title("Ví dụ minh họa")
        import HoiQuy.Bai01
        HoiQuy.Bai01.display()
    with tab3:
        st.title("Ví dụ minh họa")
        import HoiQuy.Bai02
        HoiQuy.Bai02.display()
    with tab4:
        st.title("Ví dụ minh họa")
        import HoiQuy.Bai03
        HoiQuy.Bai03.display()
    with tab5:
        st.title("Ví dụ minh họa")
        import HoiQuy.Bai04
        HoiQuy.Bai04.display()
    with tab6:
        st.title("Ví dụ minh họa")
        import HoiQuy.Bai05
        HoiQuy.Bai05.display()
