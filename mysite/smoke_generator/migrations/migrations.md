After changing, run this to make a new migration:

python3 manage.py makemigrations smoke_generator


Based upon the generated migration number, when sql migrations are needed, run this:

python3 manage.py sqlmigrate smoke_generator 0001 <change this


When ready, run this to migrate:

python3 manage.py migrate


