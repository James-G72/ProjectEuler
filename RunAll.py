"""Thought I would try and do this in a weird way to see whats possible"""

import os
import argparse
import timeit
import collections


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
        if file[0:7] == "Project":
            p_num = int(file.split(" ")[0].split("t")[1])
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
    print(f"")
    for p_num, mod in projects.items():
        print(f"\n --- Testing Project {p_num} --- ")
        s_t = timeit.default_timer()
        out = mod.main(mod.INPUT)
        e_t = timeit.default_timer()
        t_t = (e_t - s_t)
        # TODO add docstrings to all main functions to print what the test is about
        if out == mod.ANSWER:
            print("    Correct answer of {} returned in {:.5f} seconds".format(out, t_t))
        else:
            print("    Incorrect answer of {} returned in {:.5f} seconds".format(out, t_t))
            print(f"    Correct Answer is {mod.ANSWER}.")


if __name__ == "__main__":
    args = parse_args()
    all_files = os.listdir(os.getcwd())
    projects = import_all_mains(all_files)

    run_files(projects, time_funcs=args.time)

