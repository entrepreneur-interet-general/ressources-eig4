# Notebooks

Ce projet permet de rapidement configurer un environment jupyter lab sur sa machine.

# Utilisation

## Pré-requis
- docker
- docker-compose

## Installation

Copier le fichier `.env-template` vers `.env` :
    cp .env-template .env

Remplacer les variables à changer :
- P_NOTEBOOKS_DATA: le chemin où les données du notebook seront écrites
- JUPYTER_BASE_PORT: le port
- JUPYTER_SPARK_PORT:
- UID:
- PYSPARK_NUMBER_CORES: le nombre de core utilisés par le spark local
- PYSPARK_MEMORY_GB: le nombre de ram utilisés par le spark local


Une bonne pratique est d'avoir dans son home (ou autre part) un dossier `docker-volumes` dans lequel les différents projets pourront écrire.

Créer le dossier au path $P_NOTEBOOKS_DATA afin qu'il ne soit pas créé avec le user root lors du `docker-compose up`.
Par exemple (à modifier selon la variable $P_NOTEBOOKS_DATA de votre .env) :
    mkdir $HOME/docker-volumes/notebooks-data

Vous pouvez maintenant build les images docker
    docker-compose build

Puis lancer le serveur
    docker-compose up

Cela va faire apparaître dans les logs une url avec un token qui redirigera vers le jupyter lab.
Par exemple :
    http://127.0.0.1:8888/?token=559295c7a8f3264c6738def66cfe148d8a0702778e4ae272

## Commentaire

Les données produites et écrite dans le `/data` du container seront persistantes.

L'environment de travail sera au path `/home/jovyan/work` et ce path est rajouté au `PYTHONPATH` pour pouvoir écrire une petite librairie.

## Makefile

Le Makefile contient des commandes utiles:
```
make build           # Build le container
make run             # Lance le jupyter serveur
make logs            # Affiche les logs du serveur
make down            # Détruit l'environment et donc le serveur jupyter
make restart-jupyter-base # Détruit puis restart le serveur jupyter
make restart-jupyter-spark # Détruit puis restart le serveur jupyter
```
