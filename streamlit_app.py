import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Continue tu m'intéresses", page_icon="✨", layout="centered")

# --- DESIGN PREMIUM ET MOBILE-FIRST (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #0e1117 0%, #1a1c23 100%);
    }
    
    [data-testid="column"] {
        width: fit-content !important;
        flex: 1 1 auto !important;
        min-width: 0px !important;
    }
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        gap: 10px !important;
    }

    .card-container {
        background-color: #fdfdfd;
        padding: 40px 25px;
        border-radius: 24px;
        border-bottom: 6px solid #f39c12; 
        text-align: center;
        min-height: 280px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 20px 40px rgba(0,0,0,0.4);
        margin: 10px 0;
    }
    
    .question-text {
        color: #2c3e50;
        font-size: 22px;
        font-weight: 600;
        font-family: 'Helvetica Neue', sans-serif;
        line-height: 1.4;
    }

    .stButton button[kind="primary"] {
        background-color: #f39c12 !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        height: 3.8em !important;
        width: 100% !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 15px rgba(243, 156, 18, 0.3) !important;
    }

    .stButton button[kind="secondary"] {
        background-color: #2c3e50 !important;
        color: #bdc3c7 !important;
        border: 1px solid #34495e !important;
        border-radius: 15px !important;
        height: 3.8em !important;
        width: 100% !important;
    }

    h1 { font-family: 'Georgia', serif; font-weight: 700; color: white; margin-bottom: 0px; text-align: center; }
    .instruction { color: #7f8c8d; font-style: italic; font-size: 0.9rem; margin-bottom: 20px; text-align: center; }
    .progress-text { color: #7f8c8d; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- TA LISTE DE QUESTIONS ---
questions_list = [
    "Qu’est ce qui t'intéresse le plus en ce moment ?",
    "Est-ce que tu peux nous parler d’une des expériences les plus intéressantes que tu aies vécu ?",
    "Est-ce que tu peux nous parler d’une personne que tu trouves très intéressante ?",
    "Est-ce que tu peux nous parler d’une œuvre que tu trouves particulièrement intéressante ?",
    "Un truc que tu crois avec certitude, sans en avoir de preuve ?",
    "Si tu pouvais avoir accès à une statistique précise sur ta propre vie, laquelle voudrais-tu connaître ?",
    "Si on pouvait te 'télécharger' une compétence ou un savoir instantanément (façon Matrix), que choisirais-tu ?",
    "S'il y avait un mystère dont tu pouvais connaître la solution instantanément, lequel serait-ce ?",
    "Si tu pouvais passer un message court que l'intégralité de l'humanité entendrait en même temps, que dirais-tu ?",
    "Est-ce que tu as appris quelque chose d’intéressant récemment ?",
    "Est-ce qu’il y a une chose intéressante te concernant que peu de gens savent ?",
    "Si on te donne des moyens illimités pour réaliser un projet, qu’est ce que ce serait ?",
    "Est-ce qu’il y a quelque chose dont tu es certain, mais sans en avoir de preuve ?",
    "Quelle est la dernière chose sur laquelle tu as changé d’avis ?",
    "Est-ce qu’il y a un endroit dans le monde qui t’a particulièrement marqué ?",
    "Si tu pouvais redécouvrir ou revivre quelque chose pour la première fois, qu’est ce que ce serait ?",
    "Est-ce qu’il t'est arrivé quelque chose qui reste à ce jour inexpliqué ?",
    "Est-ce qu’il y a une théorie ou un concept que tu trouves particulièrement intéressant ?",
    "Est-ce qu’il y a une histoire vraie que tu trouves particulièrement intéressante ?",
    "C’est quand la dernière fois que tu as fait un truc pour la première fois ?",
    "Quelle a été ta plus grande douleur physique dans ta vie ?",
    "Qu’est ce que tu attends le plus de l’amitié ?",
    "Quel est l’objet que tu possèdes auquel tu es le plus attaché ?",
    "Si tu pouvais faire du tourisme temporel, où et quand irais-tu ?",
    "Quelle est la coïncidence la plus incroyable qui te soit jamais arrivée ?",
    "Y a-t-il un talent ou une compétence que tu admires chez les autres, mais que tu te sens totalement incapable de pratiquer ?",
    "Si tu devais vivre dans une autre époque, mais avec ton niveau de confort actuel, laquelle choisirais-tu ?",
    "Si tu pouvais supprimer une peur ou une angoisse de ton esprit pour toujours, laquelle choisirais-tu ?",
    "Si tu pouvais envoyer un SMS de 140 caractères à toi-même il y a 10 ans, qu'écrirais-tu ?",
    "A quelle matière scolaire tu prêterais beaucoup plus d’attention maintenant que tu es adulte ?",
    "Quel petit événement où décision a eu un grand impact sur la suite de ta vie ?",
    "Si tu pouvais revivre un jour de ta vie autant de fois que tu le souhaites, lequel ce serait ?",
    "Quels sont pour toi les meilleurs plaisirs de la vie ?",
    "Est-ce que tu as une routine, ou une activité quotidienne qui te met dans un état de plénitude ?",
    "S'il y avait un version de toi dans un univers parallèle qui a fait un choix radicalement différent du tien à un moment important, à quoi ressemblerait sa vie aujourd'hui ?",
    "Quel aurait été ton métier au Moyen-Age ?",
    "Quel jeu d’enfant t’a particulièrement marqué ?",
    "Quel est ton plus grand “unpopular opinion” ?"
]

# --- SYSTÈME DE PERSISTENCE ---

# 1. Gestion du Seed (Code de partie)
if "seed" not in st.query_params:
    st.query_params["seed"] = random.randint(1000, 9999)
game_seed = int(st.query_params["seed"])

# 2. Gestion de l'Index (Position dans le paquet)
if "idx" not in st.query_params:
    st.query_params["idx"] = -1
current_idx = int(st.query_params["idx"])

# 3. Reconstruction du Deck (toujours le même pour un seed donné)
deck = list(questions_list)
random.seed(game_seed)
random.shuffle(deck)

# --- STRUCTURE ---
st.title("✨ Continue tu m'intéresses")

col_main, col_back = st.columns([4, 1])

with col_main:
    if st.button('🃏 PIOCHER UNE CARTE', type="primary"):
        if current_idx < len(deck) - 1:
            st.query_params["idx"] = current_idx + 1
            st.rerun()
        else:
            # Fin de paquet : on change de seed et on reset l'index
            st.query_params["seed"] = random.randint(1000, 9999)
            st.query_params["idx"] = 0
            st.rerun()

with col_back:
    # On peut revenir en arrière tant qu'on n'est pas au début
    if current_idx > 0:
        if st.button('🔙', type="secondary"):
            st.query_params["idx"] = current_idx - 1
            st.rerun()
    else:
        st.button(' ', type="secondary", disabled=True)

# AFFICHAGE DE LA QUESTION
if current_idx == -1:
    display_q = "Prêt pour une discussion intéressante ?"
else:
    display_q = deck[current_idx]

st.markdown(f"""
    <div class="card-container">
        <div class="question-text">{display_q}</div>
    </div>
    """, unsafe_allow_html=True)

# PROGRESSION
nb_totales = len(questions_list)
nb_tirees = current_idx + 1 if current_idx >= 0 else 0
progression = nb_tirees / nb_totales

st.progress(progression)
st.markdown(f'<p class="progress-text">Progression : {nb_tirees} / {nb_totales}</p>', unsafe_allow_html=True)

# BOUTON RESET (Nouveau !)
if st.button("🔄 Recommencer une nouvelle partie"):
    st.query_params.clear()
    st.rerun()

# FOOTER
st.write("---")
st.caption("Inspiré du podcast de Patrick Baud • Projet Personnel")
