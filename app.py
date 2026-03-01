import streamlit as st
import pandas as pd
import joblib

# Chargement
model = joblib.load('modele_churn_final.pkl')
model_columns = joblib.load('colonnes_model.pkl')

# Forcer un titre bien visible
st.write("# 📊 Prédiction de Churn")

# On enlève les colonnes complexes et on met tout à la suite pour plus de clarté
st.markdown("### 📝 Saisie des données client")

# Utilisation de labels clairs
tenure = st.slider("Ancienneté du client (en mois)", 0, 72, 12)
monthly_charges = st.number_input("Facture mensuelle ($)", value=50.0)
total_charges = st.number_input("Total payé à ce jour ($)", value=500.0)

# Sélection du contrat
contract = st.radio("Type de contrat actuel", ["Month-to-month", "One year", "Two year"])

if st.button("🔍 Calculer le risque de départ"):
    input_data = pd.DataFrame(0, index=[0], columns=model_columns)
    input_data['tenure'] = tenure
    input_data['MonthlyCharges'] = monthly_charges
    input_data['TotalCharges'] = total_charges
    
    col_contract = f"Contract_{contract}"
    if col_contract in input_data.columns:
        input_data[col_contract] = 1

    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error(f"ALERTE : Risque de départ de {proba:.1%}")
    else:
        st.success(f"STABLE : Probabilité de rester de {1-proba:.1%}")
