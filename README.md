# Company Bankruptcy Prediction

## Introduction

Dans le secteur financier, prédire la faillite est crucial pour prendre des décisions d'investissement éclairées et gérer les risques financiers. Une prévision précise des faillites peut aider les parties prenantes, telles que les investisseurs, les créanciers et les analystes financiers, à anticiper les difficultés financières et à prendre des décisions stratégiques pour atténuer les pertes potentielles.

## Objectif du Projet

L'objectif de ce projet est de développer un modèle prédictif pour prévoir la faillite des entreprises en utilisant des techniques d'apprentissage automatique. En exploitant des méthodes de modélisation avancées, le but est de construire un modèle robuste et précis qui peut efficacement prédire la probabilité de faillite et fournir des informations précieuses aux décideurs.

[Lien vers le Notebook](https://github.com/Zaccaria-Amillou/Brankruptcy-Model/blob/main/notebook/notebook.ipynb)
## Aperçu des Données

Le jeu de données utilisé dans ce projet provient de Kaggle et est intitulé [Company Bankruptcy Prediction](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction). Ce jeu de données contient des informations sur les faillites provenant du Taiwan Economic Journal pour les années 1999-2009. Il inclut une gamme de métriques financières, telles que les ratios de rentabilité, les ratios de liquidité et d'autres indicateurs financiers pertinents utilisés pour évaluer la santé financière d'une entreprise et prédire la probabilité de faillite.

![Data Overview](https://images.unsplash.com/photo-1515975325863-a4ceb4b7d6c0?q=80&w=1925&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## Méthodologie

### 1. Préparation des Données
- Prétraitement pour gérer les valeurs manquantes
- Normalisation des caractéristiques
- Traitement du déséquilibre des classes
![Correaltion](https://github.com/Zaccaria-Amillou/Brankruptcy-Model/blob/main/img/correaltion.png)

### 2. Sélection des Modèles
- **Ridge Classifier**
- **Régression Logistique**
- **Support Vector Classifier (SVC)**

### 3. Classificateur par Vote
- Combinaison des prédictions de plusieurs modèles de base
- Amélioration de la précision globale et de la robustesse des prédictions

### 4. Évaluation
- Validation croisée
- Métriques : précision, précision, rappel et F1-score


## Signification

Une prédiction précise des faillites est inestimable pour les institutions financières et les investisseurs. En prédisant les faillites avec une grande précision, les parties prenantes peuvent prendre de meilleures décisions financières, réduire les risques potentiels et améliorer la stabilité financière. Ce projet vise à fournir un outil fiable pour la prévision des faillites, contribuant à une meilleure gestion des risques et à une analyse financière améliorée.

## Structure du Rapport

Ce rapport fournit un aperçu détaillé du projet, y compris la préparation des données, le développement des modèles et l'évaluation. Chaque section offre des informations sur les méthodologies utilisées et les résultats obtenus, offrant une compréhension approfondie des objectifs et des résultats du projet.

## Conclusion

Dans ce projet, nous avons visé à développer et évaluer un modèle de classification robuste pour prédire les faillites en utilisant diverses techniques d'apprentissage automatique. Nous avons employé un classificateur par vote qui combine plusieurs modèles de base pour tirer parti de leurs forces collectives et améliorer les performances prédictives.

### Résumé de la Méthodologie

1. **Préparation des Données**
   - Prétraitement du jeu de données.

2. **Sélection du Modèle**
   - Classificateur par vote avec :
     - **Ridge Classifier avec Calibration**
     - **Régression Logistique**
     - **Support Vector Classifier (SVC)**

3. **Entraînement et Évaluation du Modèle**
   - Entraînement avec validation croisée
   - Évaluation avec des métriques de performance

### Résultats

Le classificateur par vote a atteint une précision impressionnante d'environ 87%. Ce résultat indique que notre modèle est très efficace pour distinguer les entités en faillite de celles qui ne le sont pas.

- **Rapport de Classification** : Fournit des métriques détaillées telles que la précision, le rappel et le score F1 pour chaque classe.
- **Matrice de Confusion** : Visualise les prédictions vraies positives, vraies négatives, fausses positives et fausses négatives.
- **Précision** : Calculée à 88%.

![Confusion Matrix](https://github.com/Zaccaria-Amillou/Brankruptcy-Model/blob/main/img/output.png)

### Implications

La haute précision de ~88% suggère que notre modèle de classificateur par vote est bien adapté pour prédire les faillites, ce qui peut être précieux pour les institutions financières, les investisseurs et les analystes. Ce niveau de précision signifie que le modèle peut aider de manière significative à identifier les entités à risque, réduisant potentiellement les pertes financières et améliorant les processus de prise de décision.
