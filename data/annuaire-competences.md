# Atelier data science - séminaire

## Annuaire des compétences de la promo

* WSL: Antoine, Vincent et PE
* Pycharm: Line, PE, Vincent, Raphaëlle Roffo, Pengfei
* VSCode: Vincent, Raphaëlle Roffo, Antoine, Rémi
* Black python formatting: Raphaelle, Rémi
* Plotly, Dash: Vincent, Antoine, PE,
* BigQuery: Line, Rémi
* Airflow/Prefect: Raphaelle BL,
* Apache Atlas: Pengfei
* Dashboarding: Line, Raphaelle Roffo, Antoine, ...
* Neuroscience: Line, Raphaelle BL
* Conda: Line
* Deep learning: Antoine
* Touch typing: Antoine
* Vim: Antoine
* Catboost: Antoine
* ML and time series: Raphaëlle BL
* Sphynx pour la doc: Raphaelle BL
* Animation/maintien d’une ligne open source: Raphaëlle BL
* Dask - Raphaelle BL
* Unittesting - Pierre-Etienne
* FaseAPI - PE, Rémi
* Active Learning - PE, Rémi
* Desambiguation, dedupe - PE
* QGIS/ArcGIS/GeoDa, les libs python & R associées - Raphaelle Roffo
* Docker - Antoine, Pengfei, Rapahelle Roffo, Rémi, ...
* NLP preprocessing - Raphaelle Roffo, PE
* NLP libs (NLTK, beautifoulSoup, gensim...) - Raphaelle Roffo, PE
* PowerBI/DAX - Raphaelle Roffo
* Hadoop, Hive, Spark - Pengfei
* Authentication - Pengfei
* ETL, ELT, ELTLTLTL - Pengfei
* Formats de fichiers (parquet, ...) - Pengfei
* Data management, data cleaning - Pengfei
* Kepler.gl - Vincent
* Parallel coordinates plots (plotly) - Vincent
* cufflinks - Vincent


## Ateliers Expert

* Data engineering / Data cleaning - Pengfei
* Catboost/Shap - Antoine
* Sphynx - Raphaelle BL
* Prefect - Raphaelle BL
* Timeflux - Raphaelle BL
* Dask - Raphaelle BL
* MakeFile/Precommit/isort/black/test coverage - Vincent, Antoine, PE
* FastAPI vs Flask et Django - Rémi
* Dash / Plotly - Vincent, Antoine
* Preprocessing NLP - Raphaëlle Roffo
* SIG - Raphaëlle Roffo
* Authentification - Pengfei
* Docker - Remi, Vincent, ou autre
* Vim, shell, tmux (touch typing), Antoine
* Apache Atlas - Pengfei
* Google BigQuery - Line
* Python Typing - Remi
* NLP galaxy, Raphaelle Roffo, PE
* Hadoop, Hive, Spark - Pengfei
* Functionnal programming - Rémi
* ML and time series - Raphaelle BL



## Ateliers Débats

* Versioning des features (et des modèles, datasets, ...)
* Pytorch vs Jax vs Theano
* ELT, ETL vs ELTLTLT
* pip vs conda vs poetry
* Active learning
* NLP best practices
* Archi ML


## Demande d’expertise
* Cortex
* DVC
* Jax
* Apprentissage déséquilibré (imblearn)
* Text structure extraction
* OCR


## Outil de collaboration
* Documentation type EIG: Ressource data science dans la doc EIG
* Sous arborescence Annuaire, outils, ateliers, discussions
* Repo pour les sandbox
* Sessions visio (hebdo?, 30min?) enregistrées



## Conseils de lecture
Technical debt in ML systems
ML guidelines de google
Elements of statistical learning


Retours d’expérience
* Versioning des features: très compliqué à géré. Mieux vaut avoir plusieurs features. Ne jamais modifier le code d’un feature. Pattern très régulier. Un feature n’est jamais modifié.
* Truc chelou qui m’est apparu récemment: modèle qui rejette des requêtes, attention au fait de ne classifier que ce qui n’a jamais été choisi par l’autre modèle. (C’est le cas d’un modèle en production)
* Cas d’un modèle en prod: toujours laisser passer une faible portion des cas aléatoirement
* Plusieurs modèles qui s’enchainent: classe d’évaluation intermédiaire.
* Outil pipeline de sklearn: je recommande qui permet d’enchaîner différents modèles. Très pratiques
* Pour explorer les jeux de données en plus que 3 features. Chaque colonne est transformée en barres. Ca permet d’identifier des patterns en plusieurs sur des features en plusieurs dimensions. C’est dans plotly. C’est très fluide, même avec 20 millions de points.


