#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    # Open csv
    with open(filename) as f:
        crash_times = []
        # Load list with crash times
        csv_reader = csv.DictReader(f, delimiter=',')
        for row in csv_reader:
            crash_times.append(row['Time'])
        crash_hours = []
        for time in crash_times:
            if (time != '' and 'c' not in time and "'" not in time
             and "." not in time):
                crash_hours.append(int(time.split(':')[0]))
                
        # Create a new list with the number of crashes per hour in day
        crash_count = [0] * 24
        for i in range(24):
            for hour in crash_hours:
                if  hour == i:
                   crash_count[i] += 1
        return crash_count            
        
        

def weigh_pokemons(filename, weight):
    # List of Pokemon matching weight
    matching = []
    # Deserialize json file
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        # Go through loaded dictionary
        for pok in data["pokemon"]:
            # Get weight value and convert from string to float
            pokemon_weight = float(pok["weight"].split(" ", 1)[0])
            # Add to matching if need be
            if pokemon_weight == weight:
                matching.append(pok["name"])
    return matching
    
def single_type_candy_count(filename):
    count = 0
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        # Go through loaded dictionary
        for pok in data["pokemon"]:
            # Only look at Pokemon if it is single type
            if len(pok["type"]) == 1:
                try:
                    count += pok["candy_count"]
                except:
                    continue         
    return count

def reflections_and_projections(points):
    reflected_points = np.copy(points)
    #for i in range(len(points[0])):
    #    y = points[1, i]
    #    y = (-1 * y) + 2
    #    reflected_points[1, i] = y
    #reflected_points = (-1) * points + 2
    #print(reflected_points)
    # This is a numby array, so we can project this all at once
    reflected_points[1] = (reflected_points[1] * (-1)) + 2
    rotation_array = np.array([[0, -1], [1, 0]])
    rotated_points = rotation_array @ reflected_points
    #print(rotated_points)
    projected_array = 1/(10) * np.array([[1, 3], [3, 9]]) 
    projected_points = projected_array @ rotated_points
    #print(projected_points)
    return projected_points
        
def normalize(image):
    maximum = np.amax(image)
    minimum = np.amin(image)
    normed_image = np.int_((255*(image - minimum)) / (maximum - minimum))
    return normed_image     
    

def sigmoid_normalize(image, a):
    maximum = np.amax(image)
    minimum = np.amin(image)
    normed_image = np.int_(255*(1+np.exp((-a**(-1))*(image-128)))**(-1))
    return normed_image    

#print(histogram_times('airplane_crashes.csv'))
#print(weigh_pokemons('pokedex.json', 10.0))
#print(single_type_candy_count("pokedex.json"))
#image = np.array([[1,2], [3,4]])
#print()
#print("RP: ", reflections_and_projections(image))
#reflections_and_projections(image)
#print()
#print("Normalize ", normalize(image))
#print()
#print("Sigmoid: ", sigmoid_normalize(image, 1000))
