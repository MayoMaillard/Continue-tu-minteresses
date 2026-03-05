import streamlit as st
import random

# Configuration de l'onglet du navigateur
st.set_page_config(page_title="Test Jeu de Cartes", page_icon="🎲")

# --- DESIGN (CSS pour que ça ressemble à une carte) ---
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
    }
    .card-container {
        background-color: white;
        padding: 50px 20px;
        border-radius: 20px;
        border: 4px solid #FF4B4B;
        text-align: center;
        min-height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        margin: 20px 0;
    }
    .question-text {
        color: #1a1a1a;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TA LISTE DE TEST ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        "Quel est le pire cadeau que tu as jamais reçu ?",
        "Si tu pouvais être invisible pendant 1h, tu ferais quoi ?",
        "Raconte ta plus grosse honte au collège.",
        "Quel est l'achat le plus inutile que tu as fait récemment ?",
        "Si on t'offrait 1 million d'euros mais que tu devais vivre sans internet à vie, tu acceptes ?",
        "C'est quoi ton talent caché le plus absurde ?",
        "Quelle est la dernière recherche bizarre dans ton historique Google ?",
        "Si tu devais vivre dans un film, lequel choisirais-tu ?",
        "Quel est le plat que tu cuisines le mieux (ou le moins mal) ?",
        "Quelle est la règle de société la plus débile selon toi ?"
    ]

# --- LOGIQUE D'AFFICHAGE ---
st.title("🎲 Test du Jeu de Cartes")
st.write("Appuie sur le bouton pour piocher une question au hasard !")

if 'current_q' not in st.session_state:
    st.session_state.current_q = "Clique sur le bouton pour lancer le jeu !"

if st.button('🃏 PIOCHER UNE CARTE'):
    st.session_state.current_q = random.choice(st.session_state.questions)

# Affichage de la carte
st.markdown(f'''
    <div class="card-container">
        <div class="question-text">{st.session_state.current_q}</div>
    </div>
    ''', unsafe_allow_html=True)

st.caption("Fait avec ❤️ pour ton projet perso")
