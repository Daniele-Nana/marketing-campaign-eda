import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("EDA - Segmentation clients marketing")

@st.cache_data
def load_data():
    df = pd.read_csv('marketing_campaign.csv', sep=';')
    # Nettoyage minimal
    df['Income'].fillna(df['Income'].median(), inplace=True)
    # Ajout dépense totale
    spending_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 
                     'MntSweetProducts', 'MntGoldProds']
    df['Total_Spending'] = df[spending_cols].sum(axis=1)
    return df

df = load_data()

# Section 1 : Aperçu
st.subheader("Aperçu des données")
st.write(df.head())

# Section 2 : Distribution de la cible
st.subheader("Répartition des réponses")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots()
    sns.countplot(x='Response', data=df, ax=ax)
    st.pyplot(fig)
with col2:
    st.write(f"Taux de réponse : {df['Response'].mean()*100:.2f}%")

# Section 3 : Dépenses totales
st.subheader("Dépenses totales selon la réponse")
fig, ax = plt.subplots()
sns.boxplot(x='Response', y='Total_Spending', data=df, ax=ax)
ax.set_yscale('log')
st.pyplot(fig)

# Section 4 : Corrélations
st.subheader("Matrice de corrélation (variables clés)")
num_cols = ['Income', 'Recency', 'Total_Spending', 'NumWebVisitsMonth',
            'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'Response']
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Section 5 : Segmentation interactive
st.subheader("Segmentation : Revenu vs Dépenses")
income_bins = st.slider("Nombre de tranches de revenu", 2, 10, 4)
spend_bins = st.slider("Nombre de tranches de dépenses", 2, 10, 4)

df['Income_Group'] = pd.qcut(df['Income'], q=income_bins, labels=False, duplicates='drop')
df['Spending_Group'] = pd.qcut(df['Total_Spending'], q=spend_bins, labels=False, duplicates='drop')
segment_response = df.groupby(['Income_Group', 'Spending_Group'])['Response'].mean().unstack()

fig, ax = plt.subplots()
sns.heatmap(segment_response, annot=True, cmap='viridis', ax=ax)
st.pyplot(fig)