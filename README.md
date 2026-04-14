# Churn Prediction ML API

## Overview
This project demonstrates an end-to-end ML deployment pipeline with CI/CD on Azure.

It focuses on:
- FastAPI for serving predictions
- Docker for containerization
- GitHub Actions for CI/CD
- Azure Container Apps for deployment

## Live Demo
https://churn-ml-api.purplecoast-442677a6.eastus.azurecontainerapps.io/docs

## API Endpoints

### Health Check
`GET /`

Response:
```json
{"message": "Churn API is running"}

Prediction

POST /predict

Example request:

{
  "tenure": 12,
  "monthly_charges": 70,
  "total_charges": 840
}

Example response:
{
  "churn_prediction": 0,
  "score": 5.38
}
