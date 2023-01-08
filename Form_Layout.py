import streamlit as st
#py -m streamlit run Form_Layout.py

st.title('Registration Form')
first,last = st.columns(2)
first.text_input("First name")
last.text_input("Last name")

email,mob =st.columns([3,1])
email.text_input('email_id')
mob.text_input('Mobile number')

user,pw,pw2=st.columns(3)
user.text_input('username')
pw.text_input('password',type='password')
pw2.text_input("Retype Your Paasword",type='password')

ch,bl,sub= st.columns(3)
ch.checkbox("i agree")
if sub.button('submit'):
    st.write("")
    st.write('submitted successfully')