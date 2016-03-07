# easyGigHubRepositorie

不登陆网页创建远程仓库的脚本

create a new repositorie without website

2016-03-07 update:

我真是蠢死了，github留了API可以直接使用，用命令行的CURL命令就可以实现这个功能
In cammand line, we can use command curl to post some data to a url, this cammand is used to create a new github without browser:
```
curl -i -u username -d '{"name": "new_repo_name"}' https://api.github.com/user/repos
```

