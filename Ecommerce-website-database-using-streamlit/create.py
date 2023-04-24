import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        Seller_id = st.text_input("ID:")
        Name = st.text_input("Name:")
    with col2:
        s_pass = st.text_input("Pass:")
    Address = st.text_input("Address:")
    if st.button("Add Seller"):
        add_data(Seller_id,s_pass,Name,Address)
        st.success("Successfully added Seller: {}".format(Name))
