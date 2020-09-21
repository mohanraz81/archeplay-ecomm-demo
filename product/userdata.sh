#!/bin/bash
yum -y install git
git clone https://github.com/mohanraz81/archeplay-ecomm-demo.git
awsregion=us-east-1
tablename=mytable
cd archeplay-ecomm-demo/product
sed -i "s/REGIONNAME/$awsregion/g" docker-compose.yaml
sed -i "s/TABLENAME/$tablename/g" docker-compose.yaml
sh -x ./startup.sh