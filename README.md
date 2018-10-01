# Repository for Python Modules

### Clone yumaeda-python repository.
```bash
git clone https://github.com/yumaeda/yumaeda-python.git $HOME/yumaeda-python
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
cd $HOME/yumaeda-python
invoke clean build
```

# Docker

### Launch Docker Container.
```bash
cd $HOME/yumaeda-python
docker-compose up -d --build
```

### Execute demo.py under `$HOME/yumaeda-python`.
```bash
docker exec -it python python /root/script/demo.py
```
