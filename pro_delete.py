import pandas as pd
import streamlit as st
from database import pro_view_all_data, view_only_product_names, pro_delete_data


def pr_delete():
    result = pro_view_all_data()
    df = pd.DataFrame(result, columns=['Product_id','Type','Color','P_Size','Gender','Commission','Cost','Quantity','Seller_id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_products = [i[0] for i in view_only_product_names()]
    selected_product = st.selectbox("Task to Delete", list_of_products)
    st.warning("Do you want to delete {}".format(selected_product))
    if st.button("Delete product"):
        pro_delete_data(selected_product)
        st.success("Product has been deleted successfully")
    new_result = pro_view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Product_id','Type','Color','P_Size','Gender','Commission','Cost','Quantity','Seller_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)