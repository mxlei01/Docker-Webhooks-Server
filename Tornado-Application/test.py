import tornado
import docker_commands
from tornado.testing import AsyncTestCase

class Test_APIs(AsyncTestCase):
    @tornado.testing.gen_test
    def test_stopRepoContainer(self):
        # Tests the string stopRepoContainer if string replacement succeeded
        command = docker_commands.stopRepoContainer % ("mxlei01/repo")
        self.assertIn("mxlei01/repo", command)

    @tornado.testing.gen_test
    def test_deleteRepoContainers(self):
        # Tests the string deleteRepoContainers if string replacement succeeded
        command = docker_commands.deleteRepoContainers % ("mxlei01/repo")
        self.assertIn("mxlei01/repo", command)

    @tornado.testing.gen_test
    def test_deleteRepoImages(self):
        # Tests the string deleteRepoImages if string replacement succeeded
        command = docker_commands.deleteRepoImages % ("mxlei01/repo")
        self.assertIn("mxlei01/repo", command)

    @tornado.testing.gen_test
    def test_pullRepo(self):
        # Tests the string pullRepo if string replacement succeeded
        command = docker_commands.pullRepo % ("mxlei01/repo")
        self.assertIn("mxlei01/repo", command)

    @tornado.testing.gen_test
    def test_runRepo(self):
        # Tests the string runRepo if string replacement succeeded
        command = docker_commands.runRepo % ("mxlei01/repo", "mxlei01/repo")
        self.assertIn("mxlei01/repo", command)