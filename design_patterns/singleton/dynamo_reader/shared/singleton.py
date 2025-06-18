from threading import Lock


class SingletonMeta(type):
    """
    Metaclass that ensures a class has only one instance (Singleton Pattern).
    Any class using this metaclass will only be instantiated once.
    """

    # Dicionário que armazena as instâncias únicas de cada classe que usa essa metaclasse
    _instances = {}

    # Lock garante que o acesso ao _instances seja thread-safe (seguro em ambientes concorrentes)
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Quando você chama a classe (ex: MyClass()), esse método é executado.
        Garante que a instância seja única mesmo se várias threads chamarem ao mesmo tempo.
        """

        # Trava a execução: só uma thread por vez pode entrar nesse bloco
        with cls._lock:
            # Se ainda não existe instância dessa classe, criamos e armazenamos
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        # Sempre retorna a mesma instância criada anteriormente
        return cls._instances[cls]
