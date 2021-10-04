import unittest
from recruitment_tasks import *

class Test(unittest.TestCase):

    def test_task_1(self):
        self.assertEqual(task_1(0), 0)
        self.assertEqual(task_1(10001), 10001)
        self.assertEqual(task_1(110000), 11)
        self.assertEqual(task_1(512), 215)
        self.assertEqual(task_1(-954), -459)
        self.assertEqual(task_1(-2147483648), 0)
        self.assertEqual(task_1(2147483647), 0)
        self.assertEqual(task_1(2147447412), 2147447412)

    def test_task_2(self):
        self.assertCountEqual(task_2("46") , ["gm", "gn", "go", "hm", "hn", "ho", "im", "in", "io"])
        self.assertCountEqual(task_2("") , [])
        self.assertCountEqual(task_2('2'), ["a", "b","c"])
        self.assertCountEqual(task_2('31111'), ['d', 'e', 'f'])
        self.assertCountEqual(task_2("88") , ["tt", "tu", "tv", "ut", "uu", "uv", "vt", "vu", "vv"])

    def test_task_3(self):
        self.assertListEqual(task_3("Hey there mate, it’s nice to finally meet you!", 16),['Hey  there mate,', 'it’s   nice   to', 'finally     meet', 'you!'])
        self.assertListEqual(task_3("If the setUp() method raises an exception while the test is running, the framework will consider the test to have suffered an error, and the test method will not be executed.", 25),
                             ['If   the  setUp()  method', 'raises an exception while', 'the  test is running, the', 'framework  will  consider', 'the test to have suffered', 'an  error,  and  the test', 'method    will   not   be', 'executed.'])


if __name__ == '__main__':
    Test.test_task_1()
    Test.test_task_2()
    Test.test_task_3()

