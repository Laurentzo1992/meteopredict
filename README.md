# 🌧 PrecipFormer – Burkina Faso

**Système de prévision des précipitations par intelligence artificielle pour le Burkina Faso**

## 📋 Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Demo](#-demo)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Architecture](#-architecture)
- [Structure du projet](#-structure-du-projet)
- [Technologies](#-technologies)
- [Personnalisation](#-personnalisation)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌍 À propos

**PrecipFormer** est une application web interactive développée avec Streamlit qui utilise l'intelligence artificielle pour prévoir les précipitations au Burkina Faso. Conçue pour l'agriculture et la gestion des ressources en eau, elle offre une interface moderne et intuitive pour visualiser et analyser les données pluviométriques.

### 🎯 Objectifs

- 📊 Fournir des prévisions précises de précipitations
- 🗺️ Visualiser la distribution géographique des pluies
- 📈 Analyser les tendances temporelles et statistiques
- 🌾 Aider les agriculteurs dans la planification des cultures
- 💧 Optimiser la gestion des ressources en eau

---

## ✨ Fonctionnalités

### 🎨 Interface utilisateur

- **Design Dark Mode Premium** - Interface élégante avec effets glassmorphism et néon
- **Responsive** - Adaptation automatique à tous les écrans
- **Animations fluides** - Transitions CSS modernes pour une meilleure expérience

### 📊 Visualisations

- **Série temporelle interactive** - Évolution des précipitations sur 45 jours
- **Carte géographique** - Visualisation spatiale avec marqueurs colorés selon l'intensité
- **Graphiques statistiques** - Histogrammes, box plots, et tableaux récapitulatifs

### 🔧 Fonctionnalités avancées

- **Navigation temporelle** - Slider pour explorer l'historique des prévisions
- **Métriques en temps réel** - Moyenne, maximum, minimum, variance
- **Analyse automatique** - Insights générés automatiquement
- **Export de données** - Tableaux statistiques détaillés

---

## 🎥 Demo

### Interface principale
```
┌─────────────────────────────────────────────────┐
│   🌧 PrecipFormer – Burkina Faso 🇧🇫           │
│   Système de prévision par IA                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  📊 Moyenne    🔥 Maximum    ❄️ Minimum   ⏰    │
│   12.45 mm      28.90 mm      3.21 mm    24/44  │
│                                                 │
├─────────────────────────────────────────────────┤
│  📊 Analyse | 🗺 Carte | 📈 Statistiques       │
└─────────────────────────────────────────────────┘
```

### Captures d'écran

*Ajoutez vos captures d'écran ici*

---

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

### Installation rapide

```bash
# Cloner le repository
git clone https://github.com/votre-username/precipformer.git
cd precipformer

# Créer un environnement virtuel (recommandé)
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur macOS/Linux:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Fichier requirements.txt

```txt
streamlit>=1.28.0
plotly>=5.17.0
folium>=0.14.0
streamlit-folium>=0.15.0
pandas>=2.0.0
numpy>=1.24.0
xarray>=2023.0.0
```

---

## 💻 Utilisation

### Lancement de l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

### Configuration

Créez un fichier `config.yaml` pour personnaliser les paramètres :

```yaml
# Configuration PrecipFormer
app:
  title: "PrecipFormer – Burkina Faso"
  version: "2.0.0"
  
data:
  days: 45
  lat_range: [9.4, 15.1]
  lon_range: [-5.5, 2.4]
  
theme:
  primary_color: "#FF6B6B"
  secondary_color: "#FFD93D"
  accent_color: "#6BCF7F"
```

### Utilisation de base

1. **Sélectionner la date** - Utilisez le slider dans la sidebar
2. **Explorer les onglets** :
   - 📊 **Analyse temporelle** - Visualisez l'évolution dans le temps
   - 🗺️ **Carte interactive** - Explorez la distribution géographique
   - 📈 **Statistiques** - Consultez les analyses détaillées
3. **Interagir avec les graphiques** - Survolez, zoomez, téléchargez

---

## 🏗 Architecture

### Structure modulaire

Le code est organisé en modules réutilisables pour une meilleure maintenabilité :

```python
├── Theme           # Gestion des couleurs et du CSS
├── Components      # Composants UI réutilisables
├── Charts          # Générateurs de graphiques Plotly
├── MapBuilder      # Construction de cartes Folium
├── Sidebar         # Configuration de la barre latérale
└── main()          # Fonction principale d'orchestration
```

### Diagramme de flux

```
┌─────────────┐
│   main()    │
└──────┬──────┘
       │
       ├─── Theme.get_css()
       │
       ├─── Components.header()
       │
       ├─── Sidebar.render()
       │
       ├─── load_data()
       │
       ├─── Components.metric_card() × 4
       │
       └─── Tabs
            ├─── Charts.time_series()
            ├─── MapBuilder.create_dark_map()
            └─── Charts.histogram() + Charts.boxplot()
```

### Flux de données

```
generate_fake_burkina_data()
          ↓
      xarray Dataset
          ↓
   simulate_precip_fake()
          ↓
    numpy.ndarray (45 × lat × lon)
          ↓
    Visualisations (Plotly, Folium)
```

---

## 📁 Structure du projet

```
precipformer/
│
├── app.py                      # Application principale
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation
├── LICENSE                     # Licence MIT
│
├── services/
│   ├── __init__.py
│   ├── fake_data.py           # Génération de données simulées
│   └── predictor.py           # Modèle de prévision
│
├── assets/
│   ├── logo.png               # Logo de l'application
│   └── screenshots/           # Captures d'écran
│
├── config/
│   └── config.yaml            # Configuration de l'app
│
├── tests/
│   ├── test_data.py           # Tests des données
│   ├── test_charts.py         # Tests des graphiques
│   └── test_components.py     # Tests des composants
│
└── docs/
    ├── user_guide.md          # Guide utilisateur
    ├── developer_guide.md     # Guide développeur
    └── api_reference.md       # Référence API
```

---

## 🛠 Technologies

### Frontend
- **Streamlit** - Framework web pour applications data science
- **Plotly** - Bibliothèque de graphiques interactifs
- **Folium** - Cartes géographiques interactives
- **CSS3** - Styles personnalisés avec glassmorphism

### Backend
- **Python 3.8+** - Langage principal
- **NumPy** - Calculs numériques
- **Pandas** - Manipulation de données
- **xarray** - Données géospatiales

### Design
- **Poppins Font** - Typographie moderne
- **Dark Theme** - Interface sombre optimisée
- **Gradient Effects** - Effets visuels modernes

## 🤝 Contributing

Les contributions sont les bienvenues ! Voici comment participer :


### Guidelines

- Suivez le style de code PEP 8
- Ajoutez des tests pour les nouvelles fonctionnalités
- Mettez à jour la documentation
- Décrivez clairement vos changements dans la PR



