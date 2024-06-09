import streamlit as st
from gtts import gTTS
import os

# Função para gerar e reproduzir áudio
def play_audio(description, key):
    tts = gTTS(description, lang='pt')
    audio_file = f"audio_{key}.mp3"
    tts.save(audio_file)
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')

# Descrições das imagens
descriptions = {
    'button1': "Esta é uma obra de arte impressionante do acervo do MASP...",
    'button2': "Aqui vemos uma pintura incrível que retrata...",
    'button3': "Esta imagem mostra uma cena icônica...",
    'button4': "Nesta obra, o artista conseguiu capturar...",
    'button5': "A pintura apresenta uma composição fascinante..."
}

st.title('Title')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_AL_MASP_00267_01.jpg", width=100)
    if st.button('Clique aqui', key='button1'):
        description = descriptions['button1']
        st.write(description)
        play_audio(description, 'button1')

with col2:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_C_01193_01.jpg", width=100)
    if st.button('Clique aqui', key='button2'):
        description = descriptions['button2']
        st.write(description)
        play_audio(description, 'button2')

with col3:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10811_01.jpg", width=100)
    if st.button('Clique aqui', key='button3'):
        description = descriptions['button3']
        st.write(description)
        play_audio(description, 'button3')

with col4:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10808_01.jpg", width=100)
    if st.button('Clique aqui', key='button4'):
        description = descriptions['button4']
        st.write(description)
        play_audio(description, 'button4')

with col5:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10802_01.jpg", width=100)
    if st.button('Clique aqui', key='button5'):
        description = descriptions['button5']
        st.write(description)
        play_audio(description, 'button5')

with st.sidebar:
    st.header('Salut')
    st.write('Seu aplicativo de dicas de saúde!')
    st.caption('Criado por ...')
