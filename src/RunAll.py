"""Thought I would try and do this in a weird way to see whats possible"""

import os
import sys
import argparse
import timeit
import collections

ROOT_ADDRESS = "https://projecteuler.net/problem="
FILE_PATH = "/".join(os.path.abspath(__file__).split("/")[:-1])
PROBLEM_PATH = os.path.join(FILE_PATH, "Problems")
sys.path.insert(0, PROBLEM_PATH)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", default=True, action="store_true")
    return parser.parse_args()


def import_all_mains(list):
    """
    Import all project scripts and store module path in a dict
    :param list: List of relative file paths
    :return: Dict of modules
    """
    unsorted = {}
    for idx, file in enumerate(list):
        if file[0:7] == "Problem":
            p_num = int(file.split(" ")[0].split("m")[1])
            _ = __import__(file[:-3])
            unsorted[p_num] = _

    out = collections.OrderedDict(sorted(unsorted.items()))

    return out


def run_files(projects, time_funcs):
    """
    Execute main functions in modules
    :param projects: Dict of modules
    :param time_funcs: If True, report the time to run.
    :return: None
    """
    print("")
    times = {}
    for p_num, mod in projects.items():
        print(f"\n- Testing Problem {p_num}:")
        print(f"    {ROOT_ADDRESS+str(p_num)}")
        print(f"    Functionality: {mod.main.__doc__}")
        s_t = timeit.default_timer()
        out = mod.main(mod.INPUT)
        e_t = timeit.default_timer()
        t_t = (e_t - s_t)
        if out == mod.ANSWER:
            print("    Correct answer of {} returned in {:.5f} seconds".format(out, t_t))
        else:
            print("    Incorrect answer of {} returned in {:.5f} seconds".format(out, t_t))
            print(f"    Correct Answer is {mod.ANSWER}.")
        times[p_num] = t_t

    sorted_times = dict(sorted(times.items(), key=lambda item: item[1], reverse=True))
    print(f"Listing Problems by time taken to return:")
    for idx, (p_num, time) in enumerate(sorted_times.items()):
        print("    {} - Problem {} : {:.5f} seconds".format(idx+1, p_num, time))



if __name__ == "__main__":
    args = parse_args()
    projects = import_all_mains(os.listdir(PROBLEM_PATH))

    run_files(projects, time_funcs=args.time)

