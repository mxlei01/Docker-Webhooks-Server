from unittest import TestLoader, TextTestRunner, TestSuite
from unit_tests.docker_command_tests import Test_APIs

# Uses a testLoader to run multiple tests from different python unit tests file
if __name__ == "__main__":
    loader = TestLoader()

    suite = TestSuite((
            loader.loadTestsFromTestCase(Test_APIs),
        ))

    runner = TextTestRunner()
    runner.run(suite)