# Selenium用のPythonモジュール

### 必要なモジュールをインストールする。 
```bash
brew update
brew install python
sudo easy_install pip
sudo easy_install six
sudo pip install --user matplotlib
sudo pip install --user selenium
sudo pip install --user invoke
sudo pip install --user pylint
```

### Task Runnerを実行する。
```bash
invoke clean build
```

# Docker

### Selenium & Python & ChromeのDockerコンテナを起動する。
```bash
docker-compose up -d --build
```

### `$HOME/selenium` 直下のdemo.pyを実行する。
```bash
docker exec -it python python /root/script/demo.py
```
