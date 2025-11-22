# Docker-projet-N-Ashley-Tania

Générateur de noms de groupes – Projet Docker

## Table des matières
- [Lancer le projet](#lancer-le-projet)
- [Gestion des environnements](#gestion-des-environnements)
- [Liens utiles](#liens-utiles)
- [Remarques](#remarques)

## Lancer le projet

Ce projet utilise Docker Compose pour lancer une application Flask, une base MySQL et un outil d’administration.

1. Cloner le projet
   git clone https://github.com/NGAMGA/Docker-projet-N-Ashley-Tania.git
   
   cd Docker-projet-N-Ashley-Tania

2. Préparer les variables d'environnement

   cp .env.dist .env


3. Lancer les services

   docker compose up --build

4. Accéder aux services

   Application : http://localhost:8085

   phpMyAdmin : http://localhost:8086

   utilisateur : banduser

   mot de passe : bandpass

5. Construire l’image pour la mise en productions
   docker build -t bandnamesgenerator:1.0.0 ./web

## Gestion des environnements

En fonction de l’environnement (développement ou production), plusieurs paramètres peuvent changer :

- Les identifiants et mots de passe dans le fichier .env.
- Les ports exposés pour l’application.
- Le serveur MySQL utilisé (local en développement, distant en production).
- Le mode debug de Flask (activé en développement, désactivé en production).
- Le service phpMyAdmin ne serait pas déployé en production pour des raisons de sécurité.

## Liens utiles

Voici les ressources utilisées pour mener à bien le projet :

- Documentation Docker
- Documentation Docker Compose
- Documentation MySQL
- Documentation phpMyAdmin
- Supports de cours du module Conteneurisation

## Remarques

Ce projet m’a permis de mieux comprendre le fonctionnement de Docker et des architectures multi-conteneurs.  
J’ai rencontré quelques difficultés au niveau de la connexion MySQL, mais cela m’a aidée à pratiquer la résolution d’erreurs liées aux conteneurs et aux variables d’environnement.