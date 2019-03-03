#!/usr/bin/python3
# AUTHOR: lamhaoyin
# I18N & Optimize: pan93412

import argparse
import gettext

'''
Set up gettext

Gettext is a tool to let program translatable.
'''
gettext.bindtextdomain("fastfib", "locale")
gettext.textdomain("fastfib")
_ = gettext.gettext

'''
Set up argparse
'''
arg = argparse.ArgumentParser(
  description=_("This program is used to calculate Fibonacci number."),
  epilog=_("Please report any bugs to <https://github.com/lamhaoyin/Fibonacci_FAST>"),
)

arg.add_argument(
  "num",
  action="store",
  help=_("the N value of F(N)."),
  type=int
)

arg.add_argument(
  "-v",
  action="store_true",
  help=_("Verbose mode"),
  required=False
)

argv = arg.parse_args()

def matrix(A, B) :
    C = [A[0] * B[0] + A[2] * B[1], A[1] * B[0] + A[3] * B[1], A[0] * B[2] + A[2] * B[3], A[1] * B[2] + A[3] * B[3]]
    return C

ANS = [1, 0, 0, 1]
TMP = [1, 1, 1, 0]

N = argv.num
NInit = str(N)

if argv.v: print(_("[I] Start process: %s") % (NInit))

while N > 0 :
    if N % 2 == 1 :
        ANS = matrix(ANS, TMP)
    TMP = matrix(TMP, TMP)
    N = N // 2
    if argv.v: print("\r" + _("[I] Now process: %d") % (N), end=" "*len(NInit), flush=True)

if argv.v: print()
print(_("[I] Done. F(n) is:\n%d") % (ANS[1]))
