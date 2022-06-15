gcloud builds submit --tag gcr.io/streamlit-app3/Streamlit-App3  --project=streamlit-app3

gcloud run deploy --image gcr.io/streamlit-app3/Streamlit-App3 --platform managed  --project=streamlit-app3 --allow-unauthenticated

