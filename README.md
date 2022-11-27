Projet softdesk

créer un repository github
créer un projet dans pycharm avec readme
faire un gitclone ssh du projet
faire un cd pour se placer dans le projet nouvellement créé
faire un vagrant init ubuntu/bionic64
Démarrer le serveur: vagrant up
Éteindre le serveur : exit
modifier le fichier par celui mis à disposition par Udemy qui est deja configuré
pour démarrer le serveur : vagrant up
pour arreter le serveur : exit
pour se connecter en ssh au serveur : vagrant ssh
pour se à connecter à l'explorateur de fichier du serveur une fois connecté en ssh: cd /vagrant
créer un venv python a la racine du seveur vagrant : python -m venv ~/env
activer le venv : source ~/env/bin/activate
desactiver le venv : desactivate
ajout des 2 requirements 
django==4.1.3
djangorestframework==3.14.0
pip install -r requirements.txt (dans l'envrionement activé)

