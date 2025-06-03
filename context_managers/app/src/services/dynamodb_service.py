import random
import time

def simulate_dynamodb_put_item(item: dict):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate network delay

    if random.choice([True, False]): # Randomiza sucesso/erro
        raise Exception("Simulated DynamoDB error")
    
    return {"status": "success", "item_id": item.get("id")}
