#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
#IF -> verificamos si nginx esta instalado, sino, se instala
if [ "$(dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -c "ok installed")" -eq 0 ];
then
	sudo apt-get -y install nginx;
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "PAGINA DE PRUEBA" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i "/listen 80 default_server;/ a \\\trewrite ^/redirect_me https://www.anandtech.com permanent;" /etc/nginx/sites-available/default
sudo sed -i '/server_name _;/a \\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\troot /usr/share/nginx/html;\n\tinternal;\n}' /etc/nginx/sites-available/default
sudo sed -i "/listen 80 default_server;/ a \\\tadd_header X-Served-By ${HOSTNAME};" /etc/nginx/sites-available/default
sudo sed -i "23i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
