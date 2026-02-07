#!/usr/bin/env python
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from aca.codehelper import lint_code, analyze_code, suggest_improvements, explain_and_improve

# Test 1: Lint
code1 = "x = 1; y = 2; print(x)"
print("=== TEST 1: LINT ===")
print(lint_code(code1))

# Test 2: Analyze
code2 = "def foo():\n    pass\nclass Bar:\n    pass"
print("\n=== TEST 2: ANALYZE ===")
print(analyze_code(code2))

# Test 3: Suggestions
code3 = "def calculate(a, b):\n    result = a + b\n    print(result)"
print("\n=== TEST 3: SUGGESTIONS ===")
print(suggest_improvements(code3))

# Test 4: Full review
code4 = "for i in range(100):\n    print(i)"
print("\n=== TEST 4: REVIEW ===")
print(explain_and_improve(code4))
