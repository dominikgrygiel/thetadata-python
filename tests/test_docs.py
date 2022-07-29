"""Contains tests for the tutorial section of the documentation."""
import docs
from docs.first_request import first_request
from docs.list_roots import get_roots
from docs.end_of_day import end_of_day
from docs import manipulate_df, manipulate_series


def test_docs_first_req():
    """Test the first tutorial."""
    first_request()
    manipulate_df.main()


def test_docs_list_roots():
    """Test the list roots tutorial."""
    get_roots()
    manipulate_series.main()


def test_docs_end_of_day():
    """Test the end of day blog snippet."""
    end_of_day()
