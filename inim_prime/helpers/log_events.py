from typing import List

from inim_prime.models import LogEvent

def filter_new_log_events(last_log_events: List[LogEvent], current_log_events: List[LogEvent]) -> List[LogEvent]:
    """
    Given two lists of LogEvent (old → new), return only events in current_log_events
    that are not repeated from last_log_events. Comparison ignores the `id` field.
    """
    def event_key(log_event: LogEvent):
        return (
            log_event.timestamp,
            log_event.type,
            log_event.agent,
            log_event.location,
            log_event.value,
        )

    last_keys = [event_key(e) for e in last_log_events]
    current_keys = [event_key(e) for e in current_log_events]

    n_last = len(last_keys)
    n_curr = len(current_keys)

    if n_last == 0:
        return current_log_events

    # Find how many events at the start of current are already at the end of last
    overlap_index = 0
    for i in range(min(n_last, n_curr)):
        if last_keys[-(i + 1):] == current_keys[:i + 1]:
            overlap_index = i + 1

    return current_log_events[overlap_index:]