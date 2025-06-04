import functools
import datetime
#import traceback

def log(filename=None):
    """
    Декоратор логирования выполнения функции.

    Если filename задан, логи пишутся в файл, иначе — в консоль.

    Логируются:
     - Имя функции и результат при успешном выполнении
     - Имя функции, тип ошибки и параметры при исключении
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            params = ", ".join(args_repr + kwargs_repr)

            def write_log(message):
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                final_msg = f"[{timestamp}] {message}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        print(final_msg, file=f)
                else:
                    print(final_msg)

            try:
                result = func(*args, **kwargs)
                write_log(f"Функция '{func_name}' успешно выполнена. Результат: {result!r}")
                return result
            except Exception as ex:
                exc_type = type(ex).__name__
                write_log(f"Функция '{func_name}' вызвала ошибку '{exc_type}'. Параметры: {params}")
                raise

        return wrapper
    return decorator
