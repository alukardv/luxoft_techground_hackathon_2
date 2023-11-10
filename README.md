# luxoft_techground_hackathon_2
## Setup
### Install pyenv
#### Link for pyenv
```
https://github.com/pyenv/pyenv
```
#### Install python 3.12 version
```bash
pyenv install 3.12
```
### Install poetry
#### Link for poetry
```
https://python-poetry.org/docs/#installation
```
### Create project with poetry
```bash
git clone git@github.com:alukardv/luxoft_techground_hackathon_2.git
cd luxoft_techground_hackathon_2
```
#### Create virtual environments
```bash
pyenv local 3.12
```
#### Install requirements
```bash
poetry install
```
### Create project with venv
```bash
git clone git@github.com:alukardv/luxoft_techground_hackathon_2.git
cd luxoft_techground_hackathon_2
```
#### Create virtual environments
```bash
pyenv local 3.12
```
#### Create virtual environments and activate
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Install requirements
```bash
pip3 install -r requirements.txt
```


### Load initial data
```bash
./manage.py loaddata initial_data/map.json
./manage.py load_initial_cities initial_data/cities.txt
```