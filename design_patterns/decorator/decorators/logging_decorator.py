from functools import wraps
from typing import Callable, Any

def logging_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[LOG] Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}'.")
        return result
    return wrapper