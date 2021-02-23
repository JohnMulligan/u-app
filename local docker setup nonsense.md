local docker setup nonsense
docker-machine restart
docker-machine env default 
eval $(docker-machine env default)  

note: docker-machine does not like it at all when i'm logged in to vpn 