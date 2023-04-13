import random
import pandas

# LIST COMPREHENSION
# LIST COMPREHENSION
# LIST COMPREHENSION

some_list = [1, 2, 3, 4, 5]

some_new_list = [n + 1 for n in some_list]


def multiple_func(value):
    return value * 2


one_more_list = [multiple_func(n) for n in some_list]

print(some_new_list)
print(one_more_list)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

# LIST Comprehension with conditions and functions

some_string = "bla bla bla"


def capitalise_letter(value):
    return value.upper()


def check_if_letter_is_not_equal_to_space(value):
    if not value == ' ':
        return True
    else:
        return False


some_new_string = [capitalise_letter(n) for n in some_string if check_if_letter_is_not_equal_to_space(n)]

print(str(some_new_string))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=


# LIST Comprehension with range


list_for_range = [n * 2 for n in range(1, 5)]

print(list_for_range)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=


# LIST Comprehension with reading from file


f1_nums = []
with open("file1.txt") as f1:
    f1_nums = [int(n.strip()) for n in f1.readlines()]

f2_nums = []
with open("file2.txt") as f2:
    f2_nums = [int(n.strip()) for n in f2.readlines()]

result = [n for n in f1_nums if n in f2_nums]

print(result)

# DICTIONARY COMPREHENSION
# DICTIONARY COMPREHENSION
# DICTIONARY COMPREHENSION


# DICTIONARY Comprehension with from LIST

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Isabelle', 'Julia']

dictionary_with_scores = {n: random.randint(1, 100) for n in names}

print(dictionary_with_scores)

dictionary_scores_to_dataframe = {"name": [], "score": []}

for key in dictionary_with_scores:
    dictionary_scores_to_dataframe["name"].append(key)
    dictionary_scores_to_dataframe["score"].append(dictionary_with_scores[key])


pandas.DataFrame(dictionary_scores_to_dataframe).to_csv("dict_scores.csv")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

# DICTIONARY Comprehension with from DICTIONARY

students_dataframe = pandas.read_csv("dict_scores.csv")

dictionary_scores_from_csv = {}

for (index, row) in students_dataframe.iterrows():
    dictionary_scores_from_csv[row.name] = row.score


dict_of_passed_students = {key: value for (key, value) in dictionary_scores_from_csv.items() if value > 70}

print(dict_of_passed_students)

