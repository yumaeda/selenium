# Selenium用のPythonモジュール

### 必要なモジュールをインストールする。 
```bash
pip install invoke
pip install pylint
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
