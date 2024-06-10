import streamlit as st
from gtts import gTTS
from PIL import Image
import requests
from io import BytesIO
import base64
from deep_translator import GoogleTranslator
from ollama import Client

# Configurar o cliente Ollama
client = Client(host='https://ef12-2804-14d-5c5c-9ce1-00-1006.ngrok-free.app')
translator = GoogleTranslator(source='en', target='pt')

# Função para gerar e reproduzir áudio
def play_audio(description, key):
    tts = gTTS(description, lang='pt')
    audio_file = f"audio_{key}.mp3"
    tts.save(audio_file)
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')

# Função para converter imagem em base64
def convert_to_base64(image_bytes):
    return base64.b64encode(image_bytes).decode()

# Função para descrever uma imagem
def describe_image(image_bytes):
    st.write("Descrevendo imagem...")  # Mensagem de log
    image_base64 = convert_to_base64(image_bytes)
    
    response = client.chat(
        model='llava',
        messages=[
            {'role': 'user', 'content': 'Describe the following work of art:', 'images': [image_base64]},
        ],
    )
    return translator.translate(response['message']['content'])

# Descrições das imagens pré-definidas
descriptions = {
    'button1': "A pintura mostra uma mulher nua deitada de barriga para cima, com o corpo ligeiramente inclinado para a direita em uma praia deserta. A iluminação da cena é dominada por tons quentes, sugerindo o pôr do sol. Seus cabelos negros e longos estão espalhados atrás de sua cabeça. Ela usa um adorno feito de penas na cintura. Ao fundo, o mar está calmo, com pequenas ondas lambendo a margem. Árvores densas e escuras margeiam a praia, criando uma atmosfera de mistério e tranquilidade. O céu quente complementa a cena serena e introspectiva.",
    'button2': "Esta pintura retrata uma cena de interior de uma casa. No primeiro plano, à esquerda, há uma cama com uma colcha escura decorada com padrões florais. Em frente à cama, um aparador de madeira com gavetas está encostado na parede. Em cima do aparador, um vaso contém um arranjo de flores diversas. Acima do aparador, na parede, estão pendurados dois retratos emoldurados: um homem de aparência séria e uma mulher loira com um vestido escuro. A parede está coberta com papel de parede com um padrão de folhas. No centro da composição, uma porta branca parcialmente aberta revela uma figura masculina de costas, vestida com um roupão, caminhando em um corredor com carpete.",
    'button3': "É uma obra abstrata que utiliza as cores e elementos da bandeira do Brasil. No centro da composição, há um grande círculo azul escuro, que é cortado por uma faixa. Sobre o círculo, uma seta vermelha aponta para cima, atravessando a faixa. O fundo é verde, com um losango amarelo no centro. Dentro do círculo azul, há estrelas brancas representando a constelação do Cruzeiro do Sul. A inscrição 'OKÊ OKÊ OKÊ OKÊ' está escrita em amarelo na faixa. A pintura utiliza formas geométricas simples e cores sólidas para criar uma imagem de forte impacto visual, evocando elementos nacionais brasileiros.",
    'button4': "A pintura representa um retrato de uma mulher negra, com cabelo curto e encaracolado, usando um vestido vinho de ombros à mostra com uma borda clara. O fundo é verde pastel bem claro. A mulher -Zefirina- está olhando diretamente para frente, com uma expressão séria. Ela usa brincos brancos pendurados em ambas as orelhas.",
}

st.title('HEART')

# Seção para upload de imagem ou link
st.header('Upload ou Link da Imagem')
image_source = st.radio("Escolha a fonte da imagem", ('Upload', 'Link'))

if image_source == 'Upload':
    uploaded_file = st.file_uploader("Escolha uma imagem...", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem carregada.', use_column_width=True)
        image_bytes = uploaded_file.getvalue()  # Lê o conteúdo do arquivo carregado
        description = describe_image(image_bytes)  # Passa o conteúdo do arquivo para a função
        st.write(description)
        play_audio(description, 'uploaded_image')
elif image_source == 'Link':
    image_url = st.text_input("Coloque o link da imagem")
    if image_url:
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            st.image(image, caption='Imagem do link.', use_column_width=True)
            description = describe_image(response.content)  # Passa o conteúdo da resposta para a função
            st.write(description)
            play_audio(description, 'linked_image')
        except Exception as e:
            st.error(f"Não foi possível carregar a imagem do link. Verifique o URL. Erro: {e}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_AL_MASP_00267_01.jpg", width=200)
    if st.button('Clique aqui', key='button1'):
        description = descriptions['button1']
        st.write(description)
        play_audio(description, 'button1')

with col2:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_C_01193_01.jpg", width=200)
    if st.button('Clique aqui', key='button2'):
        description = descriptions['button2']
        st.write(description)
        play_audio(description, 'button2')

with col3:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10811_01.jpg", width=200)
    if st.button('Clique aqui', key='button3'):
        description = descriptions['button3']
        st.write(description)
        play_audio(description, 'button3')

with col4:
    st.image("https://assets.masp.org.br/uploads/temp/WEB_JB_MASP_10808_01.jpg", width=200)
    if st.button('Clique aqui', key='button4'):
        description = descriptions['button4']
        st.write(description)
        play_audio(description, 'button4')

with st.sidebar:
    st.header('HEART')
    st.write('Sejam bem-vind@s ao HEART!')
    info = st.write('Neste aplicativo, pinturas e imagens transpassam as barreiras do visual. Com o objetivo de garantir acessibilidade, aqui, a arte pode ser ouvida e, assim, com essa maior proximidade com o público, pode ser sentida com o coração (HEAR + ART = HEART). Usa-se, desse modo, a Inteligência Artificial para garantir o direito à arte e cultura, por uma arte mais acessível e quebradora de barreiras sensoriais.')
    st.caption('Criado por Alinne Rohs, Luiza Torrão Britto, Pedro Bezerra')
