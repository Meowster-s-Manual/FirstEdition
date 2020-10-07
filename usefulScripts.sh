# improting json data into db
mongoimport --jsonArray --db meowster --collection chest --file dump.json
# vue ui setup for port 8081 pi4 ip address
vue ui -H 192.168.1.111 -p 8081
# serve our web page
vue run serve
#enter mongodb in the container
mongo --username meowster --password 3L3T3
#copying dump.json to docker
docker cp dump.json mongodb:dump.json
#mongo import inside the container
mongoimport --jsonArray --db meowster --collection chest --username meowster --password 3L3T3 --authenticationDatabase admin --file dump.json

