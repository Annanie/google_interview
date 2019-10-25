def replace20(s):
    return "%20".join(s.split(" "))

test_dict = {
    "Ab cd" : "Ab%20cd",			#general case
    "Abcd" : "Abcd",
    "" : "",
    "Ab  cd" : "Ab%20%20cd"
}

for test, result in test_dict.items():
    print(f"For {test} answer is {result == replace20(test)}")
