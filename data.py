import streamlit as st
import pandas as pd
import numpy as np

a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd=n.reshape((2,4))
dic= { "name":"tarun",
       "age" :34 ,
       "city" :'noida'
}
data = pd.read_csv("Dataset//Computer_Data.csv")

st.dataframe(data)
st.json(dic)
st.write(data)
