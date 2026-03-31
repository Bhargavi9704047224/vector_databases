import chromadb

# Create client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="vehicles")
print("Collection created:", collection.name)

# Add data
collection.add(
    documents=[
        "car runs on land",
        "plane flies in sky",
        "boat travels on water",
        "bus is public transport on road"
    ],
    ids=["car1", "plane1", "boat1", "bus1"]
)

# Query
results = collection.query(
    query_texts=["vehicle that run on road"],
    n_results=2
)
# Print output
print(results)