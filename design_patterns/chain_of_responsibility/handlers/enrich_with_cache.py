from core.chain import Handler

class EnrichWithCacheHandler(Handler):
    def __init__(self, cache_service):
        super().__init__()
        self.cache_service = cache_service

    def handle(self, data):
        print("Enriching data from cache...")

        category_id = data.get('category_id')
        if category_id:
            category_name = self.cache_service.get_category_name(category_id)
            if category_name:
                data['category_name'] = category_name
            else:
                data['category_name'] = 'Unknown'

        if self._next_handler:
            return self._next_handler.handle(data)
        return data
                