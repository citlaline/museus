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
    'button1': "A pintura mostra uma mulher nua deitada de costas em uma praia deserta. A iluminação da cena é dominada por tons quentes de laranja e marrom, sugerindo o pôr do sol. A mulher está deitada na areia, com o corpo ligeiramente inclinado para a direita. Seus cabelos negros e longos estão espalhados atrás de sua cabeça. Ela usa um adorno colorido feito de penas na cintura. Ao fundo, o mar está calmo, com pequenas ondas lambendo a margem. Árvores densas e escuras margeiam a praia, criando uma atmosfera de mistério e tranquilidade. O céu, tingido de laranja e rosa, complementa a cena serena e introspectiva.",
    'button2': "Esta pintura retrata uma cena de interior de uma casa. No primeiro plano, à esquerda, há uma cama com uma colcha escura decorada com padrões florais. Em frente à cama, um aparador de madeira com gavetas está encostado na parede. Em cima do aparador, um vaso branco contém um arranjo de flores coloridas. Acima do aparador, na parede, estão pendurados dois retratos emoldurados: um homem de aparência séria e uma mulher loira com um vestido escuro. A parede está coberta com papel de parede com um padrão de folhas. No centro da composição, uma porta branca parcialmente aberta revela uma figura masculina de costas, vestida com um roupão azul claro, caminhando em um corredor com piso vermelho.",
    'button3': "É uma obra abstrata que utiliza as cores e elementos da bandeira do Brasil. No centro da composição, há um grande círculo azul escuro, que é cortado por uma faixa branca com a inscrição "ORDEM E PROGRESSO". Sobre o círculo, uma seta vermelha aponta para cima, atravessando a faixa branca. O fundo é verde, com um losango amarelo no centro. Dentro do círculo azul, há estrelas brancas representando a constelação do Cruzeiro do Sul. A inscrição "OKÊ OKÊ OKÊ OKÊ" está escrita em amarelo na faixa branca. A pintura utiliza formas geométricas simples e cores sólidas para criar uma imagem de forte impacto visual, evocando elementos nacionais brasileiros.",
    'button4': "A pintura retrata Zeferina, uma figura central contra um fundo escuro. Zeferina é uma mulher negra, vestida com roupas tradicionais que consistem em um vestido branco longo com detalhes coloridos. Ela usa um pano de cabeça que cobre parte de seus cabelos, também adornado com padrões e cores vivas. Seu semblante é sério e determinado, refletindo uma força interna e uma história de resistência.
No fundo, o cenário é neutro e escuro, destacando ainda mais a figura de Zeferina e a sua presença imponente. A luz na pintura é sutil, focando principalmente no rosto e no traje de Zeferina, criando um contraste dramático entre ela e o fundo. A pintura parece capturar não apenas a imagem física de Zeferina, mas também a sua essência, transmitindo um senso de história e luta.",
    'button5': "A pintura "Vizinhança" de Lucia Laguna é uma composição vibrante e detalhada que captura uma cena complexa de uma área urbana. A obra é repleta de cores vivas e formas abstratas, representando casas, ruas, árvores e outras estruturas que compõem uma vizinhança.
No primeiro plano, há uma série de linhas e formas geométricas que representam as casas e os telhados, pintadas com uma paleta de cores variadas, incluindo tons de vermelho, azul, verde e amarelo. As casas são estilizadas, com detalhes que sugerem janelas, portas e telhados.
No fundo da pintura, as cores e formas se fundem em um padrão mais abstrato, dando uma sensação de profundidade e movimento. A vegetação é representada por manchas de verde que sugerem árvores e arbustos, enquanto as ruas são indicadas por linhas sinuosas que percorrem a composição.
A iluminação na pintura é uniforme, sem sombras fortes, o que contribui para a sensação de um espaço plano e colorido. A obra transmite uma sensação de dinamismo e vida, capturando a essência de uma vizinhança vibrante e cheia de energia."
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
    st.header('ArtWatch')
    st.write('Aplicativo que descreve e fala das artes que quer ver. Literalmente!')
    st.caption('Criado por Alinne Rohs, Luiza Torrão Britto')
