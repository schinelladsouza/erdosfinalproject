import numpy as np
import pandas as pd

mushrooms = pd.read_csv("mushrooms.csv")

#adds an underscore instead of a hyphen so you can actually write variable names
mushrooms.columns = ['class', 'cap_shape', 'cap_surface', 'cap_color', 'bruises', 'odor',
       'gill_attachment', 'gill_spacing', 'gill_size', 'gill_color',
       'stalk_shape', 'stalk_root', 'stalk_surface_above_ring',
       'stalk_surface_below_ring', 'stalk_color_above_ring',
       'stalk_color_below_ring', 'veil_type', 'veil_color', 'ring_number',
       'ring_type', 'spore_print_color', 'population', 'habitat'] 



#new dataframe that will have the one-hot variables. 
mushrooms_new = pd.DataFrame()
mushrooms_new["edible"] = pd.get_dummies(mushrooms["class"])["e"]


#a dictionary takes the value of a column and returns a dict that gives human translations to all of the values
#(makes figuring out what is happening easier but not necessary)
#there is a "missing" value in stalk root, not sure if that's intended. 
life = {"cap_shape" : {"b" : 'bell', "c" : "conical", 'x' : 'convex','f' : 'flat', 'k' : 'knobbed','s' : 'sunken'},
"cap_surface": { "f":'fibrous','g' : 'grooves','y' : 'scaly','s' : 'smooth'}, 
'cap_color': {'n' : 'brown','b' : 'buff','c' : 'cinnamon','g' : 'gray','r' : 'green', 'p' : 'pink','u' : 'purple',
              'e' : 'red','w' : 'white','y' : 'yellow'}, 
'bruises' : {'t' : 'bruises','f' : 'no'}, 
'odor' : {'a' : 'almond','l' : 'anise','c' : 'creosote', 'y' : 'fishy', 'f' : 'foul', 'm' : 'musty',
          'n' : 'none','p' : 'pungent','s' : 'spicy'}, 
"gill_attachment" : {"a" : 'attached','d' : 'descending','f' : 'free','n' : 'notched'}, 
'gill_spacing' : {'c' : 'close','w' : 'crowded','d' : 'distant'},
'gill_size' : {'b' : 'broad','n' : 'narrow'}, 
'gill_color' : {'k' : 'black','n' : 'brown','b' : 'buff','h' : 'chocolate','g' : 'gray', 'r' : 'green','o' : 'orange'
                                ,'p' : 'pink','u' : 'purple','e' : 'red', 'w' : 'white','y' : 'yellow'}, 
'stalk_shape': { 'e': 'enlarging','t' : 'tapering'}, 
'stalk_root': {'b' : 'bulbous','c' : 'club','u' : 'cup','e' : 'equal', 'z' : 'rhizomorphs',
               'r' : 'rooted','?' : 'missing'},
'stalk_surface_above_ring' : {'f' : 'fibrous','y': 'scaly','k' : 'silky','s' : 'smooth'},
'stalk_surface_below_ring': {'f' : 'fibrous','y' : 'scaly','k' : 'silky','s' : 'smooth'},
'stalk_color_above_ring' : {'n' : 'brown','b' : 'buff','c' : 'cinnamon','g' : 'gray','o' : 'orange',
                            'p' : 'pink','e' : 'red','w' : 'white','y' : 'yellow'},
'stalk_color_below_ring' : {'n' : 'brown','b' : 'buff','c' : 'cinnamon','g' : 'gray','o' : 'orange',
                            'p' : 'pink','e' : 'red','w' : 'white','y' : 'yellow'},
'veil_type' : {'p' : 'partial','u' : 'universal'},
'veil_color' : {'n' : 'brown','o' : 'orange','w' : 'white','y' : 'yellow'},
'ring_number' : {'n' : 'none','o' : 'one','t' : 'two'},
'ring_type' : {'c' : 'cobwebby','e' : 'evanescent','f' : 'flaring','l' : 'large',
               'n' : 'none','p' : 'pendant','s' : 'sheathing','z' : 'zone'},
'spore_print_color' : {'k' : 'black','n' : 'brown','b': 'buff','h' : 'chocolate','r' : 'green', 'o' : 'orange',
                            'u' : 'purple','w' : 'white','y' : 'yellow'},
'population': {'a' : 'abundant','c' : 'clustered','n' : 'numerous', 's' : 'scattered',
               'v' : 'several','y' : 'solitary'},
'habitat': {'g' : 'grasses','l' : 'leaves','m' : 'meadows','p' : 'paths','u' : 'urban','w' : 'waste','d' : 'woods'}}


#code that actually constructs the dataframe
#put in any columns you want for the outer loop. 
for colname in ["spore_print_color", "odor"]: 
    temp = pd.get_dummies(mushrooms[colname])
    values = mushrooms[colname].unique() #lists all the values of the given column, ie for "class" returns ["e","p"]
    for value in values:
        mushrooms_new[colname + "_" + life[colname][value] ] = temp[value] 
        #if you want just the column value, replace with colname + '_' + value 
        
#mushrooms_new has what you want. 
#if you 
