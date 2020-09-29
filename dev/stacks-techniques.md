# Premiers choix de stacks techniques

### MonitorFish (WIP) 
Frontend: React / Angular (en fonction d'une collaboration éventuelle avec une startup d'état sur des composants front)
Backend: Spring Boot en Kotlin car c'est déjà maîtrise par les équipes (juste ils sont en Java) 
DB: postgreSQL avec PostGIS et Timescale (time series)
Pipeline data en Python 
Ops : Github + Github Actions

### Neotac 
( sous réserve de validations )
Front : ? Pas decidé pour le moment, sûrement React 
Mobile : Kotlin et/ou Java ( reco / validation ANSSI )
Backend : Python + Django + Rest framework ( a valider )
DB : Postgres 
Devops propre gendarmerie avec zip à envoyer via tickets —> implique de trouver un moyen d’automatiser un peu ça.

### SEDAccord (stack de Vitam dans lequel le projet risque de s'insérer, mais pas définitif)
Front : Angular
Back : Java 11 + Spring Boot, Kotlin si possible
"DB" : S3
(sachant que back + DB risquent d'être mocked pour les 10 mois)
Ops : Git/Github + CI Jenkins si Vitam sinon probablement Circle CI

### Atlas Culture
Front : ?
Back : Django / Python
DB : PostgreSQL / PostGIS
Ops : Github + Heroku

### Siance
Front: React (a priori, il y a déjà un truc de fait), intéressé pour une formation express en TS
Back: Python (co-écrit avec le datascientist)
Pipeline data: python/bash/cron ... 
DB: on a récupéré du postgres / elasticsearch (et des csv ...)
Ops: Pour l'instant, Gitlab-CE en "local" (dockerisé)

### Open Collectivités
Front : Vue (a priori, pas fixé)
Back : Python (Django + Django REST)
DB : Postgres

### LABEL
Langage : Typescript
Front : React
Back : Express, GraphQL
Base de données : MongoDb
Intégration Continue : pas prioritaire, git hooks au niveau du push pour l'instant, probablement Jenkins à terme
Autre outils : Docker, Eslint, Prettier
Organisation du code : monorepo



## Atelier Choix de Stack
Plusieurs problématiques quand au choix du projet : 

* Intégration : Il faut s'intégrer à une techno existante car il y a déja des équipes sur place / volonté de garder une techno spécifique
* Communication : Il est possible de s'intégrer avec l'outil existant via des services servis sous forme d'API / accès aux BDD direct ou indirect ( par réplication ) 
* Savoir faire : L'équipe de développement à un passif de connaissances sur les technos qu'elle a déja utilisé / a déjà connaissances. + L'équipe sur place dans l'administration peut avoir déja des technos connues et pas forcément envie de partir sur une toute nouvelle techno.
* Open source : Le projet open source peut permettre d'avoir un écosystème réutilisé ou peut avoir envie de recruter des développeurs ( donc techno un peu connue, avec un écosystème ou bien un réseau de développeurs ) 


## Systèmes existants : 
 * Drive collaboratif : https://drive.google.com/drive/folders/1a9-O5eSiGluSYs362343ujSyb33Wb9z6?usp=sharing
    
 ## Plan d'action : 
 * Groupe de lecture hebdo / bi-hebdo sur les pratiques du clean code.
 * Faire un atelier Git pour améliorer nos process de développement