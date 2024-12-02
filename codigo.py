from groq import Groq
import streamlit as st

api_key = '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'

client = Groq(api_key=api_key)

st.title("Conversão de Imagem para Texto com Groq")
st.write("Envie uma imagem e veja a descrição gerada pelo modelo.")

uploaded_image = st.file_uploader("Envie uma imagem:", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Imagem carregada", use_column_width=True)
    image_bytes = uploaded_image.read()

    try:
        completion = client.chat.completions.create(
            model="llava-v1.5-7b-4096-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Descreva esta imagem:"},
                        {"type": "image", "image": {"file": image_bytes}},
                    ],
                }
            ],
            temperature=0.5,
            max_tokens=3000,
            top_p=0.9,
            stream=False,
            stop=None,
        )
        response_message = completion.choices[0].message["content"]
        st.success("Descrição da imagem:")
        st.write(response_message)
        
    except Exception as e:
        st.error(f"Erro ao processar a imagem: {e}")

col1, col2, col3, col4 = st.columns(4)

descriptions = {
    'button1': 'Descrição da obra Moema, 1866 (Victor Meirelles).',
    'button2': 'Descrição da obra Interior, 1925 (Anita Malfatti).',
    'button3': 'Descrição da obra Okê Oxóssi, 1970 (Abdias Nascimento).',
    'button4': 'Descrição da obra Zeferina, 2018 (Dalton Paula).',
}

def play_audio(description, button_key):
    st.audio(f"audio/{button_key}.mp3")

with col1:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_AL_MASP_00267_01.jpg", width=150)
    st.caption('Moema, 1866 (Victor Meirelles)')
    if st.button('Clique aqui', key='button1'):
        description = descriptions['button1']
        st.write(description)
        play_audio(description, 'button1')

with col2:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_C_01193_01.jpg", width=150)
    st.caption('Interior, 1925 (Anita Malfatti)')
    if st.button('Clique aqui', key='button2'):
        description = descriptions['button2']
        st.write(description)
        play_audio(description, 'button2')

with col3:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10811_01.jpg", width=150)
    st.caption('Okê Oxóssi, 1970 (Abdias Nascimento)')
    if st.button('Clique aqui', key='button3'):
        description = descriptions['button3']
        st.write(description)
        play_audio(description, 'button3')

with col4:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10808_01.jpg", width=150)
    st.caption('Zeferina, 2018 (Dalton Paula)')
    if st.button('Clique aqui', key='button4'):
        description = descriptions['button4']
        st.write(description)
        play_audio(description, 'button4')

with st.sidebar:
    st.header('HEART')
    st.write('Sejam bem-vind@s ao HEART!')
    st.write('Neste aplicativo, pinturas e imagens transpassam as barreiras do visual. Com o objetivo de garantir acessibilidade...')
    st.caption('Criado por Alinne Rohs, Luiza Torrão Britto, Pedro Bezerra')
