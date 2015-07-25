__author__ = 'derek'

import pprint




def can_combine_meetings(meeting_1, meeting_2):
    meeting_first = None
    meeting_second = None

    if meeting_1[0] < meeting_2[0]:
        meeting_first = meeting_1
        meeting_second = meeting_2
    else:
        meeting_first = meeting_2
        meeting_second = meeting_1

    # if the first meeting starts before at at the same time as the second meeting and
    # the the first meeting ends after the start of the second
    meetings_overlap_or_adjacent = meeting_first[0] <= meeting_second[0] and meeting_first[1] >= meeting_second[0]
    return meetings_overlap_or_adjacent


def combine_meetings(meeting_first, meeting_second):

    meeting_combined = [0, 0]
    if meeting_first[0] < meeting_second[0]:
        meeting_combined[0] = meeting_first[0]
    else:
        meeting_combined[0] = meeting_second[0]

    if meeting_first[1] > meeting_second[1]:
        meeting_combined[1] = meeting_first[1]
    else:
        meeting_combined[1] = meeting_second[1]

    return tuple(meeting_combined)


def condense_meeting_times(meeting_schedule):
    # Sort the meetings by the start time
    meeting_schedule.sort(key=lambda meeting:meeting[0])

    meeting_index = 0
    while meeting_index < len(meeting_schedule)-1:
        if can_combine_meetings(meeting_schedule[meeting_index], meeting_schedule[meeting_index+1]):
            meeting_combined = combine_meetings(meeting_schedule[meeting_index], meeting_schedule[meeting_index+1])
            del meeting_schedule[meeting_index + 1]
            del meeting_schedule[meeting_index]
            meeting_schedule.insert(meeting_index, meeting_combined)
        else:
            meeting_index += 1

    return meeting_schedule


def run_problem_4():
    meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    #meeting_times =   [(1, 10), (2, 6), (3, 5), (7, 9)]
    condensed_meeting_times = condense_meeting_times(meeting_times)
    pprint.pprint(condensed_meeting_times)


if __name__ == "__main__":
    run_problem_4()
