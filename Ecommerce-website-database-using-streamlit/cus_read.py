import pandas as pd
import streamlit as st
import plotly.express as px
from database import cus_view_all_data


def cust_read():
    result = cus_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Customer_id','c_pass','Name','Address','Pincode','Phone_number_s','cart_id'])
    with st.expander("View all Customers"):
        st.dataframe(df)
    