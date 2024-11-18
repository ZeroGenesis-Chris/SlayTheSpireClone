import random

class EventManager:
    def __init__(self, player, enemy, events=[]):
        """
        Initializes the EventManager with a player, enemy, and a list of possible events.
        """
        self.player = player
        self.enemy = enemy
        self.events = events  # List of possible events to be triggered

    def add_event(self, event):
        """
        Adds a new event to the event list.
        """
        self.events.append(event)
        print(f"Event '{event.__class__.__name__}' added to the event list.")

    def trigger_random_event(self):
        """
        Randomly triggers an event from the event list.
        """
        if not self.events:
            print("No events available to trigger.")
            return

        event = random.choice(self.events)
        print(f"Triggering event: {event.__class__.__name__}")
        event.execute(self.player, self.enemy)

    def trigger_event(self, event):
        """
        Manually trigger a specific event from the event list.
        """
        if event not in self.events:
            print(f"Event {event.__class__.__name__} not found.")
            return

        print(f"Manually triggering event: {event.__class__.__name__}")
        event.execute(self.player, self.enemy)
