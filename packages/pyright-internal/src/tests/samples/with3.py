# This sample verifies the proper type analysis of context managers
# that suppress exceptions, as indicated by a return type of "bool"
# for the __exit__ or __aexit__ method.

from contextlib import suppress


def test1() -> None:
    class A:
        b: str

    x = b""
    a = A()
    with memoryview(x), suppress(AttributeError):
        if a.b:
            raise RuntimeError()
        return

    # This should generate an error because
    # the code is not unreachable.
    c = "hi" + 3

    with memoryview(x):
        raise RuntimeError()

    # This should not generate an error because
    # the code is unreachable.
    return 3


def test2() -> None:
    some_dict = dict()

    with suppress(KeyError):
        print(some_dict["missing_key"])

    # This should generate an error because the
    # code is reachable.
    return 1


def test3(cm: suppress) -> None:
    some_dict = dict()

    with cm:
        print(some_dict["missing_key"])

    # This should generate an error because the
    # code is reachable.
    return 1

class CMFactory:
    def suppress(self) -> suppress:
        return suppress()

def test4() -> None:
    some_dict = dict()

    with CMFactory().suppress():
        print(some_dict["missing_key"])

    # This should generate an error because the
    # code is reachable.
    return 1
