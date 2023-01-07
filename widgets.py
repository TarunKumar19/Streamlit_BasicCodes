import streamlit as st

st.title("widgets")
if st.button("Subscribe"):
    st.write("welcome")

name =st.text_input('type your name')
st.write(name)

address=st.text_area('type your address')
st.write(address)

st.date_input('enter date')
st.time_input('enter time')

if st.checkbox('Accept the T&C',value=False):
    st.write('thank you for accepting')

v1=st.radio('select colours',["r","g","b"],index=2)
v2=st.selectbox('select colours',["r","g","b"],index=0)
st.write(v1,v2)
v3=st.multiselect('colours',["r","g","b"])
st.write(v3)

v4=st.slider('age',min_value=10,max_value=70,value=20,step=2)
st.write(v4)

st.number_input("numbers",min_value=10,max_value=70,value=20,step=2)
ima=st.file_uploader('upload a file')
st.image(ima)
