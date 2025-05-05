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

# -------- Boucle de validation --------
# … votre code inchangé au-dessus …

for stage in range(1, 5):
    if st.session_state.stage == stage:
        user_input = st.number_input(
            f"Étape {stage} : Entrez la valeur de d{stage}",
            min_value=0, max_value=9, key=f"input_{stage}"
        )
        if st.button(f"Valider d{stage}", key=f"validate_{stage}"):
            if user_input == expected_codes[stage-1]:
                st.success(f"✅ Cadenas {stage} déverrouillé !")
                st.session_state.stage += 1
                # on retire st.experimental_rerun()
            else:
                st.error("❌ Code incorrect, réessayez.")
        break


# -------- Félicitations --------
if st.session_state.stage > 4:
    st.balloons()
    st.success("🎉 Tous les cadenas sont déverrouillés ! Bravo !")
    st.write("Vous pouvez maintenant passer à la conclusion du TP.")
