def door_windows_alarm(sensors):
    """
    checks if any of the sensors have been triggered and if so returns true. If any
    of the sensors have been triggered it will return false. sensors readings are passed as a list
    and each element is a boolean that represents the value of a sensor. A true value means that
    the sensor has been activated (so the door or window has been opened) and a false value
    means that the door or window is still closed
    """
    pass

def temperature_proportional_controller(desired_value, real_value, k):
    """
    write a function that returns a value that will be used to control temperature of a water
    heater using a proportional controller algorithm. A proportional controller returns a value
    proportional to the error calculated (so if the error is big and positive, the returned value
    is big and you heater gets a lot hotter. If the error is small, then the returned value is small and
    your heater just get a little bit warmer. If the error is negative means that you should turn off
    your heater by returning a 0). You can calculate the error by substracting the desired value
    from the real value and then return (k* error) if the error is positive
    """
    pass

def speed(time_measurement1, time_measurement2, distance):
    """
    speed is equal to distance/time. You have installed a system to measure cars speed. Your system have
    2 sensors, when a car passes each of those sensors you read what time is it. You also know the
    distance between those 2 sensors. you can assume that time_measurement2 is always greater
    than time_measurement1. Given these 2 time measurements and the distance between 
    the 2 sensors return the speed
    """
    pass

def speeding_cars(sensor_measurements, max_speed):
    """
    sensor_measurements is a list of sensor measurements bundled in tuples
    that can be used on your speed funcion, for example:
    sensor_measurements = [(car1_time1, car1_time1, distance),(car2_time1, car2_time2, distance)]
    calculate the speed of each car and using max_speed return a list of booleans that
    represent if the car has been speeding, for example:
    [car1_speeding, car2_speeding]
    """
    pass

def count_letters(text, letter):
    """
    count how many times 'letter' is repeated in 'text'. For example if letter is 'a'
    and text is 'a great acorn' this function should return 3
    """
    pass

def items_in_store(desired_items, store_items):
    """
    desired_items and store_items are both lists. This function will check if the
    store has all the desired items and return true in that case. After finishing
    implementing this function check with me if thre is a more efficient solution
    """
    pass

def decode_number_tone(dialed_number_frequencies):
    """
    On old telephonic systems, the dialed number is transmitted by sending 2 codes together
    (frequencies). The following table shows the value of the frequencies sent when a key is pressed:
    Key	Frequency
    1	[697, 1209]
    2	[697, 1336]
    3	[697, 1477]
    4	[770, 1209]
    5	[770, 1336]
    6	[770, 1477]
    7	[852, 1209]
    8	[852, 1336]
    9	[852, 1477]
    0	[941, 1336]
    This function receives as an input a list containing the 2 frequencies sent and returns which
    key was dialed. Notice that the frequencies on dialed_number_frequencies might not be ordered,
    so you will either need to order them or handle 2 cases for each key. In case the input do not
    match a key return None.
    """
    pass


def decode_full_number_tone(number_tones):
    """
    this function builds on decode_number_tone. Now you receive a list containing
    the different frequencies found when dialing a full number. Return the full
    dialed number inside a list
    """
    pass