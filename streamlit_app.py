import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Continue tu m'intéresses", page_icon="✨", layout="centered")

# --- DESIGN PREMIUM (CSS) ---
st.markdown("""
    <style>
    /* Fond dégradé sombre */
    .stApp {
        background: linear-gradient(180deg, #0e1117 0%, #1a1c23 100%);
    }
    
    /* Carte style Papier Premium */
    .card-container {
        background-color: #fdfdfd;
        padding: 40px 25px;
        border-radius: 24px;
        border-bottom: 6px solid #e67e22; 
        text-align: center;
        min-height: 280px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 20px 40px rgba(0,0,0,0.4);
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .question-text {
        color: #2c3e50;
        font-size: 22px;
        font-weight: 600;
        font-family: 'Helvetica Neue', sans-serif;
        line-height: 1.4;
    }
    
    /* Style du bouton Principal (Piocher) */
    div.stButton > button:first-child {
        background-color: #f39c12;
        color: white;
        border-radius: 15px;
        border: none;
        height: 3.8em;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(243, 156, 18, 0.3);
    }

    /* Style du bouton Secondaire (Retour) - Plus discret */
    div.stButton > button:active, div.stButton > button:focus, .st-emotion-cache-19rxjzo {
        background-color: #2c3e50;
    }
    
    /* Forcer le bouton précédent à être gris/discret */
    section[data-testid="stSidebar"] + div .stButton button[kind="secondary"] {
        background-color: #2c3e50;
        color: #bdc3c7;
        border: 1px solid #34495e;
        border-radius: 15px;
    }

    h1 {
        font-family: 'Georgia', serif;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0px;
    }
    
    .instruction {
        color: #7f8c8d;
        font-style: italic;
        font-size: 0.9rem;
        margin-bottom: 30px;
    }

    .progress-text {
        color: #7f8c8d;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 10px;
    }
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
        "S'il y avait une version de toi dans un univers parallèle qui a fait un choix radicalement différent du tien à un moment important, à quoi ressemblerait sa vie aujourd'hui ?",
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

# --- STRUCTURE DE L'ÉCRAN ---
st.title("✨ Continue tu m'intéresses")
st.markdown('<p class="instruction">Laissez la curiosité guider la soirée...</p>', unsafe_allow_html=True)

# Colonnes asymétriques : 3/4 pour piocher, 1/4 pour retour
col_main, col_back = st.columns([3, 1])

with col_main:
    if st.button('🃏 PIOCHER UNE CARTE'):
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
    if st.session_state.previous_q:
        # On utilise une flèche pour gagner de la place
        if st.button('🔙'):
            temp = st.session_state.current_q
            st.session_state.current_q = st.session_state.previous_q
            st.session_state.previous_q = temp
            st.rerun()

# LA CARTE
st.markdown(f'''
    <div class="card-container">
        <div class="question-text">{st.session_state.current_q}</div>
    </div>
    ''', unsafe_allow_html=True)

# LA PROGRESSION (JUSTE EN DESSOUS)
nb_totales = len(st.session_state.questions)
nb_tirees = nb_totales - len(st.session_state.deck)
progression = nb_tirees / nb_totales

st.progress(progression)
st.markdown(f'<p class="progress-text">Progression : {nb_tirees} / {nb_totales}</p>', unsafe_allow_html=True)

# FOOTER
st.write("---")
st.caption("Inspiré du podcast de Patrick Baud • Projet Personnel")
