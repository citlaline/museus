import streamlit as st

st.title('Title')

with st.sidebar:
   st.header('Salut')
   st.writer('Seu aplicativo de dicas de saúde!')
   st.caption('Criado por ...')

image = open('https://assets.masp.org.br/uploads/temp/WEB_IM_MASP_10834_01.jpg', 'rb').read()
if st.button('Click me'):
    st.write('Button clicked!')

st.image(image, caption='Your Image', use_column_width=True)


txt = st.text_area(
    "Descrição",
    "",
    )

st.write('Nosso aplicativo tem como foco oferecer ...')

tab1, tab2, tab3 = st.tabs(["Acervo", "Link"])

with tab1:
   st.header("Acervo")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("Link")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   
