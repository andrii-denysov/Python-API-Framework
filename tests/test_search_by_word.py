from http import HTTPStatus

import pytest
from hamcrest import assert_that, contains_string

from json_schemas.default_response import DEFAULT_RESPONSE_SCHEMA
from services.poetrydb.poetrydb_service import PoetryDB
from tests.base_test import BaseTest
from utils.helpers.common_actions import CommonActions


@pytest.mark.TC_002
class TestSearchByWord(BaseTest):

    def test_search_by_word(self):
        search_word = "nebula"
        query_map = {self.LINES: search_word}
        search_query = CommonActions.build_query(query_map)
        response = PoetryDB().get_query(search_query)

        response.has.status(HTTPStatus.OK)
        response.schema_validate(DEFAULT_RESPONSE_SCHEMA)
        for poem_lines in response.content:
            poem = " ".join(poem_lines.get("lines"))
            assert_that(poem, contains_string(search_word),
                        f"Search word '{search_word}' is missing in '{poem}' string")
