from typing import List

import faust

from faustify.app import faustify_app


class TrackEvent(faust.Record):
    category: str
    action: str
    label: str
    value: str
    nodeid: str


topic_track_event = faustify_app.topic('faustify-user-events', value_type=TrackEvent)


@faustify_app.agent(topic_track_event)
async def process_track_events(events):
    async for event in events:
        print(f'Hello from {event.category} to {event.action}')


@faustify_app.timer(interval=1.0)
async def auto_send_track_event():
    await process_track_events.send(
        value=TrackEvent(
            category="category",
            action="action",
            label="label",
            value="value",
            nodeid="nodeid",
        ),
    )
