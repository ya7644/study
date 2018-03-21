PHP的一些知识盲点
=================
#cgi,fastcgi,php-fpm
    1. cgi是个协议，定义了web server 和 app server之间数据交互。
    2. php-cgi是实现了该协议，web server 启动了一个php-cgi进程，将数据翻译为app server能理解的语言。
    3. php-fpm是个容器，按照配置启动一定数量的php-cgi,当有请求过来时，调用一个php-cgi进行解析。若无请求，则进行闲置。
    4. php-fpm的优点是当修改php.ini时，可以平滑进行重启。可减少交互的服务时间。

#在Linux系统中配置php-fpm
    1. 