import argparse

import env


def main():

    env1 = env.Env({'0': 1, '1': 2})
    steps = FLAGS.steps
    i = 0

    while i < steps:


        i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=30,
                        help='number of steps')
    FLAGS, unparsed = parser.parse_known_args()
    main()
