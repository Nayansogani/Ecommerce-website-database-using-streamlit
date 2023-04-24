import streamlit as st
from database import pro_add_data


def pr_create():
    col1, col2 = st.columns(2)
    with col1:
        Product_id = st.text_input("ID:")
        Type = st.text_input("Type:")
        Color = st.text_input("Color:")
        P_Size = st.text_input("P_Size:")
    with col2:
        Gender = st.text_input("Gender:")
        Commission = st.number_input("Commission:")
        Cost = st.number_input("Cost:")
        Quantity = st.number_input("Quantity:")
    Seller_id = st.text_input("Seller_id:")
    if st.button("Add Product"):
        pro_add_data(Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id)
        st.success("Successfully added Product: {}".format(Product_id))
