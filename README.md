# End-To-End-Book-Recommender-System

An End-To-End E-Commerce Book RecommenderSystem Using Machine Learning Algorithms, Dockerizing The Entire Project and Push To Docker Hub, Applyijg CI/CD Pipelines Using Github Action On AWS

## How to run?

### STEPS ->

#### STEP 01. Clone the repository

```bash
git clone git@github.com:ShwaTech/End-To-End-Book-Recommender-System.git
```

#### STEP 02. Create a conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```

#### STEP 03. install the requirements

```bash
pip install -r requirements.txt
```

#### Project Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py

### Run Streamlit App ->

```bash
streamlit run app.py
```

## Streamlit app Docker Image Deployment

### 1. Login with your AWS console and launch an EC2 instance

### 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone https://github.com/ShwaTech/End-To-End-Book-Recommender-System.git
```

```bash
docker build -t shwacode/stapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 shwacode/stapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push shwacode/stapp:latest 
```

```bash
docker rmi shwacode/stapp:latest
```

```bash
docker pull shwacode/stapp
```
