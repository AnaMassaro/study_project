class CacheService:
    def __init__(self):
        self.category_cache = {
            '001': 'Electronics',
            '002': 'Books',
            '003': 'Clothing'
        }

    def get_category_name(self, category_id):
        return self.category_cache.get(category_id)
