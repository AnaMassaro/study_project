from core.chain import Handler

class ValidateFieldsHandler(Handler):
    def handle(self, data):
        print("Validating fields...")

        required_fields = ['name', 'date', 'amount']

        for field in required_fields:
            if field not in data or data[field] in [None, '', 0]:
                raise ValueError(f"Validation failed: '{field}' is missing or invalid.")
            
        if self._next_handler:
            return self._next_handler.handle(data)
        return data