# Streamlit + Traefik + Docker
This simple project uses Traefik as a reverse proxy to a Streamlit application and handles SSL certs with Lets Encrypt.

## Requirements
- Docker Compose
- Python 3.9

## Local Deployment
#### Python:
1. `cd src`  
2. `pip install -r requirements.txt`  
3. `streamlit run app.py`  

#### Docker:
1. `sudo docker-compose -f local.yml up --build`  

## Production Deployment
1. In `compose/traefik/traefik.yml`, change `example@test.com` to your email. 
2. In `compose/traefik/traefik.yml`, change `example.com` to your domain.
3. `sudo docker-compose -f production.yml up --build`

### Notes:
Feel free to make a PR or get in contact with me on Discord at yoyojoe#5510.
