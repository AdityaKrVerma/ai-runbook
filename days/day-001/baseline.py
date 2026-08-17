"""
Day 001 — baseline. Written from an empty file, no AI, no lookup.
This is the measurement, not the lesson. Kept exactly as first written,
with corrections noted below.
"""

# ---------- what I wrote ----------

# func reverse_string(str):
#     return str[-1:]
#
# class Person {
#     Person() {
#         system.out.println("I am new Person");
#     }
#     void do_something() {
#         system.out.println("Person does something");
#     }

# FizzBuzz: didn't attempt — didn't know what it was.


# ---------- what was wrong ----------
#
# reverse_string:
#   - `func` is Go/Swift. Python is `def`.
#   - `str[-1:]` = "last char to the end" -> returns "o" for "hello".
#     Wanted `str[::-1]` — the third slot is the step; -1 walks backwards.
#   - Don't name a variable `str`; it shadows the builtin.
#
# Person:
#   - Constructor was CORRECT Java: same name as class, no return type.
#   - `void` on a non-returning method: also correct.
#   - `system` needs capital S -> `System.out.println`
#   - Missing closing brace on the class.
#   - `do_something` is Python naming inside Java. Java uses `doSomething`.
#   - No fields. Two behaviours, zero state — the tell of someone who has only
#     ever modified classes, never designed one.
#
# Diagnosis: not zero. Fragments of Python and Java, blended. That's the signature
# of having read a lot of code and written very little. Fixed by days 3-7.
