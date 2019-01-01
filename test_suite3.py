import unittest

# from SMARS_Library import leg
from SMARS_Library3 import Leg
# from SMARS_Library import set_servo_pulse
from SMARS_Library3 import set_servo_pulse


class SetServoPulseTestCase(unittest.TestCase):
    """ tests setServoPulse """

    # def test_setServoPulseChannelLessThan15(self):
    #     for channel in range(0, 16):
    #         self.assertTrue(set_servo_pulse(channel, 10))

    def test_setservo_pulse_channel_less_than_15(self):  # Python 3 library test
        for channel in range(0, 16):
            self.assertTrue(set_servo_pulse(channel, 10))

    # def test_setServoPulseIsNumberBetween0And4096(self):
    #     self.assertTrue(set_servo_pulse(0, 0))
    #     self.assertTrue(set_servo_pulse(0, 4096))
    #     self.assertTrue(set_servo_pulse(0, 2000))
    #     self.assertFalse(set_servo_pulse(0, 4097))
    #     self.assertFalse(set_servo_pulse(0, -1))

    def testsetservopulseisnumnerbetween0and4096(self):  # Python 3 library test
        self.assertTrue(set_servo_pulse(0, 0))
        self.assertTrue(set_servo_pulse(0, 4096))
        self.assertTrue(set_servo_pulse(0, 2000))
        self.assertFalse(set_servo_pulse(0, 4097))
        self.assertFalse(set_servo_pulse(0, -1))

    # def test_setangle(self):
    #     legtest = leg()  # type: leg
    #     self.assertTrue(legtest.setAngle(0))
    #     self.assertTrue(legtest.setAngle(180))
    #     self.assertFalse(legtest.setAngle(181))

    def test_setangle3(self):  # Python 3 library test
        legtest3 = Leg(channel=0, leg_minangle=0, leg_maxangle=180, invert=False, name="testbot")  # type: Leg
        self.assertTrue(legtest3.setangle(0))
        self.assertTrue(legtest3.setangle(180))
        self.assertFalse(legtest3.setangle(181))


class TestLegSetdefault(unittest.TestCase):
    """ tests leg setdefault() """

    def test_setdefault(self):
        l = Leg(channel=0, leg_minangle=0, leg_maxangle=180, invert=False, name="testbot")
        self.assertIsNone(l.setdefault())


if __name__ == '__main__':
    unittest.main()