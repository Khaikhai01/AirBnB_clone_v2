#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

#installing and updating nginx
sudo apt install nginx
sudo apt update nginx -y

#creating needed folders
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

#dummy html file
sudo tee /data/web_static/releases/test/index.html <<EOF
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# creating symbolic link between the files
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#changing ownership
sudo chown -R ubuntu:ubuntu /data/

#server set up
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {    \n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

#restarting nginx
sudo service nginx restart
