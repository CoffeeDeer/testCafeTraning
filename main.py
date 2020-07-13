class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        print("when this")


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        print('is called')
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    #19
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)


#TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

"""

테스트케이스 테스트 객체 생성
생성자 호출 - testcase __init__ 이름 입력
run 실행


"""