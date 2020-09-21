#!/bin/bash
yum -y install git
git clone https://github.com/mohanraz81/archeplay-ecomm-demo.git
awsregion=us-east-1
tablename=producttable
cd archeplay-ecomm-demo/product
sed -i "s/REGIONNAME/$awsregion/g" docker-compose.yaml
sed -i "s/TABLENAME/$tablename/g" docker-compose.yaml
cp product.service /etc/systemd/system/product.service
systemctl daemon-reload
systemctl enable product.service
systemctl start product.service