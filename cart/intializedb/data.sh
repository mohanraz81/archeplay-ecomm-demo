#!/bin/bash
set -ex
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -h cart-db $MYSQL_DATABASE <<EOF
CREATE TABLE carttable ( id INT(11) AUTO_INCREMENT PRIMARY KEY, user VARCHAR(32) NOT NULL, productid VARCHAR(32));
EOF