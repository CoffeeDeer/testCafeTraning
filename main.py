class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()

        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

        return result

    def setUp(self):
        pass

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.log = self.log + "testMethod "

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):
    def setUp(self):
        print('TestCaseTest SetUp')
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        print(test.log)
        assert('setUp testMethod tearDown ' == test.log)

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 faild" == result.smmary())



class TestResult():
    def __init__(self):
        self.runCount = 0
        self.failCount = 0

    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return "{0} run, {1} faild".format(self.runCount, self.runCount)


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testFailedResult").run()

