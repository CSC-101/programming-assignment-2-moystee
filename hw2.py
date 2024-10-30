import data
from typing import Optional
# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point, p2: data.Point) -> data.Rectangle:
    if p1.x < p2.x:
        top_left_x = p1.x
    else:
        top_left_x = p2.x
    if p1.x > p2.x:
        bottom_right_x = p1.x
    else:
        bottom_right_x = p2.x
    if p1.y > p2.y:
        top_left_y = p1.y
    else:
        top_left_y = p2.y
    if p1.y < p2.y:
        bottom_right_y = p1.y
    else:
        bottom_right_y = p2.y
    top_left = data.Point(top_left_x, top_left_y)
    bottom_right = data.Point(bottom_right_x, bottom_right_y)
    return data.Rectangle(top_left, bottom_right)
#Purpose: Create a rectangle by finding the bottom right and top left point (corners)
# Part 2
def shorter_duration_than(song1: data.Song, song2: data.Song) -> bool:
    if song1.duration.minutes < song2.duration.minutes:
        return True
    elif song1.duration.minutes > song2.duration.minutes:
        return False
    return song1.duration.seconds < song2.duration.seconds
#Purpose: Return true if first song is shorter than the second, otherwise false
# Part 3
def song_shorter_than(songs: list[data.Song], max_duration: data.Duration) -> list[data.Song]:
    return [song for song in songs if song.duration.minutes < max_duration.minutes or song.duration.minutes
            == max_duration.minutes and song.duration.seconds < max_duration.seconds]
#Purpose: Return songs within a list that are shorter than duration inputted
# Part 4
def running_time(songs: list[data.Song], playlist: list[int]) -> data.Duration:
    total_minutes = 0
    total_seconds = 0
    for song in playlist:
        if song >= 0:
            if song < len(songs):
                song_duration = songs[song].duration  # Access the song's duration
                total_minutes += song_duration.minutes
                total_seconds += song_duration.seconds
    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60
    return data.Duration(total_minutes, total_seconds)
#Purpose: Adds each song's running time together and display total
# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(route) <= 1:
        return True
    for i in range(len(route) - 1):
        city_a = route[i]
        city_b = route[i + 1]
        link_found = False
        for link in city_links:
            if (city_a in link) and (city_b in link):
                link_found = True
                break
        if not link_found:
            return False
    return True
#Purpose: Determine if a route between two cities is a valid route by looking for links between 1+ pairs.
# Part 6
def longest_repetition(numbers: list[int]) -> Optional[int]:
    if not numbers:
        return None
    longest_index = None
    longest_length = 0
    current_index = 0
    current_length = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                longest_index = current_index
            current_index = i
            current_length = 1
    if current_length > longest_length:
        longest_index = current_index
    return longest_index
#Purpose: Output the starting index number that begins the largest repetition in a row within the entire list of numbers