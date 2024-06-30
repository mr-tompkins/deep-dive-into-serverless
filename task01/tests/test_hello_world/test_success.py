from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        expected = {
            'statusCode': 200,
            'message': 'Hello from Lambda'
        }
        
        actual = self.HANDLER.handle_request(dict(), dict());

        self.assertEqual(actual, expected)

