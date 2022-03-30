#Contexte :

Ce projet est issu du cours Python de M2 TNAH 2021-2022.

Il consiste en une visualisation de données collectées dans le cadre d’un travail de recherche en histoire médiévale (cf. page d’accueil du site). La langue originale du document étant le latin médiéval, un certain nombre de données alternent le français et le latin (parfois approximatif) en fonction des termes utilisés. L’objectif général du dépouillement initial sur lequel s’appuie ce projet était de rester le plus fidèle possible au document source.

Ce projet a été intégralement travaillé à partir d’un ordinateur personnel sous Windows. Malgré notre vigilance à ce sujet, il est possible que le changement de système d’exploitation nuise à certaines fonctionnalités.

Une des difficultés de ce travail a été de traiter des données qui ont été conçues à partir d’un tableur excel et dont le traitement automatique n’a pas été anticipé. Cela s’est notamment avéré complexe au niveau des identifiant des reconnaissances : ceux-ci constituent une sémantique personnelle et doivent pourtant être utilisés en l’état car c’est ce code qui est repris dans les autres tables pour effectuer des renvois. Nous avons également dû traité l’absence de normalisation des données par une série de conditions imbriqués permettant de les traiter en fonction de leur expression. Nous avons veillé à la qualité des données affichées à l’aide d’une batterie de tests, mais il est possible qu’il demeure quelques incohérences à ce sujet.

De la même manière, la recherche à facette permise par la librairie whoosh n'a pas pu être généralisé en raison de la structure complexe
des données. Nous avons donc fait le choix de ne l'utiliser que pour la table Personnes

#Nota Bene :

Quelques images ont été emprunté au site personnel du propriétaire de la commanderie de Devesset, les autres sont issu de notre collection personnelle.

Le code regroupe systématiquement les données concernant les individus concernés sous le vocable « hommes », comme traduction générique du terme « homines ».

#Installation :

Pour utiliser cette application, merci de télécharger le présent répertoire git. Le programme se lance à partir d’un interpréteur python et du fichier run.py situé à la racine du dossier déposé sur github. Veillez aussi à disposer des packages listés dans le fichier requirements.txt.

Il est possible qu’un bug ait lieu au moment de la première utilisation de Flask-SQLAlchemy : 

AttributeError: module 'time' has no attribute 'clock’

Il suffit alors de modifier l’élément time.clock qui pose problème par l’élément time.time (v. aussi https://stackoverflow.com/questions/58569361/attributeerror-module-time-has-no-attribute-clock-in-python-3-8).

Pour optimiser la qualité visuelle, merci de privilégier la consultation en plein écran.