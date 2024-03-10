# Finite State Automaton Implementation

This project is an implementation of a finite state automaton (FSA) in Python. The code reads state transitions and input strings from a file ("automat.in") and determines whether the input string is accepted by the automaton. The FSA is stored in a dictionary of dictionaries, where each state is mapped to a dictionary containing the transitions for each input symbol.

## Description:

The finite state automaton is a fundamental concept in computer science and is widely used in various applications such as pattern matching, lexical analysis, and parsing. This implementation reads the FSA description from a file and simulates its behavior to determine whether a given input string is accepted by the automaton.

## Usage:

To use the program, follow these steps:

1. Create a file named "automat.in" containing the description of the finite state automaton.
2. On the first line of the file, specify the final states separated by spaces.
3. On subsequent lines, specify the transitions in the format "current_state input_symbol next_state" separated by spaces.
4. Run the Python script, and it will prompt you to enter an input string.
5. The script will then determine whether the input string is accepted by the finite state automaton and display the paths that lead to accepting states.

## Example:

Suppose the "automat.in" file contains the following description:
q1 q2
q1 a q2
q2 b q1

And the input string provided is "abab".

The script will output:
Drumul numarul 1:
q1->q2->q1->q2

Drumul numarul 2:
q1->q2->q1->q2

indicating that the input string is accepted, and there are two paths that lead to an accepting state.

