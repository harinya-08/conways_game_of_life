# utils.py
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=60)
    parser.add_argument('--height', type=int, default=30)
    parser.add_argument('--fps', type=int, default=10)
    return parser.parse_args()
