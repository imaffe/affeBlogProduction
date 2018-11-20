# YOU MIGHT NEED TO CHANGE THE PERMISSION OF THIS FILE!
# build dependencies on an CentOS virtual machine
# install dependencies
sudo yum groupinstall "Development tools"
sudo yum install openssl openssl-devel sqlite-devel zlib-develbzip2-devel
sudo yum install pcre pcre-devel pcre-static
sudo yum install zlib-devel bzip2-devel ncurses-devel sqlite-devel readline-devel tk-devel
sudo yum install gcc make
# install python 3.6
sudo yum install epel-release
sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum install python36u
# change python symblo to python3 link
sudo ln -s /bin/python3.6 /bin/python3

# install pip3
sudo yum install python36u-pip
# rename pip3
sudo ln -s /bin/pip3.6 /bin/pip3

# install python failed because
# install emacs editor for me
sudo yum install emacs

sudo pip3 install uwsgi
