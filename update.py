import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_seller_names, get_seller, edit_seller_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Seller_id','s_pass','Name','Address'])
    with st.expander("Current Sellers"):
        st.dataframe(df)
    list_of_sellers = [i[0] for i in view_only_seller_names()]
    selected_seller = st.selectbox("Seller to Edit", list_of_sellers)
    selected_result = get_seller(selected_seller)
    # st.write(selected_result)
    if selected_result:
        seller_id = selected_result[0][0]
        s_pass = selected_result[0][1]
        Name = selected_result[0][2]
        Address = selected_result[0][3]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_seller_id = st.text_input("ID:", seller_id)
            new_Name = st.text_input("Name:", Name)
        with col2:
            new_s_pass = st.text_input("Pass:", s_pass)
        new_address = st.text_input("Address:", Address)
        if st.button("Update seller"):
            edit_seller_data(new_seller_id, new_s_pass, new_Name, new_address, seller_id,s_pass,Name,Address)
            st.success("Successfully updated:: {} to ::{}".format(Name, new_Name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Seller_id','s_pass','Name','Address'])
    with st.expander("Updated data"):
        st.dataframe(df2)
