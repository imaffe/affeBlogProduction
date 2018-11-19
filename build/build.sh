# build dependencies on an CentOS virtual machine

# install dependencies
sudo yum groupinstall "Development tools"
sudo yum install openssl openssl-devel sqlite-devel zlib-develbzip2-devel
sudo yum install pcre pcre-devel pcre-static

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
