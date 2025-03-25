***Guide:***

On the machine on which you want the backend to be run (does not have to be same machine as the one running the vLLM service)

*Either:*

1. install dependencies with `pip install -r requirements.txt`

2. deploy without docker with `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

*Or*:

1. create a docker image with `docker build -t fastapi-backend .`

2. start a docker container with `docker run -p 8000:8000 fastapi-backend`