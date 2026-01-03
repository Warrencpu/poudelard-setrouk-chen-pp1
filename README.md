####Présentation du projet####

Dans ce projet : "Projet Poudelard : L'art de coder comme un sorcier", nous avons réalisé un petit jeu interactif inspiré de l’univers de Harry Potter. Le jeu est de type jeu de role sans interface graphique. Il se lance et se joue directement dans le terminal Python, où le joueur doit faire différents choix pour faire avancer l’histoire. Le jeu est découpé en quatre chapitres.

Le projet a été réalisé par Elsa Setrouk et Warren Chen. Nous avons commencé par créer un dépôt GitHub afin de stocker le projet, puis nous avons cloné le dépôt sur Pycharm pour pouvoir travailler dessus. Pour commencer le jeu, il suffit de lancer le programme dans main.
Pycharm permet de travailler sur plusieurs fenêtres en même temps ce qui rend le code plus agréable à lire et permet de bien dissocier les différentes fonctions.

Afin de lancer le programme, il suffit d'exécuter le code qu'on souhaite faire marcher, l'application permet de créer une fonction pour chaque demande/mission pour que le code soit optimisée et plus fluide, mais aussi de partager notre travail plus facilement et rapidement au sein du groupe avec le commit , le push et le pull. 

####Journal de bord####

Le projet a débuté le 28 novembre 2025. Au départ, nous avons rencontré des problèmes matériels qui nous ont ralentis et nous ont empêchés de nous familiariser rapidement avec Git et PyCharm.

Le 12 janvier 2025, nous avons travaillé sur le fichier input_utils et réparti les tâches de manière équitable, avec une répartition d’environ 50 % du travail pour chacun.

Le 12 décembre 2025, les problèmes matériels ont été résolus et nous avons pu réellement commencer le développement du jeu. Nous avons alors commencé le chapitre 1. Les fonctions permettant de recevoir la lettre, de rencontrer Hagrid et d’acheter les fournitures ont été développées par Warren Chen, puis corrigées et déboguées par Elsa Setrouk. Le lancement du chapitre 1 a été réalisé par Elsa Setrouk.

Le 18 décembre 2025, nous avons commencé le chapitre 2. La fonction permettant de rencontrer les amis a été faite par Elsa Setrouk, le mot de bienvenue par Warren Chen et la cérémonie de répartition par Elsa Setrouk. Le lancement du chapitre 2 a été réalisé par Warren Chen.

Le 20 décembre 2025, nous avons travaillé sur le chapitre 3. La fonction d’apprentissage des sorts a été développée par Warren Chen, le quiz de magie par Elsa Setrouk, et la fonction permettant de lancer le chapitre 3 par Warren Chen.

Le 2 janvier, nous avons finalisé le chapitre 4 dont toutes les fonctions ont été programmées par Elsa Setrouk. Puis, nous avons repris toutes les petites erreurs d'affichage le 3 janvier afin de rendre le programme plus agréable pour les joueurs.

####Contrôle, Tests et Validation####

Il est primordial de verifier chaque entrée du joueur afin que ça ne crée pas de bug et arrête brusquement la partie.
C'est pour cela que toute entrée de chiffre/nombre, de texte ou bien meme de choix passe obligatoirement par les fonctions dans input_utils qui assurent la bonne continuation du code , l'absence d'erreur et la bonne gestion des entrées.

Nous avons dû faire face à de nombreuses erreurs et bug, la fonction demander_nombre a été la premiere à nous créer du souci, car nous n'avions pas compris qu'il suffisait de convertir l'entrée du joueur en int pour le reconvertir en string après
La méthode la plus utilisée afin de résoudre tout type de bug était de faire marcher le code en affichant la valeur de la ligne qui posait probleme (avec print) avant de l'exécuter pour pouvoir comparer sa valeur à la valeur qu'elle devrait avoir.

La manipulation des dictionnaires a été à plusieurs reprises hasardeuses et le chapitre 4 a engendré de nombreuses érreurs.
La fonction manche a été difficile à implementer à cause de la manipulation du dictionnaire des faiblesses et resistances des sorts qui été mal mis en place au début (il y avait écrit le type de sortilege que dans la clé et seulement les dégâts dans les valeurs), nous avons donc converti ces valeurs en tuples et non en listes. 
Le changement de l'implémentation du dictionnaire a aidé à optimiser le code.
Finalement la partie la plus dure a implementer a été la fonction probabilité, car nous avions du mal à comprendre comment calculer les probabilities à chaque manche pour chaque sort, de plus la fonction manche était longue donc nous l'avons divisé en deux en créant une fonction attaques qui nous a permis de mieux comprendre le fonctionnement.
Nous avons petit à petit debug la fonction probabilité avec des print verifiant la valeur de certaines variables jusqu'à finir par avoir une fonction qui marche parfaitement.
Les affichages à l'écran pour le joueur n'était pas les simples à faire, mais ont été corrigées asser rapidement.
![]("C:\Users\elsas\OneDrive\Images\Screenshots\Capture d'écran 2025-12-20 163820.png")
![]("C:\Users\elsas\OneDrive\Images\Screenshots\Capture d'écran 2026-01-03 023035.png")
![]("C:\Users\elsas\OneDrive\Images\Screenshots\Capture d'écran 2026-01-03 162625.png")