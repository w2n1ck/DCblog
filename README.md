# DCblog
#### 1. 介绍

博客系统使用python编写，基于[Django]()和[clean-blog](https://startbootstrap.com/themes/clean-blog/)前端框架编写。

我理解的博客系统只需专注于写作和阅读即可，不应该有太多胡里花哨的功能。

主要有如下功能：

提供一般的登录、注册、注销功能（线上已关闭注册），可添加文章，如果文章归属自己，可编辑文章，标签页归档该所有标签及所对应的文章，关于页添加介绍、联系等，提供分页功能。

**首页：**如果没有登录，后面的添加文章和注销将不展示。登录页可根据urls设置复杂点，线上注册可关闭。单页展示十个，可进行前后翻页。

![](http://blog.w2n1ck.com/index.png)

**添加文章：**可自定义文章背景图，文章正文采用markdown格式，Typora写完之后使用源码模式，复制粘贴一把梭，非常爽，展示时可完美解析

![](http://blog.w2n1ck.com/dcblog-add.png)

**标签页：**标签页展示所有标签，并展示对应标签页下的所有文章简介及链接。

![](http://blog.w2n1ck.com/tag.png)

**关于页：**设置了关于作者、联系方式、友链等。

![](http://blog.w2n1ck.com/about.png)

登录注册：比较简单，就使用了modelForm。

![](http://blog.w2n1ck.com/register.png)

![](http://blog.w2n1ck.com/login.png)

**文章详情页：**文章详情解析markdown正文，如果登录且文章为当前用户创建则显示编辑按钮。

![](http://blog.w2n1ck.com/detail.png)

#### 2. 源代码

Github地址：https://github.com/w2n1ck/DCblog/

线上地址：https://www.w2n1ck.com/

#### 3. 配置部署

部署使用Nginx+Gunicorn+Supervisor+Certbot，也是常见的python框架部署方式。

**nginx配置文件：**

```bash
[root@iZ2ze5t3hfgmgimaizhwq2Z conf.d]# cat dcblog_nginx.conf 
server {
    charset utf-8;
    listen 80;
    server_name www.w2n1ck.com;
 
    location /static {
        alias /var/www/html/static;
    }
 
    location / {
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:58000;
    }
}
```

**Gunicorn命令：**

```bash
gunicorn dcblog.wsgi -w 2 -k gthread -b 127.0.0.1:58000
```

**Supervisor配置：**

```bash
[root@iZ2ze5t3hfgmgimaizhwq2Z conf.d]# cat dcblog_supervisor.ini 
[program:dcblog]
command=gunicorn dcblog.wsgi -w 2 -k gthread -b 127.0.0.1:58000
directory=/root/dcblog
autostart=true
autorestart=unexpected
user=root
stdout_logfile=/root/dcblog/supervisor/var/log/dcblog-stdout.log
stderr_logfile=/root/dcblog/supervisor/var/log/dcblog-stderr.log
```

**HTTPS证书：**

```bash
yum -y install yum-utils
yum install -y certbot python2-certbot-nginx
certbot --nginx
# 设置定时任务保证不过期
echo "0 0,12 * * * root python -c 'import random; import time; time.sleep(random.random() * 3600)' && certbot renew" | sudo tee -a /etc/crontab > /dev/null
```
