### Setup

1. Install dependencies
   Dans le fichier `requirements.txt`, se trouvent nos dépendances :

   - django : package django
   - django-cors-headers : package django pour la gestio du CORS
   - djangorestframework : package django pour le développement de a'application RESTFUL
   - djangorestframework-simplejwt : package django pour la gestion de token JWT
   - mysqlclient : pakcage pour la connexion au serveur MySQL

```bash
  pip install --no-cache-dir -r requirements.txt
```

2. Configure database connection

   Pour configurer la base de données, modifiez le fichier `.env` et mettez les informations de connexion à votre base de données.
   DB_HOST est le l'url de la base de données ou le nom du service de votre base de données dans le fichier `compose.yaml`

   ```
   DB_ENGINE=django.db.backends.mysql
   DB_HOST=db
   DB_PORT=3306
   DB_NAME=pokedex
   DB_USER=root
   DB_PASSWORD=root
   ```

3. Run migrations

   ```bash
     python manage.py migrate
   ```

4. Run server

   ```bash
     python manage.py migrate
   ```

5. Avec docker

   Il y'a un fichier `compose.yaml` composé de 3 services :

   - db: service pour la base de données **MariaDB**
   - adminer: service pour une interface de gestion de la base de données
   - api: service pour notre application

   ```bash
     docker-compose up -d
   ```
"# API_POKEDEX" 
