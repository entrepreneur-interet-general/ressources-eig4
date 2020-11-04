# Juptyer notebooks

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
