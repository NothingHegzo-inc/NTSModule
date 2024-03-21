import time, logging, sys, os
from typing import Callable, Any, overload
from functools import wraps

# class LOGGING:
#     @overload
#     def __init__(function: Callable[..., Any]) -> Callable[..., Any]: ...
#     @overload
#     def __init__(function: Callable[...,Any], logger: logging.Logger) -> Callable[...,Any]: ...
#     def __init__(self, logger: logging.Logger = logging.getLogger()) -> None:
#         def decorator(function: Callable[..., Any]) -> None:
#             self.function = function
#             self.logger = logger
#         return decorator
    
#     def loggingF(self, function: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(function)
#         def wrapper(*args, **kwargs) -> Any:
#             self.logger.debug(f"Calling function '{function.__name__}'")
#             returnValue = function(*args, **kwargs)
#             self.logger.debug(f"'{function.__name__}' function was called with a return value '{returnValue}'.")
#             self.logger.debug(f"Finished calling function '{function.__name__}'.")
#             return returnValue
#         return wrapper
    
#     def timer(self, function: Callable[..., Any]) -> Callable[..., Any]:
#         @wraps(function)
#         def wrapper(*args, **kwargs) -> Any:
#             timeBefore = time.time()
#             returnValue = function(*args, **kwargs)
#             timeAfter = time.time()
#             timeTaken = timeAfter-timeBefore
#             logging.debug(f"'{function.__name__}' function took {timeTaken} seconds to process.")
#             return returnValue
#         return wrapper
    
#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         newFunc = self.loggingF(self.timer(self.function))
#         returnValue = newFunc(*args, **kwargs)
#         return returnValue
        


def timer(function: Callable[..., Any], logger: logging.Logger) -> Callable[..., Any]:
    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        timeBefore = time.time()
        returnValue = function(*args, **kwargs)
        timeAfter = time.time()
        timeTaken = timeAfter-timeBefore
        logger.debug(f"'{function.__name__}' function took {timeTaken} seconds to process.")
        return returnValue
    return wrapper

def loggingF(function: Callable[..., Any], logger: logging.Logger) -> Callable[..., Any]:
    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        logger.debug(f"Calling function '{function.__name__}'")
        returnValue = function(*args, **kwargs)
        logger.debug(f"'{function.__name__}' function was called with a return value '{returnValue}'.")
        logger.debug(f"Finished calling function '{function.__name__}'.")
        return returnValue
    return wrapper

loggingOn = False

@overload
def logC(): ...
@overload
def logC(logger: logging.Logger): ...
def logC(logger: logging.Logger = logging.getLogger()):
    def decorator(function):
        @wraps(function)
        def combiner(*args, **kwargs) -> Any:
            newFunc = loggingF(timer(function, logger), logger)
            returnValue = newFunc(*args, **kwargs)
            return returnValue
        return combiner
    return decorator


if __name__ == '__main__':
    ...
