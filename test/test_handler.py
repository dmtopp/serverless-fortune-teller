from unittest import TestCase
from src.handler import handler


class TestHandler(TestCase):
    def test_fortune_returned(self):
        event = {}
        context = {}

        result = handler(event, context)

        self.assertIsInstance(result, str)
