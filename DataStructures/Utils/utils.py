from DataStructures.Utils.error import FunctionNotImplemented
import pytest


def handle_not_implemented(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FunctionNotImplemented as exp:
            if "NOT_IMPLEMENTED" in exp.type:
                pytest.skip(exp.function + " Not implemented yet")
            else:
                raise exp
        except AttributeError as exp:
            if "module 'DataStructures" in str(exp):
                pytest.skip(exp.name + " Not implemented yet")
            else:
                raise exp
    return wrapper
