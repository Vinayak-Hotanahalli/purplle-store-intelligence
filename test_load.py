from app.load_events import load_events

events = load_events()

print(f"Loaded {len(events)} events")

for event in events:
    print(event)