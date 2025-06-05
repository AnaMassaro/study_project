# chain_builder.py

from handlers.format_fields import FormatFieldsHandler
from handlers.validate_fields import ValidateFieldsHandler
from handlers.enrich_with_cache import EnrichWithCacheHandler
from handlers.send_to_sqs import SendToSQSHandler

from services.cache_service import CacheService
from services.sqs_service import SqsService


def build_handler_chain():
    cache_service = CacheService()
    sqs_service = SqsService(queue_name="my-queue-name")

    format_handler = FormatFieldsHandler()
    validate_handler = ValidateFieldsHandler()
    enrich_handler = EnrichWithCacheHandler(cache_service)
    send_handler = SendToSQSHandler(sqs_service)

    # Montar a cadeia
    format_handler.set_next(validate_handler)
    validate_handler.set_next(enrich_handler)
    enrich_handler.set_next(send_handler)

    return format_handler
