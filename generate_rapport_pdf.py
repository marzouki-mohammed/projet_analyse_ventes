from fpdf import FPDF
import os

# Chemins des images à inclure (ajustez selon vos besoins)
image_paths = [
    "p4_graphic/heatmap_global.png",
    "p4_graphic/heatmap_sexe_categories.png",
    "p4_graphic/scatterplot_montant_achat_age_client.png",
    "p4_graphic/scatterplot_frequence_achat_age_client.png",
    "p4_graphic/scatterplot_panier_moyen_age_client.png",
    "p4_graphic/scatterplot_panier_moyen_age_client_clusters.png",
    "p4_graphic/barplot_categorie_produit_age_client.png"
]

rapport = FPDF()
rapport.add_page()
rapport.set_font("Arial", 'B', 16)
rapport.cell(0, 10, "Rapport d’Analyse Globale des Ventes", ln=True, align='C')
rapport.ln(5)

rapport.set_font("Arial", '', 12)
sections = [
    ("Introduction", "Ce rapport présente une analyse exploratoire des données de ventes, réalisée à partir des fichiers clients, transactions et produits. L’objectif est de mieux comprendre les comportements d’achat, les corrélations entre variables et d’identifier des axes d’amélioration pour le business."),
    ("Méthodologie", "Les analyses ont été menées à l’aide de Python (pandas, seaborn, matplotlib, scipy) sur trois sources principales : customers.csv, transactions.csv, products.csv. Les données ont été jointes et enrichies pour permettre des analyses croisées."),
    ("Analyses et Résultats", "- Sexe des clients et catégories de produits achetés : corrélation significative (test du Chi2).\n- Âge des clients et montant total des achats : corrélation négative forte.\n- Âge des clients et fréquence d’achat : corrélation selon les groupes d’âge.\n- Âge des clients et taille du panier moyen : variations selon les tranches d’âge.\n- Âge des clients et catégories de produits : préférences selon les classes d’âge."),
    ("Visualisations", "Des graphiques (heatmaps, scatterplots, barplots) ont été générés pour illustrer la répartition des catégories de produits selon le sexe et l’âge, les corrélations entre variables numériques, et l’évolution des ventes selon l’âge."),
    ("Conclusions", "L’analyse exploratoire met en évidence des liens forts entre certaines variables démographiques et les comportements d’achat, l’importance de segmenter la clientèle, et des pistes pour approfondir l’analyse."),
    ("Recommandations", "- Approfondir l’analyse sur l’acquisition client et les canaux de vente\n- Adapter les campagnes marketing selon les segments identifiés\n- Continuer à enrichir la base de données pour affiner les analyses")
]

for title, content in sections:
    rapport.set_font("Arial", 'B', 14)
    rapport.cell(0, 10, title, ln=True)
    rapport.set_font("Arial", '', 12)
    for line in content.split('\n'):
        rapport.multi_cell(0, 8, line)
    rapport.ln(2)
    # Ajout d'une image après la section "Analyses et Résultats" et "Visualisations"
    if title == "Analyses et Résultats":
        if os.path.exists(image_paths[0]):
            rapport.image(image_paths[0], w=170)
            rapport.ln(2)
        if os.path.exists(image_paths[1]):
            rapport.image(image_paths[1], w=170)
            rapport.ln(2)
    if title == "Visualisations":
        for img in image_paths[2:]:
            if os.path.exists(img):
                rapport.image(img, w=170)
                rapport.ln(2)

rapport.output("rapport_analyse_ventes.pdf")
print("Le rapport PDF a été généré sous le nom 'rapport_analyse_ventes.pdf'.")
