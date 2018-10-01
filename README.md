# Repository for Python Modules

### Clone yumaeda-python repository.
```bash
git clone https://github.com/yumaeda/selenium.git $HOME/selenium
```

### Install Packages.
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

### Execute Task Runner.
```bash
cd $HOME/selenium
invoke clean build
```

# Docker

### Launch Docker Container.
```bash
cd $HOME/selenium
docker-compose up -d --build
```

### Execute demo.py under `$HOME/selenium`.
```bash
docker exec -it python python /root/script/demo.py
```
