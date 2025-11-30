"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module provides functions to calculate bake time, preparation time,
and total elapsed cooking time for lasagna.
"""

# Constant for the expected bake time of the lasagna (in minutes)
EXPECTED_BAKE_TIME = 40

# Constant for preparation time per layer (in minutes)
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from EXPECTED_BAKE_TIME.

    This function calculates how many minutes are left for the lasagna to bake
    based on the expected bake time and the time already spent baking.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    This function calculates the time required to prepare the lasagna based
    on the number of layers, with each layer taking PREPARATION_TIME minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking, and calculates the total elapsed minutes spent cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    
    
    
    
    
    
    
    
