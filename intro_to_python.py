# Lab V: A Gentle Introduction to Python
# Programming Essentials for Astronomy I - Python
#
# Fill in the TODOs below. Run this file (no compiling needed!) with:
#     python3 intro_to_python.py

# --- Part A: first steps ---------------------------------------------------

# Exercise 1: Hello, Universe
print("Hello, Universe!")
# TODO: also print your name and your favourite celestial object.
print("My name is Mhleli and my favourite celestial object is Saturn.")

# Exercise 2: variables and types
name = "Sirius"           # str
distance_ly = 8.6         # float
num_planets = 0           # int
naked_eye_visible = True  # bool

# TODO: print each variable together with its type, e.g.
#       print(name, "has type", type(name))
print(f"{name} has type {type(name)}")
print(f"{distance_ly} has type {type(distance_ly)}")
print(f"{num_planets} has type {type(num_planets)}")
print(f"{naked_eye_visible} has type {type(naked_eye_visible)}")
# --- Part B: arithmetic with astronomy -------------------------------------

# Exercise 3: unit conversions (1 parsec ~= 3.26 ly, 1 ly ~= 9.46e12 km)
# TODO: convert distance_ly to parsecs and to kilometres, and print both
#       using f-strings.
print(f"distance_ly in parsecs is {distance_ly/3.26:.2f}, and in kilometres is {distance_ly*9.46e12:.2e}")

# Exercise 4: we see the past
# TODO: print the year the light we see now left Sirius (use 2026 as "now").
print(f"light left sirius in the year {2026 - 8.6:.1f}, years ago")
# TODO: print 8.6 / 3 and 8 // 3 and notice the difference.
print(f"8.6 / 3 = {8.6 / 3:.2f}, and 8 // 3 = {8 // 3}")
pi = 3.14159
radius_km = 696_340
volume = (4/3) * math.pi * radius_km ** 3
print(f"Volume of the Sun is {volume:.3e} km^3")
# --- Part C: talking to the user -------------------------------------------

# Exercise 6: reading input
# NOTE: input() returns TEXT -- convert it with float(...) before doing maths.
# Uncomment the two lines below once you are ready to try it:
text = input("Enter a distance in light-years: ")
print(f"That is {float(text) / 3.26:.2f} parsecs.")


# --- Optional extension ----------------------------------------------------
import  math
# TODO: distance modulus  mu = 5 * math.log10(d) - 5  for d in parsecs.
distance_modulus_mu = 5 * math.log10(distance_ly / 3.26) - 5
print(f"Distance modulus (mu) for {distance_ly} light-years is {distance_modulus_mu:.2f}")

