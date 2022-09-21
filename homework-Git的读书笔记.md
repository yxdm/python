

# **GIT的原理及基本使用方式**
## **一、GIT的原理**
### **1、什么是GIT？**

**Git**是一个开源的[**分布式版本控制系统**](https://baike.baidu.com/item/GIT/12647237?fr=aladdin)，可以有效、高速地处理从很小到非常大的项目版本管理。也是Linus Torvalds为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件。

### **2、创建自己的GIT仓库**
  我们要进行开发，提交代码和中心服务器进行交互，首先我们要有自己的一个开发基地，也就是我们自己的git仓库。
#### （1）在自己已有的目录里初始化自己的git仓库，然后和中心服务器建立连接，更新 最新代码到自己的git仓库。

#### （2）将一个已经存在的项目克隆到自己的目录成为自己的git仓库。

### **3、GIT的分层结构**
GIT的工作总共分四层，其中三层是在自己本地的git仓库，包括了工作目录，暂存区和本地仓库。
 工作目录就是我们执行命令git init时所在的地方，也就是我们执行一切文件操作的地方，暂存区和本地仓库都是在.git目录，因为它们只是用来存数据的。

 远程仓库在中心服务器，也就是我们做好工作之后推送到远程仓库，或者从远程仓库更新下来最新代码到我们的git仓库。

 git所存储的都是一系列的文件快照，然后git来跟踪这些文件快照，发现哪个文件快照有变化它就会提示你需要添加到暂存区或是提交到本地仓库来保证你的工作目录是干净的。
 ![git分层结构](https://img-blog.csdn.net/20140417104150109)

 ### **4、GIT的对象**
 GIT一共有3种对象，**commit**对象，**tree**对象和**blob**对象。

  #### (1)**blob**对象对应的就是文件快照中那些发生变化的文件内容。


  #### (2)**tree**对象则记录了文件快照中各个目录和文件的结构关系，它指向了被跟踪的快照。
  

  #### (3)**commit**对象则记录了每次提交到本地仓库的文件快照，从上图看出其中有两个指针，一个指向tree对象，一个则指向上一个commit对象。在开发过程中，我们会提交很多次文件快照，那么第一次提交的内容会用一个commit来记录，这个commit没有指针指向上一个commit对象，因为没有上一个commit，它是第一个，当第二次提交时，又会有另外一个commit对象来记录，那么这次commit对象中就会有一个指针指向上一次提交后的commit对象，经过很多次提交后就会有很多的commit对象，它们组成了一个链表，当我们要恢复哪个版本的时候，只要找到这个commit对象就能恢复那个版本的文件。而我们所谓的HEAD对象其实就指向最近一个提交的commit对象，也就是最后一个commit对象。

### **5、GIT的工作流程**
git的工作流程一般是这样的：

#### (1)在工作目录中添加、修改文件；

#### (2)将需要进行版本管理的文件放入暂存区域；

#### (3)将暂存区域的文件提交到git仓库。





## **二、GIT的基本使用方式**
### **1、GIT的环境配置**

#### **(1)下载与安装GIT**

搜索GIT，进入官网直接下载安装

#### **(2)启动GIT**

安装成功后在开始菜单中会有Git项，菜单下有3个程序

Git Bash：Unix与Linux风格的命令行，使用最多，推荐最多

Git CMD：Windows风格的命令行

Git GUI：图形界面的Git，不建议初学者使用，尽量先熟悉常用命令

#### **(3)GIT配置**

 1) 查看配置 git config -l

 2) 查看系统配置git config --system --list

 3) 查看当前用户配置git config --global --list

#### **(4)GIT相关的配置文件：**

1）Git\etc\gitconfig  ：Git 安装目录下的 gitconfig       ——系统配置文件

2）C:\Users\Administrator\ .gitconfig                   ——只适用于当前登录用户的配置

#### **(5)设置用户名与邮箱（用户标识，必要）**

 git config --global user.name "yxdm"  #名称
 git config --global user.email "2903818741.@qqcom" 

### **2、GIT项目搭建** (克隆远程仓库)

#### 1、设置本机绑定SSH公钥，实现免密码登录
1)生成公私钥
``` 
$ ssh-keygen -t rsa -C "2903818741.@qq.com"
```
2)将公钥添加到GitHub中，其中并将自己的私钥添加在相应的文件夹中与之匹配

3)克隆代码 git clone 地址
```
$ git clone git@github.com:yxdm/python.git
```
4)新建文件
```
$ vi my.py
```
5)运行新建文件
```
python my.py
```
6)后续一系列操作
```
$ git add my.py

$ git commit -m "~~~~"

$ git config --global user. email. "you@example. com"
$ git config --g1obal user .name "Your Name"

$ git commit -m "~~~~"

······

```









原文链接1：https://blog.csdn.net/xiaoputao0903/article/details/23912561/

原文链接2：https://www.bilibili.com/read/cv12961604/