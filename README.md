This repository contains all the code which I have contributed to Kivy's sister project Plyer during my 3 month GSoC internship.

My work in Plyer includes the designing and implementation of platform independent APIs. Target platforms are Android, iOS, Linux, Windows, Mac OS X.

I have also contributed some of the code to projects Pyjnius and Pyobjus.

In Pyjnius, if we need to override a JAVA method then we have to provide signature of that method to Pyjnius's property `java_method`. I made a pull request on documenting the step wise procedure for finding signature of Android methods.

In Pyobjus, for implementing any sensor, we need to make a bridge in pyobjus since that part of code cannot be converted from Objective C to python. So I needed to add some Objective C code for implementation of sensors in Plyer.

I have shared links of all my contributions below.

[Pyjnius Contributions](https://github.com/kivy/pyjnius/pulls/malverick)

[Pyobjus Contributions](https://github.com/kivy/pyobjus/pulls?q=is%3Apr+author%3Amalverick)

[Plyer Contributions](https://github.com/kivy/plyer/pulls?utf8=✓&q=is%3Apr%20author%3Amalverick%20)
