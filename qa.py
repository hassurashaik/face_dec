import streamlit as st
st.set_page_config(page_title="my webpage",layout="wide")
st.write("hello world")

with st.container():
    st.write('-----')
    st.write("container code")
with st.container():
    st.write("-----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("left column")
        st.write("left side")
    with right_column:
        st.header("right column")
        st.write("right side")