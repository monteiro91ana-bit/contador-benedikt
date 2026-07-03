import streamlit as st

st.set_page_config(page_title="contador Benedikt", page_icon="🔢", layout="centered")

if "contador" not in st.session_state:
    st.session_state.contador = 0

st.title("🔢 contador Benedikt")
st.markdown("---")

st.markdown(
    f"<h1 style='text-align:center; font-size:96px;'>{st.session_state.contador}</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Incrementar", use_container_width=True):
        st.session_state.contador += 1
        st.rerun()

with col2:
    if st.button("🔄 Restablecer", use_container_width=True):
        st.session_state.contador = 0
        st.rerun()

st.markdown("### Establecer valor inicial")
nuevo_valor = st.number_input(
    "Ingresa un número:",
    value=st.session_state.contador,
    step=1,
)
if st.button("✅ Aplicar valor", use_container_width=True):
    st.session_state.contador = int(nuevo_valor)
    st.rerun()
