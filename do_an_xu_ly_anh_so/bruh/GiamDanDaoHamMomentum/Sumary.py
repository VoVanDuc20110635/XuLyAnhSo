import streamlit as st
import pandas as pd

import GiamDanDaoHamMomentum.Bai01 as GDDHM_01
import GiamDanDaoHamMomentum.Theory as GDDHM_LT

def display():
    st.title("""Ví dụ minh họa""")
    st.header("""Giảm dần đạo hàm momentum""")

    lyThuyet ,tab1 = st.tabs(["Các khái niệm", "Ví dụ "])
    with lyThuyet:
        GDDHM_LT.executeThisFunction()
    with tab1:
        st.title("Ví dụ minh họa")
        GDDHM_01.executeThisFunction()


