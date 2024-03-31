from azure.eventhub import EventHubProducerClient, EventData

connection_str = "xxxxxx"
event_hub_name = "xxxxxxx"

# Create an EventHubProducerClient instance
producer_client = EventHubProducerClient.from_connection_string(connection_str, event_hub_name=event_hub_name)

# Create a list of events to send
events = [
    {"id": 3, "message": "Event 3"},
    {"id": 4, "message": "Event 4"}
]

try:
    # Create a batch object
    with producer_client:
        # Create a batch
        event_data_batch = producer_client.create_batch()

        # Add events to the batch
        for event in events:
            event_data = EventData(body=str(event))
            event_data_batch.add(event_data)

        # Send the batch of events
        producer_client.send_batch(event_data_batch)

    print("Events sent successfully.")
except Exception as e:
    print("Error occurred:", e)
finally:
    # Close the producer client
    producer_client.close()
