from datetime import datetime, timedelta
import json
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/calendar']

# Authenticate and get Google Calendar API Scope
def get_calendar_service():
    flow = InstalledAppFlow.from_client_secrets_file('client_secret_974962523933-p6l20ljd1qupb3kvb5mjvhnbp0fd377p.apps.googleusercontent.com.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('calendar', 'v3', credentials=creds)

# Define the learning roadmap tasks
roadmap = [("Learn SQL Basics", 1),
           ("Master python for data", 1),
           ("Work with APIs & web scripting", 1),
           ("Build a simple ETL Pipeline", 1),
           ("Deep dive into databases", 2),
           ("Learn NoSQL (MongoDB, Cassandra)", 2),
           ("Explore cloud data Warehouse", 2),
           ("Hands-on data warehouse project", 2),
           ("Learn Apache Spark", 3),
           ("Explore Hadoop Basics", 3),
           ("Hands-on: Spark Data Processing", 3),
           ("Learn Apache Airflow", 4),
           ("Work with Apache Kafka", 4),
           ("Build a Batch & Streaming Pipeline", 4),
           ("Learn AWS (S3, Glue, Redshift)", 5),
           ("Learn Terraform for Infrastructure", 5),
           ("Deploy Data Pipeline on Cloud", 5),
           ("CI/CD for Data Pipelines", 6),
           ("Docker & Kubernetes for Data", 6),
           ("Build End-to-End Data Project", 6)]

# Set start date 
start_date = datetime.today()

# Create events 
def add_events_to_calendar():
    service = get_calendar_service()
    calendar_id = 'primary'

    for task, month in roadmap:
        event_date = start_date + timedelta(weeks=(month - 1) * 4)
        event = {
            'summary': task,
            'start': {'date': event_date.strftime('%Y-%m-%d')},
            'end': {'date': event_date.strftime('%Y-%m-%d')}
        }
        service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f"Event created: {task} on {event_date.strftime('%Y-%m-%d')}")

add_events_to_calendar()        