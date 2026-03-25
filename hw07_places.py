######################################################################
# Author: Alain Irumva
# Username: irumvaa
#
# Assignment: HW07: Oh, the Places You'll Go!
#
# Purpose:  To create a map of locations
#           where the user is originally from or has visited,
#           and to use tuples and lists correctly.
######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle, os


def setup_window():
    """
    Creates a window exactly 1100 x 650 and uses world-map.gif as a background pic

    :return: a Turtle Screen object
    """

    wn = turtle.Screen()
    wn.setup(1100,650)
    wn.bgpic("world-map.gif")
    return wn

def place_single_pin(window, place):
    """
    This function places a single pin on the world map.

    :param window: the window object where the pin will be placed
    :param place: a tuple object describing a place to be put on the map in the following format:
            (str: Place, str: Description, float: Latitude, float: Longitude, str: Color)

    :return: None
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    # Create a turtle and put the penup
    pin = turtle.Turtle()
    pin.penup()

    if len(place) !=5:
        print("Invalid place tuple: ", place)
        return
    name, description, lat, long, color = place

    x,y = convert_coordinates(window, long, lat)

    pin.color(color)
    pin.shape("circle")
    pin.goto(x,y)
    pin.stamp()

    pin.write(f"{name}: {description}", font=("Arial", 8, "normal"))


def convert_coordinates(window, long, lat):
    """
    Converts latitude and longitude to x and y coordinates in the map (Screen)

    :param window: Turtle Screen
    :param long: Longitude
    :param lat: Latitude

    :return: x and y coordinates in the Screen
    """
    pin_x= (long / 195) * window.window_width() / 2
    pin_y = (lat / 120) * window.window_height() / 2
    return pin_x, pin_y

    #####################################################
    # You do not need to modify this function!
    #####################################################

    # Logically, the denominator for longitude should be 360; lat should be 180.
    # These values (195 and 120) were determined through testing to account for
    # the extra white space on the edges of the map.
    pin_x = (long / 195) * window.window_width() / 2
    pin_y = (lat / 120) * window.window_height() / 2
    return pin_x, pin_y

def generate_places_list(filename):
    """
    Iterates through the file, and creates the list of places

    :param filename: the name of the file to be opened
    :return: a list representing multiple places
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    file_content = open(filename, 'r')           # Opens file for reading

    str_num = file_content.readline()           # The first line of the file, which is the number of entries in the file
    str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

    places_list = []
    for i in range(str_num):
        places_list.append(extract_place_info(file_content))         # Assembles the list of places

    file_content.close()
    return places_list

def extract_place_info(file_content):
    """
    This function extracts five lines out of file_content,
    which is a variable holding all the file content.
    Each extracted line represents, in order,
        1. a place's name
        2. a place's description
        3. latitude
        4. longitude
        5. a color for the pin

    The function returns the five elements to the function call as a tuple.

    :param file_content: contents of the file which represents all places
    :return: a tuple representing a single place.
    """

    place = []

    for i in range(5):
        content = file_content.readline().strip("\n")

        parts = content.split(":")
        info = parts[1].strip()

        if i == 2:  # latitude
            info = float(info)
        elif i == 3:  # longitude
            info = float(info)

        place.append(info)

    return tuple(place)
    # TODO Return a tuple with each piece of information. Data type is important!

def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list.
    The list of tuples is used to populate the map.

    :return: None
    """

    # A sample file was created for you to use here: places.txt

    in_file = input("Enter the name of the file: ")

    if not os.path.isfile(in_file):
        in_file = "places.txt"
    wn = setup_window()
    places = generate_places_list(in_file)
    for p in places:
        place_single_pin(wn, p)
    wn.mainloop()

    # The red box has already been completed by the above code.



if __name__ == "__main__":
    main()
