killall -9 uwsgi
cd affeBlog/
uwsgi -x socket.xml
sudo systemctl restart nginx.service
