#!/bin/bash

logpath=/var/log/zabbix-agent/
[ -d ${logpath} ] || mkdir -p ${logpath}

groupadd zabbix-agent
useradd -g zabbix-agent zabbix-agent
chown -R zabbix-agent:zabbix-agent ${logpath}

filepath=/usr/local/src/
[ -d ${filepath} ] || mkdir -p ${filepath}

yum install lftp -y

if [ $? -eq "0" ];
then


	echo "================connect SFTP==================="
	lftp -u root,123qwe sftp://192.168.0.142 <<EOF

	cd /usr/local/src/
	lcd ${filepath}
	get zabbix-3.0.4.tar.gz
	by
EOF
	echo "================SFTP get done ==================="

	cd ${filepath}
	tar zxvf zabbix-3.0.4.tar.gz -C ${filepath}
	cd zabbix-3.0.4 && ./configure --prefix=/usr/local/zabbix-agent --enable-agent && make install
	#sed -i "s@LogFile=/tmp/zabbix_agentd.log@LogFile=/var/log/zabbix/zabbix_agentd.log@g" /usr/local/zabbix/etc/zabbix_agentd.conf
	#sed -i "s@Server=127.0.0.1@Server=192.168.0.142" /usr/local/zabbix/etc/zabbix_agentd.conf
	cd /usr/local/zabbix-agent/etc/ && rm -f zabbix_agentd.conf

	lftp -u root,123qwe sftp://192.168.0.142 <<EOF
        cd /usr/local/zabbix-agent/etc/
        lcd /usr/local/zabbix-agent/etc/
        get zabbix_agentd.conf
        by
EOF
        echo "================SFTP get done ==================="
	ip=$(/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:")
	sed -i "s@ListenIP=192.168.0.142@ListenIP=${ip}@g" /usr/local/zabbix-agent/etc/zabbix_agentd.conf

	ln -s /usr/local/zabbix-agent/etc/ /etc/zabbix
	ln -s /usr/local/zabbix-agent/bin/* /usr/bin
	ln -s /usr/local/zabbix-agent/sbin/* /usr/sbin/
	cp /usr/local/src/zabbix-3.0.4/misc/init.d/fedora/core/zabbix_agentd /etc/init.d/ && chmod 755 /etc/init.d/zabbix_agentd
	sed -i "s@BASEDIR=/usr/local@BASEDIR=/usr/local/zabbix-agent@g" /etc/init.d/zabbix_agentd 
	chkconfig zabbix_agentd on
	service zabbix_agentd start	
	exit 0

fi
