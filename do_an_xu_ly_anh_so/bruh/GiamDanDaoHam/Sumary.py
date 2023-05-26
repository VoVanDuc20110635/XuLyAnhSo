import streamlit as st
# import pandas as pd
# import GiamDanDaoHam.Theory as GDDH_LT
# # import GiamDanDaoHam.Bai01 as GDDH_01
# # import GiamDanDaoHam.Bai02 as GDDH_02
# import GiamDanDaoHam.Bai02a as GDDH_2a
# import GiamDanDaoHam.Bai03 as GDDH_03
# import GiamDanDaoHam.Bai04 as GDDH_04
# import GiamDanDaoHam.Bai05 as GDDH_05
# import GiamDanDaoHam.temp as GDDH_temp

def display():
    st.title("""Ví dụ minh họa""")
    st.header("""Giảm dần đạo hàm""")

    #lyThuyet ,tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5", "Ví dụ 6", "Ví dụ 7"])
    tab_titles = ["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Ví dụ 2a", "Ví dụ 3", "Ví dụ 4", "Ví dụ 5", "Temp",]
    tabs = st.tabs(tab_titles)
    with tabs[0]:
        import GiamDanDaoHam.Theory
        GiamDanDaoHam.Theory.executeThisFunction()

    with tabs[1]:
        st.title("Ví dụ minh họa")
        import GiamDanDaoHam.Bai01
        GiamDanDaoHam.Bai01.executeThisFunction()

    with tabs[2]:
        st.title("Ví dụ minh họa")
        import GiamDanDaoHam.Bai02
        GiamDanDaoHam.Bai02.executeThisFunction()

    with tabs[3]:
        import GiamDanDaoHam.Bai02a
        st.title("Ví dụ minh họa")
        GiamDanDaoHam.Bai02a.executeThisFunction()

    with tabs[4]:
        st.title("Ví dụ minh họa")
        import GiamDanDaoHam.Bai03
        GiamDanDaoHam.Bai03.executeThisFunction()

    with tabs[5]:
        st.title("Ví dụ minh họa")
        import GiamDanDaoHam.Bai04
        GiamDanDaoHam.Bai04.executeThisFunction()

    with tabs[6]:
        st.title("Ví dụ minh họa")
        import GiamDanDaoHam.Bai05
        GiamDanDaoHam.Bai05.executeThisFunction()

    with tabs[7]:
        st.title("Ví dụ minh họa")
        import GiamDanDaoHam.temp
        GiamDanDaoHam.temp.executeThisFunction()

