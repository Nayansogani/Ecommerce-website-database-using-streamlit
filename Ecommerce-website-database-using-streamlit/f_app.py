import streamlit as st
import mysql.connector

from app import seller
from app import customer
from app import product
from app import payment
from app import query

def main():
    st.title("Admin view of Database of Ecommerce website")
    
    menu = ["Seller", "Product","Customer","Payment","SQL Queries"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Seller":
        st.subheader("Seller:")
        seller()

    elif choice == "Product":
        st.subheader("Product")
        product()

    elif choice == "Customer":
        st.subheader("Customer")
        customer()

    elif choice == "Payment":
        st.subheader("Payment")
        payment()


    elif choice == "SQL Queries":
        st.subheader("SQL Queries")
        query()


    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
