import streamlit as st

st.title('Bem vindo')
st.header('Bem vindo')
st.subheader('Bem vindo')

st.markdown('# Isso é um texto markowb e um [#]') 
st.markdown('## Isso é um texto markowb e um [#]') 
st.markdown('### Isso é um texto markowb e um [#]') 


st.markdown('-----')

st.markdown('Markdown')
st.markdown('Markdown itálico_')
st.markdown('*Markdown itálico*')
st.markdown('_Markdown negrito_')
st.markdown('**Markdown negrito**')
st.markdown('__*Markdown italico e negrito*__')


st.markdown('Isso e um link pro [google](http://google.com)')

st.markdown('<h1 style="text-align:center; color:blue;">Isso é um texto HTML</h1>', unsafe_allow_html=True)

st.markdown('Olá, mundo :sunglasses:')
st.markdown('Olá, mundo :100:')

st.markdown("""
| MARKDOWN   | PEQUENO   | GRANDE     |
|------------|-----------|------------|
| *itálico*  | `CODE`    | **NEGRITO** |
""")
