"""
Mypy examples on dataclasses.
"""
from timeit import default_timer
from dataclasses import dataclass, field


# Check if defaults have effect on speed and assignment
@dataclass
class HasDefault:
    name: str = ""
    age: int = 0


@dataclass(slots=True)
class NoDefault:
    name: str
    age: int


def effects_of_default(iterations: int = 1000):
    """
    Checks if there is any effect of assignment.

    :param iterations:
    :type iterations:
    :return:
    :rtype:
    """

    start = default_timer()
    for _ in range(iterations):
        _ = HasDefault(name="name", age=30)

    print(f"Exec time for dataclass with default values: {default_timer() - start}")

    start = default_timer()
    for _ in range(iterations):
        _ = NoDefault(name="name", age=30)

    print(f"Exec time for dataclass with NO default values: {default_timer() - start}")


# ranges = [1000, 10000, 100000, 1000000, 10000000, 100000000]
# for r in ranges:
#     print(f"range = {r}")
#     effects_of_default(r)


@dataclass(repr=False)
class Foo:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20


b = Foo(x=1, y=2)

print(b)
