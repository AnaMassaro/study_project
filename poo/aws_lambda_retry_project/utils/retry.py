import time
from functools import wraps


def retry(attempts: int = 3, delay: float = 1.0, exception_types: tuple = (Exception,)):
    """
    Decorator to retry a function if an exception occurs.

    Parameters:
    - attempts: max retry attempts (default: 3)
    - delay: delay between attempts in seconds (default: 1.0)
    - exception_types: tuple of exception classes to catch (default: all Exception)
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exception_types as e:
                    if attempt == attempts:
                        print(f"[RETRY] ❌ Tentativa {attempt}/{attempts} falhou: {e}")
                        raise
                    else:
                        print(
                            f"[RETRY] ⚠️ Tentativa {attempt}/{attempts} falhou: {e}. Tentando novamente em {delay}s..."
                        )
                        time.sleep(delay)

        return wrapper

    return decorator
