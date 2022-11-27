Projet softdesk

créer un repository github
créer un projet dans pycharm avec "README.md"
faire un gitclone ssh du projet
faire un cd pour se placer dans le projet nouvellement créé
faire un "vagrant init ubuntu/bionic64"
Démarrer le serveur: "vagrant up"
Éteindre le serveur : "exit"
modifier le fichier par celui mis à disposition par Udemy qui est deja configuré
pour démarrer le serveur : "vagrant up"
pour arreter le serveur : "exit"
pour se connecter en ssh au serveur : "vagrant ssh"
pour se à connecter à l'explorateur de fichier du serveur une fois connecté en ssh: "cd /vagrant"
créer un venv python a la racine du seveur vagrant : "python -m venv ~/env"
activer le venv : "source ~/env/bin/activate"
desactiver le venv : "desactivate"
ajout des 2 requirements 
django==4.1.3
djangorestframework==3.14.0
"pip install -r requirements.txt" (dans l'environement activé)
création du projet django: "django-admin.py startproject softdesk_project ."
creation de la 1ere app API: "python manage.py startapp profiles_api"
ajouter dans les applications du settings.py du django :
    'rest_framework',
    'rest_framework.authtoken',
    'profiles_api',
pour tester les ajouts, demarrer django: "python manage.py runserver 0.0.0.0:8000", se connecter sur un browser à "http://127.0.0.1:8000/"


