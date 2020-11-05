# Juptyer notebooks

ALERT : Les notebooks ne sont pas à utiliser dans toutes les situations [petite présentation](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1)

## Une configuration "facile" via docker / docker-compose

La configuration présenté dans `src` permet :
- D'avoir un jupyter notebook de base
  - Des données persistantes sur le host
  - Un path python bien configuré
  - Les droits corrects pour ne pas écrire en sudo
  - Connecté au network de la machine host
- De build un notebook avec pyspark

## Discussion

- Pas collaboratif (on ne peut pas vraiment éditier le notebook à 2)
- Comment partager les notebooks ?
  - Pre commit pour effacer outputs + gitignore des ipynb_checkpoints
  - Export au format html mais perte des interactions
  - -> Go dash
- Installation de packages dans l'environment

Infra s'appuyant sur des notebooks :
- [Papermill](https://papermill.readthedocs.io/en/latest/)
- [Netflix infrastructure](https://netflixtechblog.com/notebook-innovation-591ee3221233)
- [Nope to the netflix infrastructure](https://www.youtube.com/watch?v=P-sWU2bNpPw&t)
