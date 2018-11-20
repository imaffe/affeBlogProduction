## Manual For AffeBlog Deployment

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





do as the SXY tutorial

change the SElinux network root

[stackoverflow solution](https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx)

#### install python3.6
