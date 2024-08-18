from enum import StrEnum


class AdminNavigationTabs(StrEnum):
    CATALOG = "catalog"
    CUSTOMERS = "customer"


class AdminNavigationSubtabs(StrEnum):
    CATALOG_PRODUCTS = "catalog/product"
    CUSTOMERS_CUSTOMERS = "customer/customer"
