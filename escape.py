import streamlit as st

# -------- Configuration --------
st.sidebar.header("Configuration")
expected_codes = [
    st.sidebar.number_input("Code attendu d1", min_value=0, max_value=9, value=5, step=1),
    st.sidebar.number_input("Code attendu d2", min_value=0, max_value=9, value=7, step=1),
    st.sidebar.number_input("Code attendu d3", min_value=0, max_value=9, value=2, step=1),
    st.sidebar.number_input("Code attendu d4", min_value=0, max_value=9, value=5, step=1)
]

# -------- Initialisation du state --------
if "stage" not in st.session_state:
    st.session_state.stage = 1

st.title("Simulateur de cadenas - TP Maths 4e")
st.write("Suivez les étapes pour déverrouiller chaque cadenas en entrant les valeurs d1, d2, d3 et d4.")

# -------- Affichage des étapes --------
for i in range(1, 5):
    # Désactiver les étapes déjà validées ou futures
    disabled = (st.session_state.stage != i)
    user_input = st.number_input(
        f"Étape {i} : Entrez la valeur de d{i}",
        min_value=0, max_value=9,
        key=f"input_{i}",
        disabled=disabled
    )
    if st.button(f"Valider d{i}", key=f"validate_{i}", disabled=disabled):
        if user_input == expected_codes[i-1]:
            st.success(f"✅ Cadenas {i} déverrouillé !")
            st.session_state.stage = i + 1
        else:
            st.error("❌ Code incorrect, réessayez.")

# -------- Félicitations --------
if st.session_state.stage > 4:
    st.balloons()
    st.success("🎉 Tous les cadenas sont déverrouillés ! Bravo !")
    st.write("Vous pouvez maintenant passer à la conclusion du TP.")
