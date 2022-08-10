import logging
import pytest
from api.book_store_api import BookApi

data = {
    "userId": "9d99ecdd-458d-4431-a228-3f86a2946800",
    "collectionOfIsbns": [
        {
            "isbn": "9781449365035",
            "title": "Speaking JavaScript",
            "subTitle": "An In-Depth Guide for Programmers",
            "author": "Axel Rauschmayer",
            "publish_date": "2014-02-01T00:00:00.000Z",
            "publisher": "O'Reilly Media",
            "pages": 460,
            "description": "Like it or not, JavaScript is everywhere these days-from browser to server to mobile-and now you, too, need to learn the language or dive deeper than you have. This concise book guides you into and through JavaScript, written by a veteran programmer who o",
            "website": "http://speakingjs.com/"
        }
    ]
}


@pytest.mark.passed
def test_get_bookSore():
    """
    Check if you get books from the bookstore
    passed
    """
    logging.info("get book store")
    getBookStore = BookApi().get_bookStore()
    print(f' staaaaaaaaattuuusss code {getBookStore.status_code}')
    logging.info("get bookstore")
    assert getBookStore.status_code == 200


@pytest.mark.passed
def test_post_bookstore():
    """
    Check to add an existing user
    passed
    """
    logging.info("add a new user to the store")

    postbook = BookApi().post_bookStore(data)
    logging.info("Successful Post Book")
    logging.warning(f'Error, status code is {postbook.status_code}')
    assert postbook.status_code == 200