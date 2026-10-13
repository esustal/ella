# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star. 

for key in targets:
    print(key)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

for key, info in targets.items():
    print(key, info["Spectral Type"])

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

for key, info in targets.items():
    if info["Magnitude"] > 0.1:
        print(key, info["Magnitude"])

# 4) Look up another target, add all the necessary information to the targets list. 

targets["Alnitak"] = {
    "RA": "05h 40m 45.5s",
    "Dec": "−01° 56′ 34″",
    "Magnitude": 2.05,
    "Spectral Type": "0.97Ibe"
}

print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def declination(targets):
    ideal_star = None
    ideal_diff = 1000
    ideal_magnitude = 1000
    for (name, properties) in targets.items():
        dec_string = properties["Dec"]
        degree = int(dec_string.split("°")[0])
        diff = abs(degree - 20)
        magnitude = properties["Magnitude"]
    if diff < ideal_diff:
        ideal_star = key
        ideal_diff = diff
        ideal_magnitude = magnitude
    elif diff == ideal_diff and magnitude < ideal_magnitude:
        ideal_star = key
        ideal_magnitude = magnitude
        return(ideal_star)
    print(declination(targets))

# i genuinely don't know how we're supposed to do this, i got help from a friend

# 6) What is your favorite constellation? Orion