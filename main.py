class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.testStarted()
        self.setUp()

        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            print(e)
            result.testFailed()
        
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

    def testBrokenMethod(self):
        raise Exception


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run(self.result)
        assert('setUp testMethod tearDown ' == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFaildResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())


    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        
        suite.run(self.result)
        
        assert("2 run, 1 failed" == self.result.summary())


class TestResult():
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return "{0} run, {1} failed".format(self.runCount, self.failureCount)


class TestSuite():
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


suite = TestSuite()

suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFaildResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()

suite.run(result)
print(result.summary())
