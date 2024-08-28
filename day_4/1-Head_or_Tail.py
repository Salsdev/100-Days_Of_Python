#!/usr/bin/python3
import random

# Print Head or Tail
head_or_tail = random.randint(0, 1)
if head_or_tail == 0:
    print("Head")
else:
    print("Tail")
