import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    post_code: str


user = User("Иван", "Лукин", "450926")