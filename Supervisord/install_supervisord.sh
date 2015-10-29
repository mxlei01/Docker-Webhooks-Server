sudo apt-get install -y supervisor;
sudo mkdir -p /var/log/supervisor;
cd && sudo cp /Docker-Webhooks-Server/Supervisord/supervisord.conf /usr/etc/supervisord.conf;
sudo mkdir /var/supervisord;
sudo /usr/bin/supervisord;
