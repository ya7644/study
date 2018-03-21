#composer常用命令汇总

##查看composer所有目录
	composer list
##创建composer.json文件
	composer init
##获取依赖包
1.0 根据composer.json的配置进行创建，成功后将生成composer.lock文件
	composer install 
2.0 直接使用composer create-project命令进行创建。
	composer create-project [package]{=version} (拓展)
常见拓展
    --prefer-source 下载source目录下的文件
    --prefer-dist   下载正式发布的版本
    --dev           下载request-dev里的版本包
    --no-dev        跳过request-dev里的包
    