#!/usr/bin/python

# Test symbols redefined/missing

# Github issue: #61
# Author: Nguyen Anh Quynh

from keystone import *

import regress

class TestSymbols(regress.RegressTest):
    def runTest(self):
        # Initialize Keystone engine
        ks = Ks(KS_ARCH_X86, KS_MODE_32)

        try:
            encoding, count = ks.asm(b"_label:; nop; _label:")
        except KsError as e:
            if e.errno != KS_ERR_ASM_SYMBOL_REDEFINED:
                self.assertFalse(1, f"ERROR: {e}")

        try:
            encoding, count = ks.asm(b"mov eax, eflags")
        except KsError as e:
            if e.errno != KS_ERR_ASM_SYMBOL_MISSING:
                self.assertFalse(1, f"ERROR: {e}")


if __name__ == '__main__':
    regress.main()
