#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")


লজিক পয়েন্ট (Logic Breakdown)১. সংখ্যাটি বিজোড় (Odd) হলে: সরাসরি Weird প্রিন্ট করতে হবে।
(পাইথনে বিজোড় চেক করার নিয়ম: n % 2 != 0)
২. সংখ্যাটি জোড় (Even) হলে:২ থেকে ৫-এর মধ্যে হলে 
(2 \le n \le 5): Not Weird৬ থেকে ২০-এর মধ্যে হলে (6 \le n \le 20): Weird২০-এর বড় হলে (n > 20): Not Weird

আরও শর্ট ও পরিষ্কার কোড (Clean & Guard Clause Approach)
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0 or (6 <= n <= 20):
        print("Weird")
    else:
        print("Not Weird")
