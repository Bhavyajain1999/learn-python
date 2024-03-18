import pandas as pd
import streamlit as st
import time
st.title('startup dashboard')
st.header('bhavya')
st.subheader('jain')
st.write('yeh sab doglapan hai')
st.markdown(""" 
### My fav cricketers
- virat kohli   
- ABD
- Yuvraj singh
 """)

st.code(""" 
printf('hello world')
 """)

st.latex('a^2 + b^2 = 1')

df = pd.DataFrame({'name': ['bhavya' ,'somu' , 'kohli'],'marks': [10 ,20 ,30]})

st.dataframe(df)

st.metric('revenue', 'rs 3l', '-3%')


st.json({'name': ['bhavya' ,'somu' , 'kohli'],'marks': [10 ,20 ,30]})

st.image('D:\\Coding journey 2024\\datascience\\stremlit\\image.jpg')
st.video('D:\\Coding journey 2024\\datascience\\stremlit\\video.mp4')

#creating layout

st.sidebar.title('ipl')
col1, col2 = st.columns(2)
with col1:
    st.image('D:\\Coding journey 2024\\datascience\\stremlit\\image.jpg')
with col2:
    st.video('D:\\Coding journey 2024\\datascience\\stremlit\\video.mp4') 

st.error('login failed')    
st.success('ho gya bhai login tu')

st.info('information')

st.warning('warning')

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.001)
    bar.progress(i)

#taking user input 
name = st.text_input('enter name')
age = st.number_input('age')   

btn = st.button('login')

if btn:
    if name =='bhavya' and age == 100:
        st.success('login ho gya')
        st.balloons()
    else:
        st.error('galat bhai')    


st.selectbox('select gender', ['male','female','others'])

file = st.file_uploader('upload a csv file') #to upload a file

