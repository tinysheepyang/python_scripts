#!/bin/bash


echo "================connect SFTP==================="
        lftp -u root,123qwe sftp://192.168.0.75 <<EOF

        cd /opt/base/
        lcd /tmp/
        get MySQL-python-1.2.3.tar.gz
        by
EOF
echo "================SFTP get done ==================="

yum -y install mysql-devel libxml2 libxml2-dev libxslt* zlib gcc openssl python-devel mysql-devel
cd /tmp
tar zxvf MySQL-python-1.2.3.tar.gz -C /tmp
cd MySQL-python-1.2.3 && python setup.py build && python setup.py install

ed -i '$a mysql.user: 'root'\nmysql.pass: '123456'\nmysql.db: 'salt'\nmysql.port: 3306\nmysql.ssl_ca: None\nmysql.ssl_cert: None\nmysql.ssl_key: None' /etc/salt/minion
