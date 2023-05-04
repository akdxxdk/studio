# studio

# 人工智能算法软件开发

本项目为人工智能算法软件开发工作室Django官网
作者：孔德兴
项目时间：2023/5/4
最新更新时间：2023/5/4



# 服务器部署Django项目

## 安装Python3.X环境

	sudo apt-get install python3-dev
	sudo apt-get install python3-pip 


## 安装django相关环境

	pip install django


## 运行django项目

	python3 manage.py runserver


## 安装uwsgi环境

pip 方式安装：

	sudo pip install uwsgi

apt-get方式安装

	sudo apt-get install uwsgi


在项目文件里创建 uwsgi.ini文件,编辑文件，设置uwsgi属性：

	#添加配置选择
	[uwsgi]
	#配置和nginx连接的socket连接
	socket=127.0.0.1:8997
	#配置项目路径，项目的所在目录
	chdir=/wwwroot/studio/
	#配置wsgi接口模块文件路径,也就是wsgi.py这个文件所在的目录名
	wsgi-file=studio/wsgi.py
	#配置启动的进程数
	processes=4
	#配置每个进程的线程数
	threads=2
	#配置启动管理主进程
	master=True
	#配置存放主进程的进程号文件
	pidfile=uwsgi.pid
	#配置dump日志记录
	daemonize=uwsgi.log

配置文件介绍：

	介绍
	[uwsgi]#这个必写
	uid = nginx #使用nginx用户和组
	gid = nginx
	chdir = /webser/www/demosite #指定项目目录，在配置多站点时，不要启用
	module = demosite.wsgi #加载demosite/wsgi.py这个模块，在配置多站点时，不要启用
	master = true #启动主进程。
	processes = 2 #启动2个工作进程
	listen = 120 #设置socket的监听队列大小（默认：100）
	socket = /test/myapp.sock #指定socket文件，也可以指定为127.0.0.1:9000，这样就会监听到网络套接字
	pidfile = /var/run/uwsgi.pid #指定pid文件
	vacuum = true #当服务器退出的时候自动删除unix socket文件和pid文件。
	enable-threads = true #允许用内嵌的语言启动线程。这将允许你在app程序中产生一个子线程
	buffer-size = 32768 #设置用于uwsgi包解析的内部缓存区大小为64k。默认是4k。
	reload-mercy = 8 #设置在平滑的重启（直到接收到的请求处理完才重启）一个工作子进程中，等待这个工作结束的最长秒数。这个配置会使在平滑地重启工作子进程中，如果工作进程结束时间超过了8秒就会被强行结束（忽略之前已经接收到的请求而直接结束）
	max-requests = 5000 #为每个工作进程设置请求数的上限。当一个工作进程处理的请求数达到这个值，那么该工作进程就会被回收重用（重启）。你可以使用这个选项来默默地对抗内存泄漏
	limit-as = 256 #通过使用POSIX/UNIX的setrlimit()函数来限制每个uWSGI进程的虚拟内存使用数。这个配置会限制uWSGI的进程占用虚拟内存不超过256M。如果虚拟内存已经达到256M，并继续申请虚拟内存则会使程序报内存错误，本次的http请求将返回500错误。
	harakiri = 60 #一个请求花费的时间超过了这个harakiri超时时间，那么这个请求都会被丢弃，并且当前处理这个请求的工作进程会被回收再利用（即重启）
	stats=%(chdir)/uwsgi/uwsgi.status # status文件，可以查看uwsgi的运行状态
	pidfile=%(chdir)/uwsgi/uwsgi.pid # pid文件，通过该文件可以控制uwsgi的重启和停止
	daemonize=%(chdir)/uwsgi/uwsgi.log # 日志文件，通过该文件查看uwsgi的日志




uwsgi常用命令：

	uwsgi  --ini  /yourpath/uwsgi.ini  #启动运行
	uwsgi --stop /yourpath/uwsgi.pid  #停止运行
	uwsgi --reload /yourpath/uwsgi.pid  #重启运行

	ps -ef|grep uwsgi  #查看进程是否uwsgi启动



## 安装nginx环境

	sudo apt-get install nginx

在/etc/nginx/目录下，找到nginx.conf文件,使用该项目中nginx.conf配置文件进行替换，记得更改项目路径

	cd /etc/nginx/
	vi nginx.conf

nginx.conf


    user  nginx;
    worker_processes  auto;
    
    #error_log  /var/log/nginx/error.log notice;
    #pid        /var/run/nginx.pid;
    
    events {
        worker_connections  1024;
    }
    http {
        include       mime.types;
        default_type  application/octet-stream;
        
        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                          '$status $body_bytes_sent "$http_referer" '
                          '"$http_user_agent" "$http_x_forwarded_for"';
    
        
        sendfile        on;
        server {
            listen 80;
            server_name  www.kdx-qsbl.top; #改为自己的域名，没域名修改为127.0.0.1:80
            charset utf-8;
            location / {
               include uwsgi_params;
               uwsgi_pass 127.0.0.1:8997;  #端口要和uwsgi里配置的一样
               uwsgi_param UWSGI_SCRIPT studio.wsgi;  #wsgi.py所在的目录名+.wsgi
               uwsgi_param UWSGI_CHDIR /wwwroot/studio/; #项目路径
    
            }
            location /static/ {
            alias /wwwroot/studio/static/; #静态资源路径
            }
        }
    }


nginx常用命令：

	pkill -9 nginx  #关闭nginx进程

	/etc/init.d/nginx start  #启动nginx服务
	/etc/init.d/nginx restart  #重启nginx 服务
	/etc/init.d/nginx stop  #停止nginx 服务



## 启动服务器

正常启动服务器：

	uwsgi --ini uwsgi.ini  # 代码文件根目录下
	service nginx start 或 service nginx reload


更改后重启服务器：
	
	uwsgi --reload uwsgi/uwsgi.pid
	/etc/init.d/nginx -s reload


