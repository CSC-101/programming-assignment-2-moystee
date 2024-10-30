import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        input1, input2 = data.Point(8, 4), data.Point(4, 6)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(4,6), data.Point(8,4))
        self.assertEqual(expected, result)
    def test_create_rectangle_2(self):
        input1, input2 = data.Point(1, 2), data.Point(6, 4)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(1,4), data.Point(6,2))
        self.assertEqual(expected, result)
    # Part 2
    def test_shorter_duration_than_1(self):
        input1, input2 = (data.Song("Artist", "Song", data.Duration(2,44)),
        data.Song("Artist", "Song", data.Duration(3, 3)))
        result = hw2.shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(expected, result)
    def test_shorter_duration_than_2(self):
        input1, input2 = (data.Song("Artist", "Song", data.Duration(4,44)),
        data.Song("Artist", "Song", data.Duration(3, 3)))
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(expected, result)
    # Part 3
    def test_song_shorter_than_1(self):
        input1, input2 = [data.Song("Artist", "Song", data.Duration(2,44)),
        data.Song("Artist", "Song", data.Duration(3, 30))], data.Duration(3,0)
        result = hw2.song_shorter_than(input1, input2)
        expected = [data.Song("Artist", "Song", data.Duration(2,44))]
        self.assertEqual(expected, result)
    def test_song_shorter_than_2(self):
        input1, input2 = [data.Song("Artist", "Song", data.Duration(2,44)),
        data.Song("Artist", "Song", data.Duration(3, 30))], data.Duration(2,0)
        result = hw2.song_shorter_than(input1, input2)
        expected = []
        self.assertEqual(expected, result)
    # Part 4
    def test_running_time_1(self):
        input1, input2 = [data.Song("Artist", "Song", data.Duration(2, 45)),
        data.Song("Artist", "Song", data.Duration(3, 30)),
        data.Song("Artist", "Song", data.Duration(1, 50))], [0,1,2]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(8,5)
        self.assertEqual(expected, result)
    def test_running_time_2(self):
        input1, input2 = [data.Song("Artist", "Song", data.Duration(2, 45)),
        data.Song("Artist", "Song", data.Duration(3, 30)),
        data.Song("Artist", "Song", data.Duration(1, 50))], [2,2,2]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(5,30)
        self.assertEqual(expected, result)
    # Part 5
    def test_validate_route_1(self):
        input1, input2 = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
                          ['atascadero', 'santa margarita'], ['atascadero', 'creston']], ['san luis obispo',
                           'atascadero']
        result = hw2.validate_route(input1, input2)
        expected = False
        self.assertEqual(expected, result)
    def test_validate_route_2(self):
        input1, input2 = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
                          ['atascadero', 'santa margarita'], ['atascadero', 'creston']], ['san luis obispo',
                           'santa margarita', 'atascadero']
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(expected, result)
    # Part 6
    def test_longest_repetition_1(self):
        input = [1, 1, 2, 2, 1, 1, 1, 3]
        result = hw2.longest_repetition(input)
        expected = 4
        self.assertEqual(expected, result)
    def test_longest_repetition_2(self):
        input = [1, 1, 2, 2, 2, 1, 1, 3]
        result = hw2.longest_repetition(input)
        expected = 2
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
