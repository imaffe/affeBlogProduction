## Manual  Deployment on Digital Ocean Centos 7

#### pycharm to github

if you are using pycharm, the first thing you need to do is to make an .gitignore file if you haven't

- if you added a .gitignore at the very beginning

  add an .gitignore in your django project (same level with manage.py), you'll need to ignore the  .idea/  venv/   sqlite3.db and other cache files, (like cache for pyc), i'm not listing everything out but you should find out what you want to ignore in your project, you can find demo code in my github repo [affeBlog](https://github.com/imaffe/affeBlogProduction) (dive into affeBlog dir)

- if you've already done a lot in local pycharm, now you'll find that your new added .gitignore file might not work. I'm not sure about this, but : .gitignore works only for files hadn't been tracked yet. So if you've already added some trash in your git repo, you should find some useful commands on Stackoverflow or something on that.

#### create an Digital Ocean Droplet

- my droplet setting : the cheapest, centos7
- configure you centos7 remote server s周杰伦o that you can really ssh into that, and trust me, Digital Ocean ssh service is not that good. You can see tutorials on Digital Ocean [Inital Server Setup with Centos7](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-centos-7), and I'll tell why you'll need to do this
  - add a new user and give it sudo and ssh permission
  - if you want to add a second ssh key, it has something to do with the authorized_keys file and again you'll need to find that on Stackover flow, only notice that there is not a single space between two keys.
- install git on your server so you can do everything

#### build your developing environment

The build script is in build/build.sh in my git https://www.digitalocean.com/community/tutorials/initial-server-setup-with-centos-7repo. You don't need to do that exactly as i did, but i really want you to know what is the purpose of the codes.

- dev environments  : i don't know what the things in the first few line are doing but they are really important. I saw almost every server need them, so don't ask anything, just do what others said. (but if you are really curious you can find them on wiki and i MIGHT post them on my website as some asides.)
- python : more specifically is python3. You have various ways to install python3 on your host and mine is just one of them. It might be outdated so use Google and stackoverflow if you are wrong with something. Only notice that i suggest you install python3-dev first ecause i couldn't install python3-dev after installed python3, and my pip didn't work as expected. So i first install python3-dev. 
- uwsgi & nginx : I met some terrible problems when installing uwsgi. You have to do the pip upgrade first or you will fail. Again, anyproblem go to stackoverflow. Through this project i knew that finding answers quickly is an important skill as well.

#### change your settings in Django, uwsgi, nginx

see [Tutorial](), it is in Chinese, but you can find similar tutorial in English easily. I will post points i think that are worthy of your attention. 

- your nginx doesn't work might because you are using a SElinux, and there are some things I don't know why. I found some answers to this might help you with this if your nginx doesn't work. [13: Permission Denied](https://www.digitalocean.com/community/questions/403-forbidden-nginx-13-permission-denied)  [Nginx Error](https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx)
- you might have other nginx permission error. Open your nginx.conf (you must be familiar with this file if you tried hard to fix bugs), find 'user nobody' or something like that. You might want to change it to 'user root' or 'user admin'. Use ``` ps -aux``` to find out which group is running nginx service
- The STATIC_ROOT setting might have a typo in the tutorial. By reading the error_log you can easily know where is wrong. By the way find out where is your error_log in your nginx.conf
- You might want to use ``` sudo tail -f error_log``` to monitor you website
- You might want to restart the nginx.service, but i ask you to enter a password you never set. My solution is change that user(usually centos) password since you already have the root permission.

#### use git to manage your workflow







## Drafts

#### How to configure local settings after cloning pycharm project from github?

1. configure your virtual environment
2. runserver and get to your administration site
3. if you use pycharm virtual env, you should run cmd in pycharm terminal


#### How to add components to django blog?


##### URLS

- direct URL :
in the main url.py, assign an url pattern to the absolute location in the project using a string, for example
``` python
urlpatterns = {
    url('admin/',admin.site.urls),
    url('posts/',"posts.views.post_home")
    # in a pattern <appname>.views.<function>
    
    # why we must use string rather than the first row representation?
    #
    
}
```

- using an indirect/hierarchy  URL (in app url)


- regular expression practice


#### Response and Render in view

- get objects in Database.
- put them to dictionaries to be applied to templates
#### Why changes on source code didn't apply?
because the django didn't recognize the source code, and act to some other thing it is used. So we


##### Models 
Model in django can be viewed as a database table, only that it can be easily accessed by both view and controller(this convenience is provided by django, that's what django does).

##### Views 
View is like the controller in MVC design patterns. In view


##### Admin sites
In your subdirectory, create an admin.py and register according to the template admin.site

##### Deploy to remote server

first we need to check re github repo structure, in case we contained something we didn' need at all, this requires us to add .git ignore to the github repo.


#### Deploy
- create a DigitalOcean Droplet with pub-key in .ssh/ folder
- Download putty to get ssh access to it
- in putty, configure the ssh->auth->private key file of your .ssh/ folder private key
- save the session in putty, name it anything you want
- make sure the django project setting is converted to release mode

  - TODO : configure database, port, security, OS dependencies and things like that.
- configure the dependencies.
  - Manually Configure
    - install python3.6 in CentOS and corresponding packages including django
    - install git
    - install apache or nginx
    - install mysql
  - Run Build Scripts : TODO 

#### add user : admin passwd : 990513

first thing : add your ssh pub key to ~/.ssh/authorized_keys

add 3 inspector : affe_window1 ~ affe_window3 pwd : 990513

[configure ssh](https://www.linpx.com/p/configure-the-ssh-key-on-centos.html)

``` shell
adduser admin
passwd admin ## password

# give chmod
cd /etc
chmod -v u+w /etc/sudoers
emacs sudoers
# add a line at ## Allow root to run any commands anywhere
# admin  ALL=(ALL)    ALL ## not sure about the space matter or not
# then change mod
chmod -v u-w /etc/sudoers
# code from the following link
```

[sudo permission](https://www.cnblogs.com/woshimrf/p/centos-new-user.html)

``` shell
## change ssh config
```

[ssh permission](https://wiki.centos.org/HowTos/Network/SecuringSSH)

add 2 ssh pub key to the ./ssh authen file

do as the SXY tutorial [TUTORIAL](https://blog.csdn.net/eightbrother888/article/details/79503716)

change the SElinux network root

[stackoverflow solution](https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx)



- about STATIC_ROOT & STATIC_URL



need to change user:centos password to start the nginx service.

and the SElinux other settings (prevent something) [13 :permission denied solution](https://www.digitalocean.com/community/questions/403-forbidden-nginx-13-permission-denied)

django adminsite : affe  pwd:990513

#### passwords:

django admin :   affe 990513