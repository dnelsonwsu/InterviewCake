__author__ = 'derek'

import pprint


def find_meeting_insertion_index(meeting_to_insert, condensed_meeting_schedule):
    if len(condensed_meeting_schedule) == 0:
        return 0

    index = 0
    # Insertion point is first spot where meeting's start time is >= the previous meeting
    for index, meeting in enumerate(condensed_meeting_schedule):
        if meeting_to_insert[0] <= meeting[0]:
            return index

    return index+1


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
    if meeting_first[0] <= meeting_second[0] and meeting_first[1] >= meeting_second[0]:
        # These meetings are either adjacent of overlap
        return True
    else:
        return False


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


def insert_meeting_into_schedule(meeting_being_inserted, insertion_index, meeting_schedule):
    was_combined_with_adjacent_meeting = False

    if insertion_index < len(meeting_schedule):   # if there are more meetings after the insertion index
        meeting_next = meeting_schedule[insertion_index]
        if can_combine_meetings(meeting_being_inserted, meeting_next):
            meeting_combined = combine_meetings(meeting_being_inserted, meeting_next)
            # remove next meeting and replace with new combined meeting
            del meeting_schedule[insertion_index]
            insert_meeting_into_schedule(meeting_combined, insertion_index, meeting_schedule)
            was_combined_with_adjacent_meeting = True

    if insertion_index > 0:
        meeting_previous = meeting_schedule[insertion_index - 1]
        if can_combine_meetings(meeting_previous, meeting_being_inserted):
            meeting_combined = combine_meetings(meeting_previous, meeting_being_inserted)
            # remove previous meeting and replace with new combined meeting
            del meeting_schedule[insertion_index-1]
            insert_meeting_into_schedule(meeting_combined, insertion_index-1, meeting_schedule)
            was_combined_with_adjacent_meeting = True

    if not was_combined_with_adjacent_meeting:
        meeting_schedule.insert(insertion_index, meeting_being_inserted)


def condense_meeting_times(original_meeting_schedule):
    condensed_meeting_schedule = []

    # for each time slot in original meeting schedule
    for meeting in original_meeting_schedule:
        # find insertion point
        insertion_index = find_meeting_insertion_index(meeting, condensed_meeting_schedule)
        # Insert into condensed meeting schedule
        insert_meeting_into_schedule(meeting, insertion_index, condensed_meeting_schedule)

    return condensed_meeting_schedule


def run_problem_4():
    #meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    meeting_times =   [(1, 10), (2, 6), (3, 5), (7, 9)]
    condensed_meeting_times = condense_meeting_times(meeting_times)
    pprint.pprint(condensed_meeting_times)


if __name__ == "__main__":
    run_problem_4()
