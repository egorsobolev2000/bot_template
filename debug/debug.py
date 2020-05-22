import time

from .color import ColorsPrint


def timeit(f):
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print(f'Время выполнения {ColorsPrint(f.__name__, "inf").do_colored()} — ',
              ColorsPrint(str(delta_time), 'att').do_colored())
        return result

    return tmp


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(ColorsPrint(f'Возникла ошибка в функции '
                              f'{ColorsPrint(f.__name__, "inf").do_colored()}', 'err').do_colored(), e)
            raise e

    return inner
