import pandas as pd
import streamlit as st
from database import cus_view_all_data, view_only_customer_names, cus_delete_data


def cust_delete():
    result = cus_view_all_data()
    df = pd.DataFrame(result, columns=['Customer_id','c_pass','Name','Address','Pincode','Phone_number_s','cart_id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Task to Delete", list_of_customers)
    st.warning("Do you want to delete {}".format(selected_customer))
    if st.button("Delete Customer records"):
        cus_delete_data(selected_customer)
        st.success("Customer record has been deleted successfully")
    new_result = cus_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Customer_id','c_pass','Name','Address','Pincode','Phone_number_s','cart_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)