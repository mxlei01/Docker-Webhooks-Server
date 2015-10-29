sudo apt-get install -y supervisor;
mkdir -p /var/log/supervisor;
cd && mv /Docker-Webhooks-Server/Supervisord /etc/supervisor/conf.d/supervisord.conf;
mkdir /var/supervisord;
/usr/bin/supervisord;
