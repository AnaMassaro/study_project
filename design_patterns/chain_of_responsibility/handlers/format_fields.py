from core.chain import Handler

class FormatFieldsHandler(Handler):
    def handle(self, data):
        print("Formatting fields...")
        
        if 'name' in data and isinstance(data['name'], str):
            data['name'] = data['name'].strip().title()

        if 'date' in data and isinstance(data['date'], str):
            parts = data['date'].split('/')
            if len(parts) == 3:
                data['date'] = f"{parts[2]}-{parts[1]}-{parts[0]}"

        if 'amount' in data:
            raw = str(data['amount'])
            cleaned = ''.join(c for c in raw if c.isdigit() or c == '.')
            try:
                data['amount'] = float(cleaned)
            except ValueError:
                data['amount'] = 0.0

        if self._next_handler:
            return self._next_handler.handle(data)
        return data