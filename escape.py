import streamlit as st
import math

# -------- Configuration --------
st.sidebar.header("Configuration")
# Codes attendus pour d1 à d4
expected_codes = [
    st.sidebar.number_input("Code attendu d1", min_value=0, max_value=9, value=5, step=1),
    st.sidebar.number_input("Code attendu d2", min_value=0, max_value=9, value=7, step=1),
    st.sidebar.number_input("Code attendu d3", min_value=0, max_value=9, value=2, step=1),
    st.sidebar.number_input("Code attendu d4", min_value=0, max_value=9, value=5, step=1),
]
# Calcul du code attendu d5 : partie entière de la moyenne de d1 à d4
d5_expected = math.floor(sum(expected_codes) / len(expected_codes))

# -------- Initialisation du state --------nif "stage" not in st.session_state:
    st.session_state.stage = 1

st.title("Simulateur de cadenas - TP Maths 4e")
st.write("Entrez successivement d1, d2, d3, d4 puis d5 (partie entière de la moyenne) pour déverrouiller chaque cadenas.")

# -------- Étapes 1 à 4 --------for i in range(1, 5):
    disabled = (st.session_state.stage != i)
    user_val = st.number_input(
        f"Étape {i} : Entrez la valeur de d{i}",
        min_value=0, max_value=9,
        key=f"input_{i}",
        disabled=disabled
    )
    if st.button(f"Valider d{i}", key=f"validate_{i}", disabled=disabled):
        if user_val == expected_codes[i-1]:
            st.success(f"✅ Cadenas {i} déverrouillé !")
            st.session_state.stage = i + 1
        else:
            st.error("❌ Code incorrect, réessayez.")

# -------- Étape 5 --------if st.session_state.stage == 5:
    st.write("---")
    st.write("### Étape 5 : partie entière de la moyenne de d1 à d4")
    d5_val = st.number_input(
        "Entrez la valeur de d5 (partie entière de la moyenne)",
        min_value=0, max_value=9,
        key="input_5"
    )
    if st.button("Valider d5", key="validate_5"):
        if d5_val == d5_expected:
            st.success("✅ Cadenas 5 déverrouillé !")
            st.session_state.stage = 6
        else:
            st.error(f"❌ Code incorrect, la partie entière attendue est {d5_expected}.")

# -------- Félicitations --------if st.session_state.stage > 5:
    st.balloons()
    st.success("🎉 Tous les cadenas sont déverrouillés ! Bravo !")
    st.write("Vous avez complété toutes les étapes du TP.")
