# Importing pakages
import streamlit as st
import mysql.connector

from create import create
#from database import create_table
from delete import delete
from read import read
from update import update
from pay_read import paym_read
from cus_read import cust_read
from pro_read import pr_read
from cus_update import cust_update
from cus_delete import cust_delete
from pro_delete import pr_delete
from pro_update import pr_update
from pro_create import pr_create
from database import sql_executor
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password"
# )
# c = mydb.cursor()
#
# c.execute("CREATE DATABASE ebike")


def seller():
    
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("", menu)

    if choice == "Add":
        st.subheader("Enter Seller Details:")
        create()

    elif choice == "View":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()

    else:
        st.subheader("About tasks")


def product():
    
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add":
        st.subheader("Enter Product Details:")
        pr_create()

    elif choice == "View":
        st.subheader("View created tasks")
        pr_read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        pr_update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        pr_delete()

    else:
        st.subheader("About tasks")

def customer():
    
    menu = ["View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View":
        st.subheader("View created tasks")
        cust_read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        cust_update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        cust_delete()

    else:
        st.subheader("About tasks")

def payment():
    
    menu = ["View"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View":
        st.subheader("View created tasks")
        paym_read()

    else:
        st.subheader("About tasks")

def query():
    
    st.text("Write a query")

    with st.form(key='query_form'):
            
        raw_code = st.text_area("Query")
        submit_code = st.form_submit_button("Execute")


    if submit_code:
        st.code(raw_code)
        query_results = sql_executor(raw_code) 
        st.write(query_results) 

        vhvhvhgv