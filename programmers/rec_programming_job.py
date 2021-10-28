invert_index = {
    0:0,
    1:5,
    2:4,
    3:3,
    4:2,
    5:1
}

job_index = {
    0:"SI",
    1:"CONTENTS",
    2:"HARDWARE",
    3:"PORTAL",
    4:"GAME"
}

def solution(table, languages, preference):
    table = [i.split(" ") for i in table]
    scores = []

    for i in range(len(languages)):
        temp = []
        for col in table:
            index = col.index(languages[i]) if languages[i] in col else 0
            col_score = invert_index[index] * preference[i]
            temp.append(col_score)
        scores.append(temp)
    
    scores = [sum(i) for i in zip(*scores)]
    indices = [i for i, x in enumerate(scores) if x == max(scores)]
    jobs = sorted([job_index[i] for i in indices])
    return jobs[0]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["PYTHON", "C++", "SQL"], [7,5,5]))