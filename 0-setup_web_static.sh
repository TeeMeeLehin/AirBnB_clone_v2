#!/usr/bin/env bash
# Bash script to set up web server for deploying static webpages

sudo apt-get update
sudo apt-get install -y nginx

[ -d "/data/" ] || sudo mkdir -p "/data/"
[ -d "/data/web_static/" ] || sudo mkdir -p "/data/web_static/"
[ -d "/data/web_static/releases/" ] || sudo mkdir -p "/data/web_static/releases/"
[ -d "/data/web_static/shared/" ] || sudo mkdir -p "/data/web_static/shared/"
[ -d "/data/web_static/releases/test/" ] || sudo mkdir -p "/data/web_static/releases/test/"
echo "Test Page" > /data/web_static/releases/test/index.html
sudo ln -sfT /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo bash -c 'cat <<EOL > /etc/nginx/sites-available/default
server {
   listen 80 default_server;
   listen [::]:80 default_server;
   
   root /var/www/html;
   index index.html;
   
   location / {
       add_header X-Served-By \$hostname;
   }

   location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
   
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }
   
   error_page 404 /404.html;
   
   location = /404.html {
      internal;
   }
}
EOL'

sudo service nginx restart
