# luxoft_techground_hackathon_2
## setup
```bash
pyenv local 3.12
poetry install
```

### Load initial data
```bash
./manage.py loaddata initial_data/map.json
./manage.py load_initial_cities initial_data/cities.txt
```
