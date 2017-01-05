#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    print("\n".join([x for x in dir(hidden_4) if not x[:2] == "__"]))
