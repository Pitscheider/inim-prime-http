from datetime import datetime, timedelta
from typing import List
from dataclasses import dataclass
from itertools import count

from inim_prime.helpers.log_events import filter_new_log_events
from inim_prime.models import LogEvent

# Assuming LogEvent class is already defined above
# Assuming filter_new_log_events is the corrected version

# Generator for unique IDs
id_gen = count(1)

def make_event(timestamp, type, agent=None, location=None, value=None):
    return LogEvent(next(id_gen), timestamp, type, agent, location, value)

def print_events(events: List[LogEvent], title="Events"):
    print(f"\n{title} ({len(events)}):")
    for e in events:
        print(f"  {e}")

# Base timestamp
base_time = datetime(2026, 1, 13, 12, 0, 0)

# Test scenarios
scenarios = []

# 1. No previous events → everything is new
scenarios.append(("No previous events", [], [
    make_event(base_time, "A"),
    make_event(base_time + timedelta(seconds=1), "B"),
]))

# 2. No new events → result is empty
scenarios.append(("No new events", [
    make_event(base_time, "A")
], []))

# 3. Partial overlap at start
last = [
    make_event(base_time, "A"),
    make_event(base_time + timedelta(seconds=1), "B"),
]
current = [
    make_event(base_time + timedelta(seconds=1), "B"),  # overlapping
    make_event(base_time + timedelta(seconds=2), "C"),  # new
]
scenarios.append(("Partial overlap", last, current))

# 4. Complete overlap → result empty
last = [
    make_event(base_time, "A"),
    make_event(base_time + timedelta(seconds=1), "B"),
]
current = [
    make_event(base_time, "A"),
    make_event(base_time + timedelta(seconds=1), "B"),
]
scenarios.append(("Complete overlap", last, current))

# 5. Overlap with different length current > last
last = [
    make_event(base_time, "A"),
]
current = [
    make_event(base_time, "A"),  # overlapping
    make_event(base_time + timedelta(seconds=1), "B"),  # new
    make_event(base_time + timedelta(seconds=2), "C"),  # new
]
scenarios.append(("Current longer than last", last, current))

# 6. Overlap with different length last > current
last = [
    make_event(base_time, "A"),
    make_event(base_time + timedelta(seconds=1), "B"),
    make_event(base_time + timedelta(seconds=2), "C"),
]
current = [
    make_event(base_time + timedelta(seconds=1), "B"),
    make_event(base_time + timedelta(seconds=2), "C"),
]
scenarios.append(("Last longer than current", last, current))

# 7. No overlap → everything new
last = [
    make_event(base_time, "X"),
]
current = [
    make_event(base_time + timedelta(seconds=10), "Y"),
    make_event(base_time + timedelta(seconds=20), "Z"),
]
scenarios.append(("No overlap", last, current))

# 8.
last = [
    make_event(base_time, "A"),
]
current = [
    make_event(base_time, "A"),
    make_event(base_time, "A"),
    make_event(base_time, "B"),
    make_event(base_time, "A"),
]
scenarios.append(("Last longer than current", last, current))

# Run tests
for title, last_events, current_events in scenarios:
    print(f"\n=== Scenario: {title} ===")
    print_events(last_events, "Last events")
    print_events(current_events, "Current events")
    filtered = filter_new_log_events(last_events, current_events)
    print_events(filtered, "Filtered new events")
