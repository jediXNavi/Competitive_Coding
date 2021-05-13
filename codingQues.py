import re
import numpy as np
"""A very interesting problem in encountered in one of the coding tests."""

T = ['test1a', 'test2', 'test1b', 'test1c', 'test3']
R = ['Wrong answer', 'OK', 'Runtime error', 'OK', 'Time limit exceeded']


def solution(T, R):
    T_changed = list(map(lambda x: re.findall(r'\d', x)[0], T))
    T_changed = list(map(int, T_changed))
    group_dict = {}
    for (index, test_case, result) in zip(T_changed, T, R):
        test_case_id = f'test|codility{index}'
        if test_case_id in group_dict.keys():
            group_dict.get(test_case_id).append([test_case, result])
        else:
            group_dict[test_case_id] = [[test_case, result]]

    score = score_calculator(group_dict)
    return score


def score_calculator(score_dict):
    scores = []
    for groups in score_dict.keys():
        group_tests = score_dict[groups]
        score = list(map(lambda x: x[1] == 'OK', group_tests))
        if all(score):
            scores.append(1)
        else:
            scores.append(0)

    score = np.mean(scores)
    return np.round(score, 2)


print(solution(T, R))
