def letter_grade(score):
    grade = ''
    if score >=90:
        grade ='A'
    elif score >=80:
        grade ='B'
    elif score >=70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade ='E'
    return grade
def count_vowels(strings):
    results = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for word in strings:
        for letter in word:
            if letter.lower() in results:
                results[letter.lower()]=results[letter.lower()]+1
    return results
def count_words(strings):
    results= {}
    for word in strings:
        words = word.split(" ")
        for index in words:
            if index not in results:
                results[index] = 1
            else:
                results[index] = results[index]+1
    return results
def words_by_first_letter(strings):
    results = {}
    for word in strings:
        words = word.split(" ")
        for index in words:
            if index[0] not in results:
                results[index[0]] = [index]
            else:
                results[index[0]].append(index)
    return results
def indices_of_words(strings):
    results = {}
    for index in range(len(strings)):
        words = strings[index].split(" ")
        for word in words:
            if word not in results:
                results[word] = [index]
            else:
                if index not in results[word]:
                    results[word].append(index)
    return results
def by_grade(grades):
    results = {}
    for key in grades:
        value = grades[key]
        if value not in results:
            results[value] = [key]
        else:
            results[value].append(key)
    return results
def compute_letter_grades(grades):
    results = {}
    for key in grades:
        value = 0
        for index in grades[key]:
            value = value+index
        value = value/len(grades[key])
        grade = letter_grade(value)
        results[key] = grade
    return results
def add_letter_grade(grades):
    results = {}
    for name in grades:
        results[name] = {}
        for key in grades[name]:
            if key not in results[name]:
                results[name][key] = grades[name][key]
        score = 0
        if "test" in results[name]:
            score = results[name]["test"]*2 +score
        else:
            results[name]["test"] = 0
        if "hw" in results[name]:
            score = score + results[name]["hw"]
        else:
            results[name]["hw"] = 0
        score = score/3
        grade = letter_grade(score)
        results[name]["course"] = grade
    return results
def compute_all_letter_grades(grades):
    results = {}
    for index in grades:
        for name in grades[index]:
            score = grades[index][name]
            if name not in results:
                results[name]=0
            if index == 'test':
                results[name] = results[name]+score +score
            if index =="hw":
                results[name] = results[name]+score

    for name in results:
        score = results[name]/3
        grade = letter_grade(score)
        results[name] = grade
    return results
def unflatten_grades(grades):
    results = {}
    for index in grades:
        name = index["name"]
        if name not in results:
            results[name] = {}
        category = index["category"]
        if category not in results[name]:
            results[name][category] = [index["score"]]
        else:
            results[name][category].append(index["score"])
    return results
def gather(values):
    results = {}
    current =""
    for index in values:
        if isinstance(index,str):
            current = index
            if index not in results:
                results[index] = []
        if isinstance(index,int) and current != "":
            results[current].append(index)
    return results

