import datetime

import pandas as pd
import streamlit as st
from database import pro_view_all_data, view_only_product_names, get_product, edit_product_data


def pr_update():
    result = pro_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Product_id','Type','Color','P_Size','Gender','Commission','Cost','Quantity','Seller_id'])
    with st.expander("Current Products"):
        st.dataframe(df)
    list_of_product = [i[0] for i in view_only_product_names()]
    selected_product = st.selectbox("Product to Edit", list_of_product)
    selected_result = get_product(selected_product)
    # st.write(selected_result)
    if selected_result:
        Product_id = selected_result[0][0]
        Type = selected_result[0][1]
        Color = selected_result[0][2]
        P_Size = selected_result[0][3]
        Gender = selected_result[0][4]
        Commission = selected_result[0][5]
        Cost = selected_result[0][6]
        Quantity = selected_result[0][7]
        Seller_id = selected_result[0][8]
        # Layout of Create

        col1, col2,col3,col4 = st.columns(4)
        with col1:
            new_Product_id = st.text_input("ID:", Product_id)
            new_Type = st.text_input("Name:", Type)
        with col2:
            new_Color = st.text_input("Color:", Color)
        with col3:
            new_P_Size = st.text_input("Psize:",P_Size)
            new_Gender = st.text_input("Gender:",Gender)
        with col4:
            new_Commission = st.text_input("Commission:",Commission)
            new_Cost = st.text_input("Cost:",Cost)
            new_Quantity = st.text_input("Quantity:",Quantity)
        new_Seller_id = st.text_input("Seller id:", Seller_id)
        if st.button("Update Product"):
            edit_product_data(new_Product_id,new_Type,new_Color,new_P_Size,new_Gender,new_Commission,new_Cost,new_Quantity,new_Seller_id,Product_id,Type,Color,P_Size,Gender,Commission,Cost,Quantity,Seller_id)
            st.success("Successfully updated:: {} to {}".format(Product_id, new_Product_id))

    result2 = pro_view_all_data()
    df2 = pd.DataFrame(result2, columns=['Product_id','Type','Color','P_Size','Gender','Commission','Cost','Quantity','Seller_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
