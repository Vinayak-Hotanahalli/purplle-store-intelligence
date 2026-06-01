from app.database import events_db

def save_event(event):
    events_db.append(event)