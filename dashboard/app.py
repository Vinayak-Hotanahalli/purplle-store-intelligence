import streamlit as st
import pandas as pd
import json

EVENTS_FILE = "outputs/events.jsonl"

events = []

try:

    with open(
        EVENTS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()

            if line:

                try:

                    events.append(
                        json.loads(line)
                    )

                except:
                    pass

except FileNotFoundError:

    st.error(
        "events.jsonl not found"
    )

df = pd.DataFrame(events)

st.title(
    "Purplle Store Intelligence Dashboard"
)

if len(df) == 0:

    st.warning(
        "No events found"
    )

else:

    unique_visitors = df[
        "visitor_id"
    ].nunique()

    entries = len(
        df[
            df["event_type"]
            == "ENTRY"
        ]
    )

    exits = len(
        df[
            df["event_type"]
            == "EXIT"
        ]
    )

    dwell_events = len(
        df[
            df["event_type"]
            == "ZONE_DWELL"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Visitors",
            unique_visitors
        )

        st.metric(
            "Entries",
            entries
        )

    with col2:

        st.metric(
            "Exits",
            exits
        )

        st.metric(
            "Dwell Events",
            dwell_events
        )

    st.subheader(
        "Raw Events"
    )

    st.dataframe(df)