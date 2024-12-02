from groq import Groq
import streamlit as st

api_key = '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'

client = Groq(api_key=api_key)

st.title("Conversão de Imagem para Texto com Groq")
st.write("Envie uma imagem e veja a descrição gerada pelo modelo.")

uploaded_image = st.file_uploader("Envie uma imagem:", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Imagem carregada", use_column_width=True)
    try:
        completion = client.chat.completions.create(
            model="llava-v1.5-7b-4096-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Descreva esta imagem:"},
                        {"type": "image_url", "image_url": {"url": image_url}},
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
