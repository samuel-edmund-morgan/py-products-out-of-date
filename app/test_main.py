from datetime import date
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products


class TestOutdatedProducts:

    @pytest.fixture()
    def outdated_products_fixture(self) -> None:
        list_of_products_dicts = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ]
        return list_of_products_dicts

    @pytest.mark.parametrize(
        "today_date,expected_outdated_products",
        [
            pytest.param(
                date(2022, 2, 1),
                [],
                id="No expired products by this day"
            ),
            pytest.param(
                date(2022, 2, 2),
                ["duck"],
                id="Have expired product by this day"
            ),
            pytest.param(
                date(2022, 2, 6),
                ["chicken", "duck"],
                id="Have expired product by this day"
            ),
            pytest.param(
                date(2022, 2, 9),
                ["chicken", "duck"],
                id="Have expired product by this day"
            ),
            pytest.param(
                date(2022, 2, 11),
                ["salmon", "chicken", "duck"],
                id="Have expired product by this day"
            )
        ]
    )
    @mock.patch("app.main.datetime.date")
    def test_outdated_products(self,
                               mocked_date_function: MagicMock,
                               today_date: date,
                               expected_outdated_products: list,
                               outdated_products_fixture: list[dict]
                               ) -> None:

        mocked_date_function.today.return_value = today_date
        assert (outdated_products(outdated_products_fixture)
                == expected_outdated_products)
