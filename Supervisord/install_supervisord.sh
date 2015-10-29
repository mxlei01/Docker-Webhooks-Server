sudo apt-get install -y supervisor;
sudo mkdir -p /var/log/supervisor;
cd && cp /Docker-Webhooks-Server/Supervisord/supervisord.conf /etc/supervisor/conf.d/;
sudo mkdir /var/supervisord;
sudo /usr/bin/supervisord;
