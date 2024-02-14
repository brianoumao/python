# list datastructure
# list are changeable


my_list = ["apple", "banana", "mangoes", "pineapples"]

my_list.sort()
print(my_list)

my_list[1] = "pineapples"
print(f"I Love eating {my_list[1]}")

my_list = ["1", "2", "3", "4", "5"]

my_list.sort()
print(my_list)

my_list[1] = "1"
print(f"I Love number {my_list[1]}")

# tuple data structures

my_tuple = ("apple", "banana", "pineapples")
print(my_tuple)
print(f"{my_tuple[0]} has {my_tuple[1]}")

# set datastructures
# unordered
my_set = {"England", "China", "USA", "Russia", "Australia", "Brazil", "Kenya"}
print(my_set)
my_set.add("Brazil")
print(my_set)

# dictionaries data structures

my_dic = {"Name": "Brian", "Age": 25, "Gender": "Male", "Profession": "Professional Basketball player"}
print(my_dic)
print(f" My name is {my_dic['Name']} I am {my_dic['Age']} years old . I am {my_dic['Gender']} and I am {my_dic['Profession']}")
