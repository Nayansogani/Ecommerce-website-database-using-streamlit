import pandas as pd
import streamlit as st
from database import view_all_data, view_only_seller_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Seller_id','s_pass','Name','Address'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_sellers = [i[0] for i in view_only_seller_names()]
    selected_seller = st.selectbox("Task to Delete", list_of_sellers)
    st.warning("Do you want to delete {}".format(selected_seller))
    if st.button("Delete Seller"):
        delete_data(selected_seller)
        st.success("Seller has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Seller_id','s_pass','Name','Address'])
    with st.expander("Updated data"):
        st.dataframe(df2)

        hvfyjdfyjf