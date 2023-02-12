#### Establishing connection with EC2 using  GIT BASH FROM LOCAL MACHINE

1.ssh -i Downloads/<key-pair.pem>{OS}@Public IPv4 address
2.sudo -su (switching to root user)

#### Installing Docker and Docker-compose on EC2 Instance

###### 1.yum install docker -y
###### 2.curl -SL https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
###### 3.sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

#### Confluent on Docker

###### 1.mkdir docker-compose.yml
###### 2.
