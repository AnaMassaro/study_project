from handlers.format_fields import FormatFieldsHandler
from handlers.validate_fields import ValidateFieldsHandler
from handlers.enrich_with_cache import EnrichWithCacheHandler
from handlers.send_to_sqs import SendToSQSHandler

class ChainBuilder:
    def __init__(self, sqs_service, cache_service):
        self.sqs_service = sqs_service
        self.cache_service = cache_service

    def build_chain(self, data):
        """
        Monta a cadeia de handlers dependendo do tipo de dado.
        Por exemplo:
        - Se data['type'] == 'full', executa toda a cadeia.
        - Se data['type'] == 'minimal', pula o handler de enriquecimento.
        - Se data['type'] == 'simple', executa só formatar e enviar.
        """
        
        data_type = data.get('type', 'full')

        format_handler = FormatFieldsHandler()
        validate_handler = ValidateFieldsHandler()
        enrich_handler = EnrichWithCacheHandler(self.cache_service)
        send_handler = SendToSQSHandler(self.sqs_service)

        # Monta a cadeia com base no tipo
        if data_type == 'full':
            # Cadeia completa
            format_handler.set_next(validate_handler)\
                          .set_next(enrich_handler)\
                          .set_next(send_handler)
            return format_handler

        elif data_type == 'minimal':
            # Sem enriquecimento
            format_handler.set_next(validate_handler)\
                          .set_next(send_handler)
            return format_handler

        elif data_type == 'simple':
            # Só formatar e enviar
            format_handler.set_next(send_handler)
            return format_handler

        else:
            # Padrão: toda cadeia
            format_handler.set_next(validate_handler)\
                          .set_next(enrich_handler)\
                          .set_next(send_handler)
            
            return format_handler