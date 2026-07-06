import streamlit as st
import json
import os
from datetime import datetime
from collections import Counter

DATA_FILE = "counter_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"contador": 0, "history": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def top3_tage(history):
    tage = Counter(entry["date"] for entry in history)
    return tage.most_common(3)


st.set_page_config(page_title="contador Benedikt", page_icon="🔢", layout="centered")

if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

st.title("🔢 contador Benedikt")
st.markdown("---")

st.markdown(
    f"<h1 style='text-align:center; font-size:96px;'>{data['contador']}</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Incrementar", use_container_width=True):
        data["contador"] += 1
        now = datetime.now()
        data["history"].append({
            "timestamp": now.strftime("%Y-%m-%dT%H:%M:%S"),
            "date": now.strftime("%Y-%m-%d"),
            "value": data["contador"],
        })
        save_data(data)
        st.rerun()

with col2:
    if st.button("🔄 Restablecer", use_container_width=True):
        data["contador"] = 0
        save_data(data)
        st.rerun()

st.markdown("### Establecer valor inicial")
nuevo_valor = st.number_input(
    "Ingresa un número:",
    value=data["contador"],
    step=1,
)
if st.button("✅ Aplicar valor", use_container_width=True):
    data["contador"] = int(nuevo_valor)
    save_data(data)
    st.rerun()

st.markdown("---")
st.markdown("### 🏆 Top 3 Tage")

top3 = top3_tage(data["history"])
if not top3:
    st.info("Noch keine Einträge vorhanden.")
else:
    medals = ["🥇", "🥈", "🥉"]
    for i, (date, count) in enumerate(top3):
        st.markdown(f"{medals[i]} **{date}** — {count} Klick{'s' if count != 1 else ''}")

if data["history"]:
    st.markdown("---")
    with st.expander("Verlauf anzeigen"):
        for entry in reversed(data["history"][-20:]):
            st.text(f"{entry['timestamp']}  →  Wert: {entry['value']}")
