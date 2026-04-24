import streamlit as st
import random

# Configuration de la page (titre de l'onglet et icône)
st.set_page_config(page_title="Continue tu m'intéresses", page_icon="✨")

# --- DESIGN PERSONNALISÉ (CSS) ---
st.markdown("""
    <style>
    /* Fond de l'application */
    .main {
        background-color: #0e1117;
    }
    
    /* Style de la carte */
    .card-container {
        background-color: #ffffff;
        padding: 50px 30px;
        border-radius: 20px;
        border-left: 12px solid #f39c12; /* Bordure orange rappelant la curiosité */
        text-align: center;
        min-height: 300px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.4);
        margin: 20px 0;
    }
    
    /* Style du texte de la question */
    .question-text {
        color: #1a1a1a;
        font-size: 24px;
        font-weight: 500;
        font-family: 'Georgia', serif;
        line-height: 1.5;
    }
    
    /* Style du bouton */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #f39c12;
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #e67e22;
        transform: translateY(-2px);
    }
    
    /* Titre principal */
    h1 {
        color: #ffffff !important;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    
    /* Texte d'instruction */
    .instruction {
        color: #bdc3c7;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Style pour le texte de progression */
    .progress-text {
        color: #bdc3c7;
        text-align: center;
        font-size: 0.9rem;
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
    st.session_state.current_q = "Clique sur le bouton pour piocher une carte."

if 'previous_q' not in st.session_state:
    st.session_state.previous_q = None

# --- AFFICHAGE ---
st.title("✨ Continue tu m'intéresses")
st.markdown('<p class="instruction">Piochez une carte et laissez la curiosité guider la conversation.</p>', unsafe_allow_html=True)

# Boutons en colonnes
col1, col2 = st.columns(2)

with col1:
    if st.button('🃏 PIOCHER'):
        # Sauvegarde pour le bouton retour
        if st.session_state.current_q != "Clique sur le bouton pour piocher une carte.":
            st.session_state.previous_q = st.session_state.current_q
        
        # Tirage d'une carte
        if len(st.session_state.deck) > 0:
            st.session_state.current_q = st.session_state.deck.pop()
            st.rerun()
        else:
            # Remélange automatique si vide
            st.session_state.deck = list(st.session_state.questions)
            random.shuffle(st.session_state.deck)
            st.session_state.current_q = st.session_state.deck.pop()
            st.rerun()

with col2:
    if st.session_state.previous_q:
        if st.button('⬅️ PRÉCÉDENTE'):
            # Échange pour revenir en arrière
            temp = st.session_state.current_q
            st.session_state.current_q = st.session_state.previous_q
            st.session_state.previous_q = temp
            st.rerun()

# Affichage de la carte
st.markdown(f'''
    <div class="card-container">
        <div class="question-text">{st.session_state.current_q}</div>
    </div>
    ''', unsafe_allow_html=True)

# --- BARRE DE PROGRESSION (JUSTE EN DESSOUS) ---
nb_totales = len(st.session_state.questions)
nb_restantes = len(st.session_state.deck)
nb_tirees = nb_totales - nb_restantes
progression = nb_tirees / nb_totales if nb_totales > 0 else 0

st.progress(progression)
st.markdown(f'<p class="progress-text">Progression : {nb_tirees} / {nb_totales}</p>', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("Projet personnel - Inspiré du podcast du même nom créé par Patrick Baud")
