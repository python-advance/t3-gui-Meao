import unittest

import os
import sys
import time
import os.path as op
from functools import partial
from kivy.clock import Clock

# it's not a relative import!
# test with --pythonpath "<path to main.py>"
from quad_eq import MainApp


class Test(unittest.TestCase):
    # sleep function that catches `dt` from Clock
    def pause(*args):
        time.sleep(0.000001)

    # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        ids = app.root.ids

        # Do something
        ids.a.text = "2"
        ids.b.text = "2"
        ids.c.text = "2"

        app.root.solve()

        self.assertEqual('D < 0', ids.d.text)
        self.assertEqual('Нет корней', ids.x.text)

        app.stop()

    # same named function as the filename(!)
    def test_example(self):
        app = MainApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()

if __name__ == '__main__':
    unittest.main()
