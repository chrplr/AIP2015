% Getting a copy of the course materials
% Christophe Pallier & Sylvain Charron
% Sept. 2015

Le cours AIP2015 est accessible sur deux dépôts ("repositories") git.

- L'un se trouve sur un site web sur Internet: https://github.com/chrplr/AIP2015

- L'autre est accessible sur le réseau wifi local "synapse" à l'adresse: student@192.168.0.2:Sites/cogmaster2015/AIP2015 (mot de passe: Ie5h,Ps'e&jn'aps)

Ce document explique comment récupérer le cours en utilisant le programme git que vous devez avoir installé sur votre ordinateur (cf. les [instructions d'installation](../00_Installation/install.html)).

Le principe est le suivant:

* vous allez créer, une fois pour toutes, une copie locale du cours sur votre ordinateur ("clonage").

* Ensuite, à tout moment, vous pourrez très simplement mettre à jour les fichiers modifiés par les enseignants.


## Création d'une copie locale

La toute première fois, vous devrez *cloner* un des repositories sur votre ordinateur, c'est à dire créer un répertoire AIP2015 contenant tous les fichiers du cours.

Si vous êtes sous Windows, ouvrez 'git shell', sous les autres sytèmes, ouvrez un terminal.

Tapez les  lignes de commandes suivantes:

* Si vous êtes connecté à Internet:

```
     git clone  https://github.com/chrplr/AIP2015 
```


* Si vous êtes connecté au reseau wifi local "synapse":

```
git clone  student@192.168.0.2:Sites/cogmaster2015/AIP2015 
```


Quand un mot de passe est demandé, tapez `test` et appuyez sur 'Entrée'.
(il est normal que le mot de passe ne s'affiche pas)

* Puis tapez les commandes suivantes:

```
cd AIP2015
git remote add synapse student@192.168.0.2:Sites/cogmaster2015/AIP2015
git remote add internet https://github.com/chrplr/AIP2015
```


* Et vérifiez si la configuration est correcte:

```
git remote -v
```

Vous devriez voir s'afficher:

```
internet        https://github.com/chrplr/AIP2015.git (fetch)
internet        https://github.com/chrplr/AIP2015.git (push)
synapse student@192.168.0.2:Sites/cogmaster2015/AIP2015 (fetch)
synapse student@192.168.0.2:Sites/cogmaster2015/AIP2015 (push)
```


## Mises à jour

Pour mettre à jour le contenu du répertoire AIP2015

1. Lancez un shell qui puisse interpréter les commandes **git** :

 - si vous êtes sous window, lancez le `Git Shell` depuis le raccourci sur votre bureau
 - si vous êtes sous mac ou linux, ouvrez un terminal

2. Déplacez-vous dans votre arborescence de fichier de telle sorte qu'**AIP2015** soit votre répertoire courant

 - version courte : selon votre OS et la méthode choisie pour le clonage initial, exécutez

```
cd AIP2015
```

ou

```
cd GitHub/AIP2015
```

 - version longue, typiquement si vous avez déplacé le répertoire AIP2015 après son clonage : localisez le répertoire AIP2015 dans votre arborescence puis exécutez la commande `cd chemin_vers_votre_repertoire_AIP2015` où il faut évidemment remplacer "chemin_vers_votre_repertoire_AIP2015" par le chemin d'accès dans votre cas particulier.

3. Exécutez la commande **git** qui met à jour votre répertoire **AIP2015** depuis l'un des deux "remote repository" du réseau

 * Si vous êtes connecté à Internet :

```
git pull internet master
```

 * Si vous êtes connecté au réseau wifi local "synapse" :

```
git pull synapse master
```

En cas de conflit empêchant la mise à jour tapez

```
git reset --hard
```

Cela effacera toutes les modifications que vous aurez pu faire dans AIP2015, permettant la mise à jour. Vous n'avez plus qu'a effectuer un des deux git pull ci-dessus.

That's all!
