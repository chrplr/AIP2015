% Getting a copy of the course materials
% Christophe Pallier & Sylvain Charron
% Sept. 2015

Le cours AIP2015 est accessible sur deux repositories git.

- L'un se trouve sur un site web sur Internet: https://github.com/chrplr/AIP2015

- L'autre est accessible sur le réseau local wifi 'synapse' à l'adresse: student@192.168.0.2:Sites/cogmaster2015/AIP2015 (mot de passe: Ie5h,Ps'e&jn'aps)

Ce document explique comment récupérer le cours en utilisant le programme git que vous devez avoir installé sur votre ordinateur.

Le principe est le suivant:

* vous allez créer, un fois pour toutes, une copie locale du cours sur votre ordinateur ("clonage").

* Ensuite, à tout moment, vous pourrez très simplement mettre à jour les fichiers modifiés par les enseignants.



## Create a local copy the first time

La toute première fois, vous devrez *cloner* un des repositoryies sur votre ordinateur, c'est à dire créer un répertoire AIP2015 contenant tous les fichiers du cours. 

 Ouvrez un terminal (*) et tapez les  lignes de commandes suivantes:

* Si vous êtes connecté à Internet:

```
git clone  https://github.com/chrplr/AIP2015 internet
cd AIP2015
git remote add synapse student@192.168.0.2:Sites/cogmaster2015/AIP2015
```

* Si vous êtes connecté au reseau wifi local 'synapse':

```
git clone  student@192.168.0.2:Sites/cogmaster2015/AIP2015 synapse
cd AIP2015
git remote add internet https://github.com/chrplr/AIP2015
```

* Vérifier si la configuration est correcte:

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

Pour mettre à jour le contenu du répertoire AIP2015, ouvrez un terminal;

* Si vous êtes connecté à Internet 

```
cd AIP2015
git pull internet master
```

* Si vous êtes connecté à synapse:

```
cd AIP2015
git pull synapse master
```


That's all!


