def format_partition_item(item: dict) -> dict:
    """
    Formats specific values.
    """
    formatted_item = {
        "partition_key": item["partition_key"],
        "name": str(item.get("name", "")).strip(),
        "age": str(item.get("age")) if "age" in item else None,
        "purchase": item.get("purchase"),
    }

    return formatted_item
