## Deploying a model as a web-service
    
### terminal 1

* virtual environment with Pipenv
    step 1: `pip install pipenv`

    step 2: venv `pipenv install`

    step 3: `pipenv install -r requirements.txt or --dev [package]`

    step 4: run `pipenv shell`


## Create script to download production model
```bash
python download_model.py
```

## creating scripts to predict and send request for Flask app
```bash
python predict.py
```
### terminal 2
```bash
python test
```

## Docker
* build
```bash
docker build -t credit-risk:v1 .
```
* run
docker run -it --rm -p 9696:9696 credit-risk:v1

    pass local file to test