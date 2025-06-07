import exercises002
import unittest

class TestExercises002(unittest.TestCase):
    def test_alarm(self):
        self.assertEqual(exercises002.door_windows_alarm([]), False)
        self.assertEqual(exercises002.door_windows_alarm([False]), False)
        self.assertEqual(exercises002.door_windows_alarm([False, True]), True)
        self.assertEqual(exercises002.door_windows_alarm([False, True, False]), True)
        self.assertEqual(exercises002.door_windows_alarm([True]), True)
    
    def test_controller(self):
        self.assertEqual(exercises002.temperature_proportional_controller(50, 50, 1), 0)
        self.assertEqual(exercises002.temperature_proportional_controller(50, 60, 1), 0)
        self.assertEqual(exercises002.temperature_proportional_controller(40, 30, 1), 10)
    
    def test_speed(self):
        self.assertEqual(exercises002.speed(40,50,10), 1)
    
    def test_speeding(self):
        self.assertEqual(exercises002.speeding_cars([],1), [])
        self.assertEqual(exercises002.speeding_cars([(40,50,10)],1), [False])
        self.assertEqual(exercises002.speeding_cars([(40,45,10)],1), [True])
        self.assertEqual(exercises002.speeding_cars([(40,45,10), (40,50,10)],1), [True, False])
    
    def test_count_letter(self):
        self.assertEqual(exercises002.count_letters("",""), 0)
        self.assertEqual(exercises002.count_letters("a great acorn","a"), 3)
        self.assertEqual(exercises002.count_letters("a great acorn","g"), 1)
        self.assertEqual(exercises002.count_letters("a great acorn"," "), 2)
        self.assertEqual(exercises002.count_letters("a great acorn","i"), 0)
    
    def test_items_in_store(self):
        self.assertEqual(exercises002.items_in_store(["water", "bread"],["apples", "bread", "water"]), True)
        self.assertEqual(exercises002.items_in_store(["water", "bread"],["apples", "water", "butter"]), False)
    
    def test_decode_number_tone(self):
        self.assertEqual(exercises002.decode_number_tone([770, 1336]), 5)
        self.assertEqual(exercises002.decode_number_tone([1336, 770]), 5)
        # next one is actually a *
        self.assertEqual(exercises002.decode_number_tone([941, 1209]), None)
        # next one is actually a #
        self.assertEqual(exercises002.decode_number_tone([941, 1477]), None)

    def test_decode_full_number_tone(self):
        number_tones_1 = [
            [852, 1336],
            [852, 1336],
            [852, 1336],
            [770, 1209],
            [770, 1477],
            [852, 1477],
            [697, 1209],
            [697, 1477],
            [852, 1209],
            [697, 1336],
        ]
        self.assertEqual(exercises002.decode_full_number_tone(number_tones_1), [8,8,8,4,6,9,1,3,7,2])
        self.assertEqual(exercises002.decode_full_number_tone([[852, 1336]]), [8])

if __name__ == "__main__":
    unittest.main()