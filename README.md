# Selenium用のPythonモジュール

### srcディレクトリのパイソンのソースをコンパイルする。 
```bash
python -m src/compileall .
```

### Selenium & Python & ChromeのDockerコンテナを起動する。
```bash
docker-compose up -d --build
```

```bash
### `$HOME/selenium` 直下のdemo.pyを実行する。
docker exec -it python python /root/script/demo.py
```
