#!/usr/bin/env bash
# Bash script that sets up your webs servers for the deployment of web_static

apt-get update
apt-get install nginx -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "/server_name _/a location \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/;\n}" /etc/nginx/sites-available/default
service nginx restart
exit 0
