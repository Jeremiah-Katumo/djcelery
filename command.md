pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/
docker build -t <container_name> .
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh  // getting into django container