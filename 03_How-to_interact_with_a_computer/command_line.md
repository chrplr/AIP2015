% Interagir en utilisant la ligne de commande
% Sylvain Charron
%

# La ligne de commande ("Shell")

C'est l'interface privilégiée avec l'ordinateur quand on veut le soumettre à notre volonté.

Elle nécessite d'utiliser un langage qui permet de communiquer avec l'ordinateur (de façon assez frustre, entendons-nous) c'est-à-dire d'envoyer des instructions à l'ordinateur et parfois voir l'output de ces instructions s'afficher à l'écran.


système|nom|pour ouvrir|langage
-------|--------|--------|------
windows|fenêtre de commande,... |win+R puis cmd| dos
mac|terminal,iterm,...|/Applications/Utilities/Terminal| bash
linux|terminal emulator,xterm,...|se loguer, Ctrl + Alt + t|bash, tcsh,...

** Exercices **

1. Accédez à une ligne de commande sur votre ordinateur.
2. identifier les informations affichées automatiquement.


# L'arborescence des fichiers

C'est une façon de se représenter et d'organiser l'information stockée dans la mémoire de l'ordinateur.

Il faut toujours savoir :

- **où on est dans cette arborescence !**
- **où se trouve ce qu'on souhaite manipuler !**


##Concepts clefs :

- **racine** : c'est le point de départ de l'organisation des informations (particularité de windows : il peut y en avoir plusieurs, une par partition)
- **repertoire** : c'est un contenant qui peut contenir des fichiers ou d'autres répertoires
- **répertoire courant** : c'est l'endroit où on se trouve à un instant donné dans l'arborescence, c'est là qu'on cherchera à ouvrir ou à écrire un fichier si on ne précise rien de plus
- **fichier** : en simplifiant ça correspond à une zone de mémoire où sont stockées des informations (texte,video,données, script,...)
- **chemin d'accès (ou _path_)** : c'est la description du chemin à suivre dans l'arborescence pour trouver un répertoire ou un fichier. Il s'agit de la suite des noms des répertoire à parcourir, séparés par un caractère `/` sous Mac et Linux et `\` sous Windows
- **chemin d'accès absolu** : c'est le chemin d'accès en partant de la racine
- **chemin relatif** : c'est le chemin d'accès à partir du répertoire courant, identifié par le signe "point" `.` tandis que le répertoire parent est identifié par le signe "point point" `..``

Tout ça peut se voir avec les outils graphiques qu'on trouve désormais couramment dans les systèmes d'exploitation.

## Gestionnaires de fichiers GUI

système|nom|pour ouvrir|racine
-------|--------|--------|------
windows|explorer|win+E| Lettre:\
mac|finder|cmd+N| /
linux|nautilus,thunar,...|commande|/

**Super important** : pour éviter les problèmes (surtout en ligne de commande), toujours utiliser des noms de répertoires et de fichiers qui suivent ces règles :
- pas d'espace
- pas de caractères hors de :
     - l'alphabet anglais majuscule et minuscule
     - les chiffres arabes
     - le `_` (on tolère aussi le `-`)
- pas le nom d'un autre truc utile


** Exercices **:

1. Trouvez sur votre ordinateur votre répertoire d'utilisateur
2. puis le répertoire racine
3. puis le répertoire où la distribution Anaconda de python est installée


## Pour aller plus loin

Les systèmes de fichiers, avec des fonctionnalités différentes et malheureusement pas forcément compatibles les uns avec les autres, correspondent à la manière de transcrire physiquement sur la mémoire cette structure. C'est pour ça qu'on a souvent de sproblèmes de transfort de fichiers en mac et PC => bien choisir comment "formater" une clef USB ou un disque dur pour partager des données

Exemples :

- FAT 32, File Allocation Table depuis windows 95 : limite la taille des fichiers à 4 Go, le seul système de fichier bien supporté par tous les systèmes d'exploitation
- NTFS, New Technology File System : depuis Windows NT, nécessite des ajouts logiciels pour être plus ou moins supporté sous mac
- exFAT, Extended File Allocation Table : Windows, à éviter comme la peste
- ext, extended file system : linux, actuellement en version ext4
- HFS et HFS+, Hierarchical File System : mac avec une taille minimale de fichier qui gaspille de l'espace



## Afficher le nom, le contenu et changer de répertoire courant

OS|langage|nom|contenu|changer | créer
---|----|--------|--------|---|---
Windows|dos|chdir|dir|chdir|mkdir
linux/OS|bash|pwd|ls|cd|mkdir
independant|python module os|os.getcwd()|os.listdir()|os.chdir()|os.mkdir()

** Essayez ces manipulations en ligne de commande avec votre système **

1. où êtes-vous quand vous ouvrez votre ligne de commande ?
2. quels sont les fichiers présents là aussi ?
1. déplacez-vous dans un répertoire où ça ne pose pas de problème de faire des tests
1. créez un répertoire qui s'appelle "test_ligne_commande" (sans les guillemets !)
1. allez dans ce répertoire


**Remarques** :

- on peut éditer des fichiers mais pas des répertoires !
- les fichiers et les répertoires comportent des méta-données (comme vos photos,emails,...) qui disent qui a le droit de faire quoi avec
- oui je sais techniquement un répertoire c'est aussi un fichier (c'est de l'info en la mémoire) mais pas la peine de s'embrouiller.
-  toutes les opérations que vous faites avec un gestionnaire sont faisable en ligne de commande (et souvent c'est plus pratique quand on a plein d'opérations à effectuer). Attention par contre, on a pas droit à l'erreur donc il vaut mieux avoir un système de suivi de version pour ses documents !
