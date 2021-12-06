import streamlit as st
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

st.subheader(random.choice(excuse_list))
st.button('Generate another excuse')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.markdown('Created by @jlinehan9')
