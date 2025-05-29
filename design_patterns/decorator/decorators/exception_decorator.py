from functools import wraps
from typing import Callable, Any

def exception_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] An exception occurred in '{func.__name__}': {e}")
            return None
    return wrapper