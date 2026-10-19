from dataclasses import dataclass
from enum import Enum


class tireLoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


@dataclass(frozen=True)
class Success[T]:
    value: T


@dataclass(frozen=True)
class Failure[E]:
    error: E


type Result[T, E] = Success[T] | Failure[E]


def tire_load_users(users: list[User]) -> Result[list[User], str]:
    return Success(users) if users else Failure("Список пользователей пуст")


print("Загрузка пользователей:", tire_load_users([
    User("Илья", 21, "ravluk@mail.ru"),
    User("Влад", 25, "vladick@mail.ru"),
    User("Мегарыцарь", 19, "megaknight@supercell.com"),
]))
