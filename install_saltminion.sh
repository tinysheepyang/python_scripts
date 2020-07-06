#!/bin/bash

checkversion()
{
	version=$(rpm -qa|grep salt-minion|awk -F '-' '{print $3}')
	if [ ! -n "${version}" ];
	then
		echo '没有安装任何salt'
		installminion
		updatefile
		updatebin
	elif [ "${version}" == "2015.5.10" ];
	then
		echo '已安装salt-minion 2015.5.10'
		updatefile
		updatebin
	else
		echo 'salt-minion与master版本不匹配'
		rpm -e $(rpm -qa|grep salt-minion)
		if [ $? -eq '0' ];
		then
			installminion
               		updatefile
                	updatebin
		else
			echo '卸载旧版本saltminion失败'
			exit
		fi

	fi
}

installminion()
{

	if [ ! -f "/etc/yum.repos.d/epel.repo" ];
	then
		rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
		sed -i 's@^#@@' /etc/yum.repos.d/epel.repo
		sed -i 's@mirrorlist@#mirrorlist@' /etc/yum.repos.d/epel.repo
	fi
}

updatefile()
{
	file='/etc/salt/minion'
	name=$(hostname)
	echo 'hostname', $name
	if [ ! -f "${file}" ];
	then
		echo 'salt-minion no install!'
		yum install salt-minion -y

		if [ $? -eq "0" ];
		then
			sed -i "s@#master: salt@master: 192.168.0.75@g" ${file}
			#sed -i "s@#id: @id: ${name}@g" ${file}
			sed -i "s@#id:@id: ${name}@g" ${file}
		else
			exit
		fi
	elif [ ! -z "$(grep '#master: ' /etc/salt/minion)" ];
	then
		sed -i "s@#master: salt@master: 192.168.0.75@g" ${file}
        	#sed -i "s@#id: @id: ${name}@g" ${file}
        	sed -i "s@#id:@id: ${name}@g" ${file}
	else	
		sed -ir "s@master: .*@master: 192.168.0.75@g" ${file}
		sed -ir "s@id: .*@id: ${name}@g" ${file}
	fi
}

updatebin()
{
	python -V &> version.txt
	version=$(cat version.txt | awk '{print $2}')
	echo 'python version',${version}
	if [ "${version}" != "2.6.6" -a -z "$(grep 'python2.6' /usr/bin/salt-minion)" ];
	then
		sed -i "s@#!/usr/bin/python@#!/usr/bin/python2.6@g" /usr/bin/salt-minion
	fi

	/etc/init.d/salt-minion restart
	sleep 5s
	status=$(/etc/init.d/salt-minion status|awk '{print $5}')
	if [ "${status}" != "running..." -o -n "${status}" ];
	then
		rm -rf /etc/salt/pki/minion/minion_master.pub
		echo 'rm -rf minion_master.pub'
		/etc/init.d/salt-minion restart
	fi
	echo 'install minon done!'
}

main()
{
	checkversion
}

main
