import logging
import datetime
import pytz
from functools import wraps


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.datetime.fromtimestamp(record.created, tz=pytz.timezone("America/Sao_Paulo"))

        if datefmt:
            return dt.strftime(datefmt)
        else:
            return dt.isoformat()


class AppLogger(logging.Logger):
    """Classe personalizada de logger pra operações na camada de serviço dentro do contexto da API.

    Args:
        name (str): O nome do logger.
        level (Union[int, str], optional): O nível de log. O padrão é logging.NOTSET.
    """

    def __init__(self, name: str, level: int | str = logging.NOTSET) -> None:
        super().__init__(name, level)

        handler = logging.StreamHandler()
        handler.setLevel(level)
        formatter = CustomFormatter(fmt="%(asctime)s : %(levelname)s : %(message)s",
                                    datefmt="%Y-%m-%d %H:%M:%S")
        
        handler.setFormatter(formatter)
        self.addHandler(handler)


class LogService:
    __loggers = {}

    def get_logger(self, name: str):
        """Recupera ou cria um logger para a aplicação com um nome especifico

        Args:
            name (str): O nome do logger a ser recuperado/criado.
        
        Returns:
            AppLogger (logging.Logger): A instância do logger associada ao nome fornecido.
        """

        if name not in self.__loggers:
            logger = AppLogger(name)
            logger.setLevel(logging.INFO)
            self.__loggers[name] = logger
        return self.__loggers[name]


def handle_exceptions(logger):
    """Decorador para logar exceções e capturar erros inesperados que afetam execução conclusão da operação na camada de serviço."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                exception_type = error.__class__.__name__
                logger.critical("Erro Inesperado em %s: %s",
                                func.__name__,
                                exception_type,
                                exc_info=error)
                return ("UnexpectedError", f"{exception_type}: {error}")
        return wrapper
    return decorator