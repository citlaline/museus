import streamlit as st

st.title('Title')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.image("https://assets.masp.org.br/uploads/temp/WEB_AL_MASP_00267_01.jpg", width=100)
   if st.button_1('Clique aqui'):
      st.write('Imagem selecionada')
      
with col2:
   st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_C_01193_01.jpg", width=100)
   if st.button_2('Clique aqui'):
      st.write_1('Imagem selecionada')

with col3:
   st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10811_01.jpg", width=100)
   if st.button_3('Clique aqui'):
      st.write_2('Imagem selecionada')

with col4:
   st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10808_01.jpg", width=100)
   if st.button_4('Clique aqui'):
      st.write_3('Imagem selecionada')

with col5:
   st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10802_01.jpg", width=100)
   if st.button_5('Clique aqui'):
      st.write_4('Imagem selecionada')

with st.sidebar:
   st.header('Salut')
   st.write_5('Seu aplicativo de dicas de saúde!')
   st.caption('Criado por ...')
