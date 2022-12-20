import datetime

import pandas as pd
import streamlit as st
from database import cus_view_all_data, view_only_customer_names, get_customer, edit_customer_data


def cust_update():
    result = cus_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Customer_id','c_pass','Name','Address','Pincode','Phone_number_s','cart_id'])
    with st.expander("Current Customers"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("customer to Edit", list_of_customers)
    selected_result = get_customer(selected_customer)
    # st.write(selected_result)
    if selected_result:
        Customer_id = selected_result[0][0]
        c_pass = selected_result[0][1]
        Name = selected_result[0][2]
        Address = selected_result[0][3]
        Pincode = selected_result[0][4]
        Phone_number_s = selected_result[0][5]
        cart_id = selected_result[0][6]
        # Layout of Create

        col1, col2, col3 = st.columns(3)
        with col1:
            new_Customer_id = st.text_input("ID:", Customer_id)
            new_Name = st.text_input("Name:", Name)
        with col2:
            new_c_pass = st.text_input("Pass:", c_pass)
            new_cart_id = st.text_input("Cart_id;",cart_id)
        with col3:
            new_Pincode = st.text_input("Pincode:", Pincode)
            new_Phone_number_s = st.text_input("Phone Number:", Phone_number_s)
        new_Address = st.text_input("Address:", Address)
        if st.button("Update customer"):
            edit_customer_data(new_Customer_id,new_c_pass,new_Name,new_Address,new_Pincode,new_Phone_number_s,new_cart_id,Customer_id,c_pass,Name,Address,Pincode,Phone_number_s,cart_id)
            st.success("Successfully updated:: {} to ::{}".format(Name, new_Name))

    result2 = cus_view_all_data()
    df2 = pd.DataFrame(result2, columns=['Customer_id','c_pass','Name','Address','Pincode','Phone_number_s','cart_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
