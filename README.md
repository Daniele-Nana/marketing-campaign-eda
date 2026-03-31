# Prédiction de réponse à une campagne marketing – Analyse exploratoire (EDA)

## Contexte

Une entreprise souhaite améliorer l'efficacité de ses campagnes marketing en ciblant les clients les plus susceptibles de répondre à une offre.  
Ce projet réalise une **analyse exploratoire (EDA)** sur un jeu de données de 2 240 clients, contenant des informations démographiques, l'historique d'achat et les réponses aux campagnes précédentes. L'objectif est de comprendre le profil des répondants et d'identifier les facteurs clés d'acceptation.

Un tableau de bord interactif **Streamlit** permet d'explorer visuellement les données et les résultats.

## Jeu de données

- **Source** : [Marketing Campaign Dataset (Kaggle)](https://www.kaggle.com/datasets/rodsaldanha/marketing-campaign)
- **Contenu** : 2 240 clients, 29 variables.
- **Variables principales** :
  - `Response` (cible) : 1 si le client a accepté la dernière campagne, 0 sinon.
  - Démographie : `Year_Birth`, `Education`, `Marital_Status`, `Income`, `Kidhome`, `Teenhome`.
  - Dépenses : `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds`.
  - Comportement d'achat : `NumWebPurchases`, `NumCatalogPurchases`, `NumStorePurchases`, `NumDealsPurchases`, `NumWebVisitsMonth`.
  - Historique des campagnes : `AcceptedCmp1` … `AcceptedCmp5`.
  - Autres : `Recency` (jours depuis le dernier achat), `Dt_Customer` (date d'inscription).

## Technologies utilisées

- **Python** – langage principal
- **Pandas, NumPy** – manipulation et analyse
- **Matplotlib, Seaborn** – visualisations statiques
- **Scikit-learn** – prétraitement, PCA
- **Streamlit** – tableau de bord interactif

## Installation et exécution

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/marketing-campaign-eda.git
cd marketing-campaign-eda
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
# Activation (Windows - cmd)
venv\Scripts\activate
# Activation (Linux/macOS)
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Télécharger le jeu de données

Téléchargez le fichier CSV depuis [Kaggle](https://www.kaggle.com/datasets/rodsaldanha/marketing-campaign) et placez‑le à la racine du projet sous le nom `marketing_campaign.csv`.

### 5. Lancer l'application Streamlit
```bash
streamlit run dashboard_marketing.py
```

L'application s'ouvre automatiquement dans votre navigateur.

## Principaux résultats de l'analyse

- **Taux de réponse** : environ 15 % (déséquilibre modéré).
- **Profil des répondants** :
  - Revenu supérieur (60 k€ contre 51 k€).
  - Dépenses totales presque doublées (987 € contre 539 €).
  - Achats plus récents (35 jours contre 51 jours).
  - Plus d'achats sur le web et par catalogue.
- **Variables les plus discriminantes** :
  - Dépenses totales, particulièrement en vin, viande et produits en or.
  - `Recency` (délai depuis le dernier achat).
  - Nombre de campagnes précédentes acceptées (`num_accepted_cmp`).
  - Achats web et catalogue.
- **Segmentation revenu × dépenses** :
  - Meilleurs taux de réponse : 36 % pour le segment « revenu moyen – dépenses très élevées », 32 % pour « revenu très élevé – dépenses très élevées ».
  - Segment « faible revenu – faibles dépenses » : seulement 6,8 %.

## Structure du dépôt
```text
marketing-campaign-eda/
├── dashboard_marketing.py        # Application Streamlit
├── requirements.txt              # Dépendances Python
├── .gitignore                    # Fichiers à ignorer (venv, csv, etc.)
├── README.md                     # Ce fichier
└── marketing_campaign.csv        # Jeu de données (non inclus dans le dépôt)
```

## Utilisation du tableau de bord

L'application Streamlit permet d'explorer interactivement :

- Distribution de la cible `Response`.
- Boxplots des dépenses par catégorie.
- Matrice de corrélation.
- Segmentation (revenu × dépenses).
- Historique des campagnes précédentes.

Des filtres sont disponibles pour affiner l'analyse par segments.

## Pistes pour la modélisation

L'analyse exploratoire pose les bases pour la construction d'un modèle prédictif. Les étapes suivantes pourraient être :

- Encoder les variables catégorielles (`Education`, `Marital_Status`).
- Normaliser les variables numériques (sauf les indicateurs binaires).
- Créer de nouvelles variables : `total_spending`, `num_accepted_cmp`, `omnichannel_score`.
- Gérer le déséquilibre éventuel (SMOTE, `class_weight`).
- Tester des modèles : régression logistique, Random Forest, XGBoost.
- Évaluer avec la précision, le rappel, le F1‑score et l'AUC‑ROC.