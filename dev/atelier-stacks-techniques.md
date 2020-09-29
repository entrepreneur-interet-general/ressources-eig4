# Atelier Stacks Techniques

### Que venez-vous chercher dans cet atelier ?
* AlexandraL : j'entends pas mal devops, j'aimerais connaître les pratiques de ce métier, on en aura tous besoin dans nos admins, est-ce qu'il y a des bonnes pratiques ?
* Raphaël : je m'occupe de la partie data et back, je vais toucher au devops, je suis très mauvais, j'aimerais des ressources
* Aliaume : comment tu mets en place un système devops dans une administration, quel est le minimum à demander aux administrations ? Ils ont rien dans la mienne, une base PostGres sur un server, comment tu gères la sécurité si tu le mets en externe ?
* Joseph : je suis à fond dans Github Actions (CI / CD fourni par Microsoft), j'aimerais bien m'ouvrir un peu, voir ce qu'on peut faire de plus
* Sylvain : connaître les bonnes pratiques aussi, je me suis formé sur le tas
* Benoit : connaître les bonnes pratiques, j'ai un Docker qui tourne en local mais je ne sais pas comment le mettre sur le serveur

### Présentation de ce qu'est Docker par Benoit

1) C'est un service de « filesystem layers » avec du cache
2) Ce ne sont pas des VM
3) Notion image vs container

### A quoi avez-vous accès comme infra ?
- Sylvain : j'ai un accès à un serveur OVH, j'ai les accès root
- Benoit : j'ai un server auquel je peux me connecter en SSH mais qui n'a pas internet dessus
- Alexandra : je suis sur Heroku, je suis sur Code anywhere (IDE en ligne), je fais du Rails, je déploie sur Heroku, c'est hyper pratique (et gratuit). On n'a pas d'appels à des BDDs internes, les données sont chargées via des fichiers CSV (données publiques). Attention au trafic 
- Raphaël : on bosse avec Octo Technology (société de conseil data et dev), donc ils gèrent la CI / CD, tout est sur Gitlab, on peut facilement se brancher sur eux et mettre en recette facilement
- Aliaume : on nous donne des machines virtuelles sur les serveurs virtuels de l'ASN, on est admin dessus, il  y avait des prestas dessus et ils copiaient un zip à chaque fois.
- Joseph : à l'INSEE, on a une salle server avec un environnement conteneurisé, ce sont des évangélistes CI/CD, ils ont Kubernetes, si vous avez des questions sur le sujet, vous pouvez leur demander
- Joseph : si vous travaillez sur Node, j'ai un repo sur Github où il y a la CI/CD configurée pour qu'à chaque fois qu'on pousse il run les tests, s'il détecte que le package.json a été changé il modifie le changelog. Si vous voulez déployer un outil en Open source, vous pouvez cloner mon repo, et il va créer un Readme, un boilerplate, vous aurez une library que vous pourrez installer. Lien : https://github.com/garronej/ts_ci. Je vous conseille de faire un repo dans lequel vous externalisez toutes les actions que vous faites dans votre CI, plutôt que d'écrire ça en bash dans votre .yml.

TODO: Présentation de comment fonctionne une CI/CD par Joseph

### Vous tenez une doc à côté de ce que vous faites ?
* Sylvain : j'utilise un wiki perso. J'aimerais bien avoir un outil pour voir rapidement sur quel server j'ai mis quel site web, il va taper sur quelle BDD, il utilise quel CMS sur quelle version ?
* Raphaël : il y a un package Python qui permet de produire un doc un peu formattée comme ça, qui s'appelle diagrams.


### Objectifs et contraintes 
1) Mise à jour, pérennisation du back et de la stack
2) Faciliter le dév
3) Permettre un transfert de connaissances pour les suivants

### Exemple de workflow
1) Faire fonctionner en local avec Docker
2) Push sur un service
3) Pull sur la machine qui va bien en dev
4) Pull sur la machine qui va bien en prod

### Questions
- Interface avec des BDD locales ?
- Serveurs déconnectés d'internet ?
- Il faut pull périodiquement pour savoir si quelque chose à changé... Mieux vaut déclencher une action au push.
- Dialogue avec la DSI quant à l'ouverture des ports.

