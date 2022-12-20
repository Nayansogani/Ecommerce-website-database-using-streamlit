import pandas as pd
import streamlit as st
import plotly.express as px
from database import pay_view_all_data


def paym_read():
    result = pay_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['payment_id','payment_date','Payment_type','Customer_id','Cart_id','total_amount'])
    with st.expander("View all Payment"):
        st.dataframe(df)
    