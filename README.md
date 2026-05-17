Global Prestige Tour

Un réseau social + tournée musicale où le prestige, l’accès et l’influence sont le moteur.

---

L’histoire

Il était une fois un couple d’influenceurs.  
Ils ne voyagent pas seuls. Ils amènent avec eux un cercle d’ami(e)s et une équipe de documentation.  

Leur mission : écrire de la musique sur eux.  
Sur leurs vies, leurs rencontres, leurs hôtels, leurs 5 minutes de gloire dans chaque ville.

Leur fonctionnement ? Un réseau social IRL.  
Tout tourne autour du prestige, de l’accès, du privilège, de l’influence.  
Chaque lieu, chaque personne, chaque moment est une story potentielle.

Ils organisent une tournée musicale dans le monde entier.  
Objectif : montrer leurs hôtels dans toutes les villes du monde sur les réseaux sociaux.  
Chaque chambre devient un décor, chaque hall un post, chaque vue une preuve.

Dans leurs backstages, il y a des horloges.  
Des horloges avec toutes les heures du monde.  
Parce qu’ici, le temps n’est pas local. Il est global.  
À côté, des piles de journaux, de magazines. Des preuves papier que c’est arrivé. Que ça compte.

---

Ce que fait ce projet

Global Prestige Tour est une app pour gérer une tournée d’influenceurs où la musique, le contenu et le statut social se mélangent.

Gestion de tournée mondiale
Planning des villes, hôtels, salles de concert
Suivi des timezones : affichage des horloges mondiales par ville
Check-in/check-out hôtels avec génération auto de contenu pour les réseaux

Réseau social interne
Profils des ami(e)s, collaborateurs, influenceurs invités
Système de prestige / accès / privilège : qui peut entrer où, qui joue quoi
Feed privé de la tournée : photos, vidéos, notes backstage

Documentation musicale
Outil pour écrire de la musique "sur" les gens de la tournée
Chaque profil peut avoir une piste, une lyric, un thème associé
Export des lyrics et setlists par ville/période

Médias & Preuves
Upload journaux, magazines, captures d’écran
Timeline média par ville pour créer un storytelling cohérent

---

Fonctionnalités clés
| Module | Description |
| **World Clocks** | Affiche l’heure locale de chaque ville de la tournée en temps réel |
| **Hotel Tracker** | Liste des hôtels visités, avec tags : luxe, rooftop, vue, suite présidentielle |
| **Social Graph** | Réseau d’amis/invités avec niveaux d’accès et influence |
| **Music Doc** | Générateur de lyrics et setlists basés sur les événements et personnes de la tournée |
| **Media Vault** | Stockage des journaux, magazines, posts, preuves de passage |
| **Period Summary** | Résumé auto par mois : villes visitées, hôtels, invités, morceaux créés |
---

Installation
git clone https://github.com/tonuser/global-prestige-tour.git
cd global-prestige-tour
bundle install
rails db:create db:migrate db:seed
rails s
Stack

Backend : Rails 7, PostgreSQL
Frontend : Hotwire + Tailwind
APIs : Google Places pour les hôtels, TimeZoneDB pour les horloges, Cloudinary pour les médias
Background Jobs : Sidekiq pour générer les résumés de période et les exports réseaux sociaux

---

Contribuer

Tu veux ajouter une ville, un hôtel, un concept de morceau basé sur un invité ?  
Ouvre une PR.  

Règle du jeu : tout doit être documenté.  
Si ce n’est pas posté, filmé, écrit, ça ne s’est pas passé.

---

Philosophie

> Ici, tout est prestige, accès, privilège ou influence.  
> Mais sans documentation, ça n’existe pas.

---

“Le monde a des horloges. Nous avons la tournée qui les fait toutes sonner.”
# global-prestige-tour
