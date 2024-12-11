# Edabit_Challenges
Challenges from Edabit site.  <br>
Basically the whole point of this repo is that I do Edabit challenges at a certain difficulty until I get bored with the difficulty, when this happens I move to more difficult challenges.
# Medium difficulty
## Finding Adjacent Nodes
link: https://edabit.com/challenge/3DAkZHv2LZjgqWbvW  <br>
Given an adjacency matrix a function checkAdjacency was written.  <br>
Considering this turned out to be a one-liner let's move on to a higher difficulty.
# Hard
## Imaginary Coding Interview
link: https://edabit.com/challenge/3A3mHS5B3NNZddQL2  <br>
There were 2 ways to complete it, one was to obviously use 3 if statement to check pairs of list elements, the other approach was to define a sequence and use a for loop to check the whole list with a single if statement.
## Encode Morse
link: https://edabit.com/challenge/5bYXQfpyoithnQisa <br>
A simple for loop and dictionary accessing by key, a slightly trickier part with inverting the dictionary and replacing list elements, slightly more enjoyable than previous but I'll consider to increase the difficulty after 3 or so more challenges.
## Find Domain Name From DNS Pointer (PTR) Records Using IP Address
link: https://edabit.com/challenge/MtktG9Dz7z9vBCFYM <br>
By using gethostbyaddr() function of the socket module this was pretty straight forward.
## The Snake — Area Filling
link: https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt <br>
Just checking if the snake still fits in the map.
# Very Hard
## Atbash Cipher
link: https://edabit.com/challenge/MGALfBAXhXqqdFyqo <br>
Because it was requested that the capitalisation was to be retained the set of alphabet in lowercase and uppercase was created, from then a certain shifting did all the work.
## Concert Seats
link: https://edabit.com/challenge/xbjDMxzpFcsAWKp97 <br>
List comprehension was used here, checking 2 rows at the same time function returns False if the conditions are not fulfilled anymore, thus reducing the time complexity of the algorithm.
## Identity Matrix
link: https://edabit.com/challenge/QN4RMpAnktNvMCWwg <br>
Once again list comprehension was used to reduce the amount of writing. <br>
Setting up a function that 'inverts' the counter, with the domain of natural numbers and codomain in integers was the trickiest part, however a student after a course in logic, set theory and mathematical analysis should have no difficulties in constructing that.
## Recursion: Happy Number
link: https://edabit.com/challenge/J9fCHDa3yYJWnK3A7 <br>
Quite simple recursion problem. Luckily conversion between ints and strings in python feels like it was designed to handle such problems with ease.
## Party People Part I: Make it Recursive
link: https://edabit.com/challenge/EuHGfJfCeLyx9BEdG <br>
Another recursion problem, the solution was to remove the elements that are bigger than the length of the list and call the function again, function ends when there are no elements to be removed returning the length of the list.
## Staircase
link: https://edabit.com/challenge/YqLBEZJR9ySndYQpH <br>
I could've used an if statement but who does that when you can define a natural number sequence that sorts it out for you.
## Prison Break
link: https://edabit.com/challenge/SHdu4GwBQehhDm4xT <br>
We're simply stripping the list of leftmost 1s and then inverting the values of the remainder just like the challenge asked.
## 