import pandas as pd
import streamlit as st
import plotly.express as px
from database import pro_view_all_data


def pr_read():
    result = pro_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Product_id','Type','Color','P_Size','Gender','Commission','Cost','Quantity','Seller_id'])
    with st.expander("View all Products"):
        st.dataframe(df)
    