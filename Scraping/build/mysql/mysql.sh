#!/bin/bash

# コンテナに入る → コンテナ内のmysql接続
docker exec -it Scraping.mysql bash -c "mysql -u root -p"
