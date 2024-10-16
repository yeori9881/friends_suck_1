import datetime
import pandas as pd

class Planner:
    def __init__(self):
        self.schedule = []

    def add_event(self, date, time, event):
        date_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        self.schedule.append({"Date and Time": date_time, "Event": event})
        print(f"Event '{event}' added on {date} at {time}.")

    def view_events(self):
        if not self.schedule:
            print("No events scheduled.")
            return
        df = pd.DataFrame(self.schedule)
        df = df.sort_values(by="Date and Time")
        print(df.to_string(index=False))

    def view_events_by_date(self, date):
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        events_on_date = [event for event in self.schedule if event["Date and Time"].date() == date_obj]

        if not events_on_date:
            print(f"No events scheduled on {date}.")
            return

        df = pd.DataFrame(events_on_date)
        df = df.sort_values(by="Date and Time")
        print(df.to_string(index=False))


planner = Planner()

while True:
    print("\nMenu:")
    print("1. Add Event")
    print("2. View All Events")
    print("3. View Events by Date")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        time = input("Enter the time (HH:MM): ")
        event = input("Enter the event description: ")
        planner.add_event(date, time, event)
    elif choice == "2":
        planner.view_events()
    elif choice == "3":
        date = input("Enter the date (YYYY-MM-DD) to view events: ")
        planner.view_events_by_date(date)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        
