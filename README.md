# End-to-End MLOps Pipeline

This project demonstrates a complete **MLOps workflow** using:

* Docker
* CI/CD (GitHub Actions)
* Kubernetes (Next Step)
* Helm (Next Step)

--- 

## Project Overview

A simple Flask-based ML application that is:

* Containerized using Docker
* Tested using Pytest
* Automated using CI pipeline
* Pushed to DockerHub for deployment

---

## Project Structure 

```
├── app
│ ├── index.html
│ └── main.py
├── docker
│ └── Dockerfile
├── tests
│ └── test_home.py
├── .github/workflows
│ └── ci.yml
├── requirements.txt
└── README.md

``` 
---

## Tech Stack

* Python (Flask)
* Docker
* GitHub Actions (CI)
* Pytest

--- 

## Run Locally 

### Clone Repo

```bash
git clone https://github.com/<your-username>/end-to-end-mlops-pipeline.git
cd end-to-end-mlops-pipeline
```
---

### Install Dependencies

```bash
pip install -r requirements.txt
```
---
