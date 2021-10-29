![AlgoInvest&Trade](logo.png)

# AlgoInvest&Trade

## Installation
Pré-requis (si vous souhaitez générer les profiles) :
* Installer `graphviz`

Dans un premier temps, cloner le repository :
```
git clone https://github.com/TBoileau/oc-python-7.git
cd oc-python-7
```

Installer les dépendances et préparer l'environnement de développement :
```
make prepare
source venv/bin/activate
make install
```

## Usage
Lancer l'application :
```
make run
```

## Tests
Lancer la suite de tests :
```
make tests
```

## Analyse du code
Dans un premier temps, pensez à éxecuter la commande qui permet de nettoyer le code :
```
make fix
```

Lancer les outils d'analyse statique :
```
make analyse
```

## Rapport
Retrouver le rapport générer par le programme [ici](https://tboileau.github.io/oc-python-7/).

## Contribuer
Veuillez prendre un moment pour lire le [guide sur la contribution](CONTRIBUTING.md).

## Changelog
[CHANGELOG.md](CHANGELOG.md) liste tous les changements effectués lors de chaque release.

## À propos
Book To Scrape a été conçu initialement par [Thomas Boileau](https://github.com/TBoileau). 
Ceci est un projet du parcours **Développeur d'application - Python** de la plateforme [Openclassrooms](https://openclassrooms.com/).
Ce projet n'a donc pas vocation a être utilisé.
Si vous avez le moindre question, contactez [Thomas Boileau](mailto:t-boileau@email.com?subject=[Github]%20AlgoInvestAndTrade)
