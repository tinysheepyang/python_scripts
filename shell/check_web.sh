#!/bin/bash

# Filename: check_web.sh
# Revision: 1.3
# Auther: chenshiyang
# Date: 2015-12-15
# Description:web服务的监控，进程挂起，加强频率,
#脚本需要给定三个参数：ip、端口、url、频率
#向指定IP的端口去访问指定的URL
#进程需要挂起，频率是指每几秒执行一次
# Usage: /bin/bash check_web.sh -H 域名 -i ip  -u url -f 频率
# 例如： /bin/bash check_web.sh -H news.emao.com -i 182.92.217.110 -u news/20 \
#1511/15627.html?n_zxl -f 5 &
# Notes:脚本 -h或者--help 获得帮助信息


#ARGS=$(getargs -a -o i:p:u:f:H: -l ip:,port:Host,url:fre:,help -- "$@")
#[ $? -ne 0 ] && run_help
#set -- "${ARGS}"
#eval set -- "${ARGS}"


#获取参数
getargs()
{
	while true
	do
		case "$1" in
		-i|--ip)
			ip="$2"
			shift
			;;
		-p|--port)
			port="$2"
			shift
			;;
		-u|--url)
			url="$2"
			shift
			;;
		-f|--fre)
			fre="$2"
			shift
			;;
		-H|--Host)
			Host="$2"
			shift
			;;
		-h|--help)
			run_help
			;;
		--)
			shift
			break
			;;
		esac
	shift
	if [ -n "${Host}" -a -n "${fre}" -a -n "${ip}" -a -n "${url}" ]
	then
		exist "${Host}" "${ip}" "${url}"
		sleep ${fre}
	fi
	done
}

#访问指定url接受四个参数Host IP URL 频率
check_web()
{

    setlog info "开始执行 curl -m 10 -o /dev/null -s -w %{http_code} \
-H Host:${Host} http://${ip}/${url}"

    http_code=$(curl -m 10 -o /dev/null -s -w %{http_code} \
		-H Host:${Host} http://${ip}/${url})

    setlog info "http_code is ${http_code}..."
    if [ "${http_code}" == "502" ];
    then
	    setlog error "http_code is 502,trystart now..."
	    trystart

	    setlog info "php-fpm restart 后开始再次获取 http_code..."
	    http_code=$(curl -m 10 -o /dev/null -s -w %{http_code} \
		-H Host:${Host} http://${ip}/${url})

	    setlog info "php-fpm restart, http_code is ${http_code}..."
	    if [ "${http_code}" != "200" ];
	    then
		    setlog warning "nginx status unkown, restarting now..."
		    sudo /etc/init.d/nginx restart
	    fi
    elif [ "${http_code}" == "404" ];
    then
	    setlog error "http_code is 404,不知道怎么办了..."
    elif [ "${http_code}" == "200" ];
    then
	    setlog info "http_code is 200,Going to sleep..."
    fi
}

#判断自身是否存在
exist()
{
    if [ "$(ps -ef | grep "$(basename $0)" | grep -v grep | wc -l)" -gt "3" ];
    then
	    setlog info "Good,check_web.sh is running..."
	    exit 2
    else
	    setlog info "getopt获取到参数，开始调用check_web..."
	    check_web "${Host}" "${ip}" "${url}"
    fi

}

#重启
trystart()
{
	phpprocess=$(ps -ef|grep php-fpm|grep -v grep|awk '{print $2}'|wc -l)
	if [ ! -n "${phpprocess}" ];
	then
		setlog error "Maybe php-fpm is stop, tring to start it ..."
		sudo /etc/init.d/php-fpm start
	else
		setlog error "Maybe php-fpm is dead, tring to restart it ..."
		sudo /etc/init.d/php-fpm restart
	fi

}

setlog()
{
	nowtime=$(date "+%Y-%m-%d %H:%M:%S")
	level=$1
	info=$2
	logpath=/var/log/nginx/app/ops/
	logfile=${logpath}/check_web.log
	[ -z "${info}"  ] && return 0
	[ -d ${logpath}  ] || mkdir -p ${logpath}
	echo ${nowtime} ${level} ${info} >> ${logfile}

}


#帮助信息
run_help()
{
	if [ "$#" -ne "8"  ];
	then
		echo "Usage: /bin/bash check_web.sh -H 域名 -i ip -u url -f 频率

		例如：在web服务服务器上运行此脚本。域名是new.emao.com ip是 \
182.92.217.110 五秒访问一次
		/bin/bash check_web.sh -H news.emao.com -i \
182.92.217.110 -u news/201511/15627.html?n_zxl -f 5 &"
	    exit
	fi
}


main()
{
	run_help $*
	getargs $*
}

main $*
