# Test for EWT Event
# Author : Cindy Wang
# Date : 2024/06/10

import logging
import time

# Set logger
logging.basicConfig(level=logging.INFO)

# Define test EWT name
etw_provider_name = "MyTestProvider001"

def init_etw_provider():
    try:
        import win32evtlogutil
        win32evtlogutil.AddSourceToRegistry(etw_provider_name, "Application")
        logging.info(f"ETW provider '{etw_provider_name}' initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing ETW provider: {e}")

# Trigger ETW Event
def trigger_etw_event():
    try:
        import win32evtlogutil
        win32evtlogutil.ReportEvent(etw_provider_name, 1, eventType=1, strings=["ETW Event Triggered"])
        logging.info("ETW event triggered successfully.")
    except Exception as e:
        logging.error(f"Error triggering ETW event: {e}")

if __name__ == "__main__":
    init_etw_provider()
    while True:
        trigger_etw_event()
        time.sleep(5) 
