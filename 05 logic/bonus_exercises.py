#_______________ex1_________________
print("=" * 10, " exercise #1.", "=" * 10)
list_1 = [1, 1, 10, 10, 9, 9, 5, 5, 6, 8, 8]


#O(n)
def find_unique(num_list):
    tmp_list = []
    for num in num_list:
        tmp_list.remove(num) if num in tmp_list else tmp_list.append(num)

    return tmp_list.pop()


print(f"O(n) version: {find_unique(list_1)}")


def find_unique_imp(num_list):
    num_set = set(num_list)

    for num in num_set:
        num_list.remove(num)
    for num in num_list:
        num_set.remove(num)
    return num_set.pop()


print(f"O(n*log(n)) [i think] version: {find_unique_imp(list_1)}")

#_______________ex2_________________
print("=" * 10, " exercise #2.", "=" * 10)
w_list = ["java", "jjav", "aavj", "jaav", "ja", "dan", "and", "dnd"]


def count_words(word_list):
    tmp_dict = {}
    for word in word_list:
        s_word = ''.join(sorted(word))
        if s_word not in tmp_dict.keys():
            tmp_dict[s_word] = 1
        else:
            tmp_dict[s_word] += 1

    return tmp_dict

print(count_words(w_list))
