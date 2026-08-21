import streamlit as st
from urllib.parse import quote


# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Chácara Bia Festas",
    page_icon="🏡",
    layout="wide"
)


# ==========================================
# ESTILO DO SITE
# ==========================================

st.markdown("""
<style>

/* Fundo */
.stApp {
    background-color: #F5EFE6;
}

/* Área principal */
.block-container {
    max-width: 1100px;
    padding-top: 3rem;
}

/* Títulos */
h1, h2, h3 {
    color: #5C4033 !important;
}

/* Textos gerais */
p, label {
    color: #5C4033 !important;
}

/* Título principal */
.titulo {
    color: #5C4033;
    font-size: 55px;
    font-weight: bold;
}

.subtitulo {
    color: #7A6252;
    font-size: 20px;
}

/* Cards de informações */
.card {
    background-color: #FFFDF9;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(92, 64, 51, 0.12);
}

/* Pacotes */
.pacote {
    background-color: #FFFDF9;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 5px 18px rgba(92, 64, 51, 0.12);
}

.preco {
    color: #8B5E3C;
    font-size: 38px;
    font-weight: bold;
}

/* Caixa de reserva */
.reserva {
    background-color: #E8DCCB;
    padding: 25px;
    border-radius: 15px;
    color: #5C4033;
}

/* Botão */
[data-testid="stLinkButton"] a {
    background-color: #7B5138 !important;
    color: white !important;
    border-radius: 10px !important;
    min-height: 50px;
    font-size: 17px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# CABEÇALHO
# ==========================================

st.markdown("""
<div class="titulo">
🏡 Chácara Bia Festas
</div>

<div class="subtitulo">
Um espaço especial para celebrar momentos inesquecíveis.
</div>
""", unsafe_allow_html=True)


st.write("")


# ==========================================
# FOTO PRINCIPAL
# ==========================================

st.image(
    "imagens/capa.jpg",
    use_container_width=True
)


# ==========================================
# VÍDEO
# ==========================================

st.write("")

st.header("🎥 Conheça nosso espaço")

st.video(
    "videos/chacara.mp4"
)


# ==========================================
# APRESENTAÇÃO
# ==========================================

st.write("")

st.header("✨ Sobre o espaço")

st.write("""
Nossa chácara é o lugar perfeito para aniversários,
confraternizações, encontros e momentos especiais.
Um ambiente agradável para você aproveitar ao lado
das pessoas que ama.
""")


# ==========================================
# INFORMAÇÕES
# ==========================================

st.write("")

st.header("🌿 Informações do espaço")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>👥 Capacidade</h3>
    <p>Até 50 pessoas</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>⏰ Duração</h3>
    <p>12 horas de evento</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🕘 Horários</h3>
    <p>9h às 19h<br>ou<br>10h às 20h</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# PACOTES
# ==========================================

st.write("")
st.header("🎁 Nossos pacotes")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="pacote">
    <h2>🏡 Diária</h2>

    <div class="preco">
    R$ 600,00
    </div>

    <p>
    Aluguel do espaço por 12 horas
    para você realizar seu evento.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pacote">
    <h2>✨ Diária + Decoração</h2>

    <div class="preco">
    R$ 850,00
    </div>

    <p>
    Aluguel da chácara + decoração
    no estilo Pegue e Monte.
    </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# CONDIÇÕES DE RESERVA
# ==========================================

st.write("")
st.header("📌 Condições da reserva")

st.markdown("""
<div class="reserva">

💳 <b>30% do valor</b> para confirmar a data.

<br><br>

📅 O valor restante deve ser pago até um dia antes do evento.

<br><br>

💚 Pagamento via Pix.

</div>
""", unsafe_allow_html=True)


# ==========================================
# WHATSAPP
# ==========================================

numero_whatsapp = "5511996656564"

mensagem = quote(
    "Olá! Gostaria de verificar a disponibilidade "
    "e agendar uma data para a Chácara Bia Festas. 🏡"
)

link_whatsapp = (
    f"https://wa.me/{numero_whatsapp}"
    f"?text={mensagem}"
)

st.write("")
st.header("📅 Reserve sua data")

st.write(
    "Clique no botão abaixo para verificar a disponibilidade."
)

st.link_button(
    "💬 QUERO AGENDAR MINHA DATA",
    link_whatsapp,
    use_container_width=True
)


# ==========================================
# RODAPÉ
# ==========================================

st.write("")
st.divider()

st.markdown("""
<div style="text-align: center; color: #7A6252;">
🏡 <b>Chácara Bia Festas</b>
<br><br>
Momentos especiais merecem um lugar especial 🤎
</div>
""", unsafe_allow_html=True)