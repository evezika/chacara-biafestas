import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Chácara Bia Festas",
    page_icon="🏡",
    layout="wide"
)


st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5EFE6;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
    }

    h1, h2, h3, p, label {
        color: #5C4033 !important;
    }

    .preco {
        color: #8B5E3C;
        font-size: 35px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏡 Chácara Bia Festas")

st.subheader(
    "Um espaço especial para celebrar momentos inesquecíveis."
)

st.image(
    "imagens/capa.jpg",
    use_container_width=True
)

st.header("🎥 Conheça nosso espaço")

st.video("videos/chacara.mp4")

st.header("✨ Sobre o espaço")

st.write(
    """
    Nossa chácara é o lugar perfeito para aniversários,
    confraternizações, encontros e momentos especiais.

    Um ambiente agradável para você aproveitar
    ao lado das pessoas que ama.
    """
)

st.header("🌿 Informações do espaço")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Capacidade", "50 pessoas")

with col2:
    st.metric("⏰ Duração", "12 horas")

with col3:
    st.metric("💰 Diária", "R$ 600,00")


st.write("**Horários disponíveis:**")

st.write(
    """
    🕘 9h às 19h

    🕙 10h às 20h
    """
)

st.header("🎁 Nossos pacotes")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏡 Diária")

    st.markdown(
        '<p class="preco">R$ 600,00</p>',
        unsafe_allow_html=True
    )

    st.write(
        "Aluguel do espaço por 12 horas "
        "para realização do seu evento."
    )

with col2:
    st.subheader("✨ Diária + Decoração")

    st.markdown(
        '<p class="preco">R$ 850,00</p>',
        unsafe_allow_html=True
    )

    st.write(
        "Aluguel da chácara + decoração "
        "no estilo Pegue e Monte."
    )

st.header("📌 Condições da reserva")

st.write(
    """
    💳 **30% do valor** para confirmar a data.

    📅 O valor restante deve ser pago até um dia antes do evento.

    💚 Pagamento via Pix.

    **Pix:** 11996656564
    """
)


st.header("📅 Reserve sua data")

st.write(
    "Entre em contato conosco para verificar "
    "a disponibilidade da data."
)

numero_whatsapp = "5511996656564"

mensagem = quote(
    """
Olá! Gostaria de verificar a disponibilidade
e agendar uma data para a Chácara Bia Festas. 🏡
"""
)

link_whatsapp = (
    f"https://wa.me/{numero_whatsapp}"
    f"?text={mensagem}"
)

st.link_button(
    "💬 Quero agendar minha data",
    link_whatsapp,
    use_container_width=True
)

st.divider()

st.write(
    "🏡 **Chácara Bia Festas**"
)

st.caption(
    "Momentos especiais merecem um lugar especial 🤎"
)