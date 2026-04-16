# 🚀 Prédiction du Churn Client (Télécom)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Ce projet utilise le Machine Learning pour identifier de manière proactive les clients risquant de quitter un opérateur télécom. Il inclut une interface utilisateur moderne et intuitive construite avec Streamlit, intégrant des éléments de design **Glassmorphism**.

## 🎯 Objectif Business
Réduire le taux d'attrition (churn) en identifiant les profils instables afin de proposer des campagnes de rétention ciblées et d'améliorer la fidélité client.

## 🌟 Fonctionnalités & Interface
- **Interface Moderne** : Design premium avec des effets Glassmorphism (transparence, flou) et des dégradés de couleurs fluides.
- **Analyse en Temps Réel** : Modifiez l'ancienneté, le type de contrat et les factures pour observer instantanément la probabilité de churn.
- **Retour Visuel** : Indicateurs visuels clairs (Alerte rouge pour un risque élevé, validation bleue pour un client stable) et recommandations associées.

## 🛠️ Stack Technique
- **Modèle Prédictif :** Random Forest Classifier (entraîné avec Scikit-Learn)
- **Développement Frontend :** Streamlit avec CSS personnalisé
- **Manipulation des Données :** Pandas

## 📈 Résultats du Modèle
- **Précision globale :** ~81%
- **Facteur n°1 de churn :** Le type de contrat (Contrats courts/mois par mois).
- **Facteur n°2 :** Le montant des charges mensuelles.

## 💻 Installation et Utilisation

**1. Cloner le projet :**
```bash
git clone https://github.com/zakariakassemi2000/Pr-diction-de-Churn-Client-Telecom.git
cd Pr-diction-de-Churn-Client-Telecom
```

**2. Installer les dépendances :**
```bash
pip install -r requirements.txt
```