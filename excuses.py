import streamlit as st
from datetime import date
import random

st.title('Why BYU Beat Utah:')

excuse_list = [
    'Thicc Boi wasn\'t playing',
    'It was in Provo',
    'Non-conference games don\'t count',
    '#FireWhitt',
    'The refs sucked',
    'The church should cancel BYU sports',
    'They are a dirty team',
    'I didn\'t feel safe',
    'Mission trips',
    'Honestly, BYU outplayed Utah and deserved to win...',
    'The altitude',
    'The fans were too nice',
    'We would have won if we scored 10 more points',
    'Sitake is unprofessional and classless',
    'Blue is an ugly color',
    'Talent gap',
    'Deez Nuts',
    '1/10',
    'Covid'
]

excuses = st.subheader(random.choice(excuse_list))
excuses = st.button('Generate another excuse')

st.write('')

fb_last_loss = date(2019, 9, 29)
bb_last_loss = date(2019, 12, 4)

col1, col2 = st.columns(2)
with col1:
    st.metric('Days Since Utah beat BYU in Football:',
             (date.today() - fb_last_loss).days)
with col2:
    st.metric('Days Since Utah beat BYU in Basketball',
             (date.today() - bb_last_loss).days)

balloons = st.button('Utah fans click here')
if balloons:
    st.subheader('Enjoy the Rose Bowl!')
    st.write('Please mail all championship shirts, trophies, and rings to Kalani Sitake.')
    st.balloons()
    
st.markdown('Created by @jlinehan9')
