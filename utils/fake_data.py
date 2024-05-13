from dataclasses import dataclass

from faker import Faker
from polyfactory.factories import DataclassFactory

fake = Faker("ru_RU")


@dataclass
class FakeProductData:
    name: str
    model: str
    seo: str


class FakeProductDataFactory(DataclassFactory[FakeProductData]):
    __faker__ = Faker(locale="ru_RU")


@dataclass
class FakeCustomerRegistrationData:
    first_name: str
    last_name: str
    email: str
    password: str


class FakeCustomerRegistrationDataFactory(
    DataclassFactory[FakeCustomerRegistrationData]
):
    __faker__ = Faker(locale="ru_RU")

    @classmethod
    def first_name(cls) -> str:
        return cls.__faker__.first_name()

    @classmethod
    def last_name(cls) -> str:
        return cls.__faker__.last_name()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()
