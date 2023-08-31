import streamlit as st
st.write("TDS Assignment  8")
p=st.number_input("Enter first number")
q=st.number_input("Enter second number")
r=st.number_input("Enter third number") 
if (p >= q) and (p >= r):
   largest = p
elif (q >= p) and (q >= r):
   largest = q
else:
   largest = r
st.write("The largest number is", largest)
st.write("By Ishika Minocha")
