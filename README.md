sudo docker run  -p 5000:5000 -v "$(pwd):/app" smorest
sudo docker run  -p 5000:5000 -w /app -v "$(pwd):/app" smorest
http://172.17.0.2:5000/swagger-ui