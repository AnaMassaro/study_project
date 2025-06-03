from src.utils.logger import get_logger

import time

logger = get_logger(__name__)

class ExecutionTimer:
    def __init__(self, operation_name: str):
        self.operation_name = operation_name

    def __enter__(self):
        self.start_time = time.time()
        logger.info(f'[START] {self.operation_name}')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        logger.info(f"[END] {self.operation_name} | Duration: {duration:.2f}s")
        if exc_type:
            logger.error(f"[ERROR] {self.operation_name} failed: {exc_val}")
            
        return False # Não suprime exceções (deixa elas acontecerem normalmente)