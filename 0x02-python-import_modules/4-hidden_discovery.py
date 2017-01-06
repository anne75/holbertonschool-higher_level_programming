#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    correct = [x for x in dir(hidden_4) if not x[:2] == "__"]
    if len(correct):
        print("\n".join(correct))
