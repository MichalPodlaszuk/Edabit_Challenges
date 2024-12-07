time_taken_list = [5, 5, 10, 10, 15, 15, 20, 20]
interview_time = 120


def interview(list, time):
    i = 0
    if time <= 120:
        for item in list:
            n = 5 * (i // 2 + 1)
            if item > n:
                return "disqualified"
            else:
                pass
            i += 1
        return "qualified"
    else:
        return "disqualified"


print(interview(time_taken_list, interview_time))
