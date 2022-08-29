"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:


[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""
import codewars_test as test
#from solution import likes


class Solution:
    def likes(names: list):
        sing_template = "<names> likes this"
        plur_template = "<names> like this"
        plur_w_num_template = "<names> and <num> others like this"

        if not names:
            return sing_template.replace("<names>", "no one")
        elif len(names) == 1:
            return sing_template.replace("<names>", names[0])
        elif len(names) == 2:
            return plur_template.replace("<names>", f"{names[0]} and {names[1]}")
        else:
            name = f"{names[0]}, {names[1]}"
            num = len(names)-2
            if num == 1:
                return plur_template.replace("<names>", f"{names[0]}, {names[1]} and {names[2]}")
            return plur_w_num_template.replace("<names>", name).replace("<num>", str(num))
            

    