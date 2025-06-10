# projet_analyse_ventes

# Rapport d’Analyse Globale des Ventes

## Introduction
Ce projet propose une analyse exploratoire des données de ventes à partir de trois sources principales : clients, transactions et produits. L’objectif est de mieux comprendre les comportements d’achat, d’identifier des corrélations entre variables et de proposer des axes d’amélioration pour le business.

## Méthodologie
L’analyse a été réalisée en Python à l’aide des bibliothèques pandas, seaborn, matplotlib et scipy. Les fichiers utilisés sont :
- `customers.csv`
- `transactions.csv`
- `products.csv`

Les données ont été jointes et enrichies pour permettre des analyses croisées.

## Analyses et Résultats
- Corrélation significative entre le sexe des clients et les catégories de produits achetés (test du Chi2)
- Corrélation négative forte entre l’âge des clients et le montant total des achats
- Corrélation entre l’âge des clients et la fréquence d’achat selon les groupes d’âge
- Variations de la taille du panier moyen selon les tranches d’âge
- Préférences de catégories de produits selon les classes d’âge

## Visualisations
Des graphiques ont été générés pour illustrer :
- La répartition des catégories de produits selon le sexe et l’âge
- Les corrélations entre variables numériques
- L’évolution des ventes selon l’âge

Exemples de graphiques :
- Heatmaps
- Scatterplots
- Barplots

Les images sont disponibles dans le dossier `p4_graphic/`.

## Conclusions
L’analyse met en évidence des liens forts entre certaines variables démographiques et les comportements d’achat, l’importance de segmenter la clientèle, et propose des pistes pour approfondir l’analyse.

## Recommandations
- Approfondir l’analyse sur l’acquisition client et les canaux de vente
- Adapter les campagnes marketing selon les segments identifiés
- Continuer à enrichir la base de données pour affiner les analyses

## Reproduire l’analyse
1. Cloner ce dépôt
2. Installer les dépendances Python nécessaires (pandas, seaborn, matplotlib, scipy)
3. Lancer les notebooks Jupyter (`p4_notebook01.ipynb`, etc.) pour explorer les analyses
4. Générer le rapport HTML et les graphiques à l’aide des scripts fournis

## Structure du projet
- `p4_data/` : données sources (clients, transactions, produits)
- `p4_graphic/` : graphiques générés
- `rapport_analyse_ventes.html` : rapport final
- `rapport_analyse_ventes.css` : style du rapport
- `generate_rapport_pdf.py` : script pour générer un PDF du rapport
- `p4_notebook01.ipynb`, etc. : notebooks d’analyse

## Auteur
Projet réalisé par [Votre Nom].