import streamlit as st

st.title("Hello Streamlit")

st.header("header")
st.subheader("sub header")
st.text("like this python code ")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag  
:moon:  
:sunglasses:
**bold**
_italics_   
""",True)

st.write(st)
d={'a':'aaple' , 'b':'ball' ,'c':'cat'}
st.write(d)