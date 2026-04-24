import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Continue tu m'intéresses", page_icon="✨", layout="centered")

# --- DESIGN PREMIUM ET MOBILE-FIRST (CSS) ---
st.markdown("""
    <style>
    /* Fond dégradé */
    .stApp {
        background: linear-gradient(180deg, #0e1117 0%, #1a1c23 100%);
    }
    
    /* FORCE LES COLONNES À RESTER CÔTE À CÔTE SUR MOBILE */
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

    /* CARTE */
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

    /* STYLE BOUTON PIOCHER (PRIMARY) */
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

    /* STYLE BOUTON RETOUR (SECONDARY) */
    .stButton button[kind="secondary"] {
        background-color: #2c3e50 !important;
        color: #bdc3c7 !important;
        border: 1px solid #34495e !important;
        border-radius: 15px !important;
        height: 3.8em !important;
        width: 100% !important;
    }

    /* HOVERS */
    .stButton button[kind="primary"]:hover {
        background-color: #e67e22 !important;
        border: none !important;
    }
    .stButton button[kind="secondary"]:hover {
        background-color: #34495e !important;
        border: 1px solid #f39c12 !important;
    }

    h1 { font-family: 'Georgia', serif; font-weight: 700; color: white; margin-bottom: 0px; text-align: center; }
    .instruction { color: #7f8c8d; font-style: italic; font-size: 0.9rem; margin-bottom: 20px; text-align: center; }
    .progress-text { color: #7f8c8d; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- TA LISTE DE QUESTIONS ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
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
    ]

# --- LOGIQUE DE LA PIOCHE ---
if 'deck' not in st.session_state or len(st.session_state.deck) == 0:
    st.session_state.deck = list(st.session_state.questions)
    random.shuffle(st.session_state.deck)

if 'current_q' not in st.session_state:
    st.session_state.current_q = "Prêt pour une discussion intéressante ?"

if 'previous_q' not in st.session_state:
    st.session_state.previous_q = None

# --- STRUCTURE ---
st.title("✨ Continue tu m'intéresses")
st.markdown('<p class="instruction">Laissez la curiosité guider la soirée...</p>', unsafe_allow_html=True)

# Colonnes avec ratio 4 pour le bouton principal et 1 pour le retour
col_main, col_back = st.columns([4, 1])

with col_main:
    # Utilisation du type "primary" pour garantir la couleur orange
    if st.button('🃏 PIOCHER UNE CARTE', type="primary"):
        if st.session_state.current_q != "Prêt pour une discussion intéressante ?":
            st.session_state.previous_q = st.session_state.current_q
        
        if len(st.session_state.deck) > 0:
            st.session_state.current_q = st.session_state.deck.pop()
            st.rerun()
        else:
            st.session_state.deck = list(st.session_state.questions)
            random.shuffle(st.session_state.deck)
            st.session_state.current_q = st.session_state.deck.pop()
            st.rerun()

with col_back:
    # On affiche le bouton retour seulement s'il y a un historique
    # Utilisation du type "secondary" pour le bouton discret
    if st.session_state.previous_q:
        if st.button('🔙', type="secondary"):
            temp = st.session_state.current_q
            st.session_state.current_q = st.session_state.previous_q
            st.session_state.previous_q = temp
            st.rerun()
    else:
        # Bouton fantôme pour garder l'alignement si pas d'historique
        st.button(' ', type="secondary", disabled=True)

# CARTE
st.markdown(f'''
    <div class="card-container">
        <div class="question-text">{st.session_state.current_q}</div>
    </div>
