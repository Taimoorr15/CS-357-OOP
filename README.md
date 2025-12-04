# Hidden-Constructor-in-python-
The question is, does python have a hidden constructor???
We know that java and C++ have hidden constructors but is that the case in python as well??
Well, the answer is yess. Pyhton does have a hidden constructor which is written before your __init__() constructor.
The constructor is __new__() which is present before the __init__() constructor but it remains hidden
Therefore we only see the __init__() constructor
