from unittest import TestCase

from examples.handlers import HandlerClassInInit
from examples.handlers.another_handler import AnotherHandlerClass
from examples.handlers.handler import HandlerClass, NonHandlerClass, HandlerClass2

from responsebot.handlers.base import BaseTweetHandler
from responsebot.utils.handler_utils import is_handler_class, discover_handler_classes


class DiscoverHandlerClassesTestCase(TestCase):
    def test_discover_handler_classes(self):
        handler_classes = discover_handler_classes('examples.handlers')

        # discover handler class in package init
        self.assertIn(HandlerClassInInit, handler_classes)

        # discover handler class in handler
        self.assertIn(HandlerClass, handler_classes)
        self.assertIn(HandlerClass2, handler_classes)
        self.assertNotIn(NonHandlerClass, handler_classes)

        # discover handler class in multiple modules
        self.assertIn(AnotherHandlerClass, handler_classes)

    def test_discover_handler_classes_in_module(self):
        handler_classes = discover_handler_classes('examples.handlers.handler')

        # discover handler class in handler
        self.assertIn(HandlerClass, handler_classes)
        self.assertIn(HandlerClass2, handler_classes)
        self.assertNotIn(NonHandlerClass, handler_classes)


class IsHandlerClassTestCase(TestCase):
    def test_with_handler_class(self):
        self.assertTrue(is_handler_class(HandlerClass))

    def test_with_non_handler_class(self):
        self.assertFalse(is_handler_class(NonHandlerClass))

    def test_with_non_class_obj(self):
        self.assertFalse(is_handler_class({}))

    def test_with_base_class(self):
        self.assertFalse(is_handler_class(BaseTweetHandler))
