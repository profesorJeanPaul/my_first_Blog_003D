from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostTestCase( TestCase ):
    def test_postPublish( self ):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 2
        # Assert
        self.assertEqual(expected,result)

    def test_postPublish2( self ):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 3
        # Assert
        self.assertEqual(expected,result)

    def test_postPublish3( self ):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 2
        # Assert
        self.assertEqual(expected,result)