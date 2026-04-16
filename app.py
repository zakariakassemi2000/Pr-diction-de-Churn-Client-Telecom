import streamlit as st
import pandas as pd
import joblib

# Configuration de la page
st.set_page_config(
    page_title="Prédiction de Churn", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for glassmorphism and modern UI
st.markdown("""
<style>
    /* Global Background Override */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* Title font and style */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #00C6FF, #0072FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Custom Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
        margin-top: 1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 43, 0.6);
        color: white;
    }
    
    /* Container Styling - For Glassmorphism Effect */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Mise en cache du modèle pour de meilleures performances
@st.cache_resource
def load_model():
    return joblib.load('Best_Model.pkl'), joblib.load('colonnes_model.pkl')

model, model_columns = load_model()

# Header
st.markdown("<h1>📊 Prédiction de Churn Client</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-top: -1rem; margin-bottom: 3rem; font-size: 1.1rem;'>Identifiez de manière proactive les clients risquant de résilier leur abonnement grâce à l'IA.</p>", unsafe_allow_html=True)

# Layout Container
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.container():
        st.markdown("<h3 style='color: #e2e8f0; margin-bottom: 1.5rem;'>📝 Profil du Client</h3>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        
        with c1:
            tenure = st.slider("⏳ Ancienneté (mois)", 0, 72, 12)
            contract = st.radio("📑 Type de contrat", ["Month-to-month", "One year", "Two year"])
            
        with c2:
            monthly_charges = st.number_input("💸 Facture mensuelle ($)", value=50.0, step=5.0)
            total_charges = st.number_input("💰 Total payé à ce jour ($)", value=500.0, step=50.0)
        
        if st.button("🔍 Lancer l'Analyse Prédictive"):
            with st.spinner("Analyse approfondie en cours..."):
                input_data = pd.DataFrame(0, index=[0], columns=model_columns)
                input_data['tenure'] = tenure
                input_data['MonthlyCharges'] = monthly_charges
                input_data['TotalCharges'] = total_charges
                
                col_contract = f"Contract_{contract}"
                if col_contract in input_data.columns:
                    input_data[col_contract] = 1

                prediction = model.predict(input_data)
                proba = model.predict_proba(input_data)[0][1]

            st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
            if prediction[0] == 1:
                st.markdown(f"""
                <div style="padding: 1.5rem; border-radius: 12px; background: rgba(255, 75, 43, 0.15); border-left: 6px solid #FF4B2B; box-shadow: 0 4px 15px rgba(255, 75, 43, 0.1);">
                    <h3 style="color: #FF4B2B; margin-top: 0; font-size: 1.4rem;">⚠️ Risque de Départ Élevé</h3>
                    <p style="font-size: 1.2rem; color: #f8fafc; margin-bottom: 0;">Probabilité de churn : <strong>{proba:.1%}</strong></p>
                    <p style="font-size: 0.9rem; color: #cbd5e1; margin-top: 10px; margin-bottom: 0;">Action recommandée : Proposer immédiatement des offres de fidélisation adaptées.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="padding: 1.5rem; border-radius: 12px; background: rgba(0, 198, 255, 0.15); border-left: 6px solid #00C6FF; box-shadow: 0 4px 15px rgba(0, 198, 255, 0.1);">
                    <h3 style="color: #00C6FF; margin-top: 0; font-size: 1.4rem;">✅ Client Stable</h3>
                    <p style="font-size: 1.2rem; color: #f8fafc; margin-bottom: 0;">Probabilité de rester : <strong>{1-proba:.1%}</strong></p>
                    <p style="font-size: 0.9rem; color: #cbd5e1; margin-top: 10px; margin-bottom: 0;">Action recommandée : Consolider la relation normale, aucune intervention urgente.</p>
                </div>
                """, unsafe_allow_html=True)
