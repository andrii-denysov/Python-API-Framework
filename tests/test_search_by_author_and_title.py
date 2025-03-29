from http import HTTPStatus

import pytest
from hamcrest import assert_that, contains_string, equal_to, equal_to_ignoring_whitespace

from json_schemas.default_response import DEFAULT_RESPONSE_SCHEMA
from services.poetrydb.poetrydb_service import PoetryDB
from tests.base_test import BaseTest
from utils.helpers.common_actions import CommonActions


@pytest.mark.TC_001
class TestSearchByAuthorAndTitle(BaseTest):

    def test_search_by_author_and_title(self):
        author_name = "William Shakespeare"
        title = "Sonnet 1: From fairest creatures we desire increase"
        query_map = {self.AUTHOR: author_name, self.TITLE: title}
        expected_poem = """From fairest creatures we desire increase,
         That thereby beauty's rose might never die,
          But as the riper should by time decease,
           His tender heir might bear his memory:
            But thou contracted to thine own bright eyes,
             Feed'st thy light's flame with self-substantial fuel,
              Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel:
               Thou that art now the world's fresh ornament,
                And only herald to the gaudy spring,
                 Within thine own bud buriest thy content,
                  And tender churl mak'st waste in niggarding:
                   Pity the world, or else this glutton be,
                    To eat the world's due, by the grave and thee.
        """
        response = PoetryDB().get_query(CommonActions.build_query(query_map))

        response.has.status(HTTPStatus.OK)
        response.schema_validate(DEFAULT_RESPONSE_SCHEMA)
        assert_that(len(response.content), equal_to(1), "Only one poem should be returned")
        actual_title = response.content[0].get(self.TITLE)
        actual_author = response.content[0].get(self.AUTHOR)
        actual_poem = " ".join(response.content[0].get(self.LINES))
        assert_that(actual_poem, equal_to_ignoring_whitespace(expected_poem))
        assert_that(actual_title, equal_to_ignoring_whitespace(title),
                    f"Expected title {title}, but was {actual_title}")
        assert_that(actual_author, equal_to_ignoring_whitespace(author_name),
                    f"Expected author {author_name}, but was {actual_author}")