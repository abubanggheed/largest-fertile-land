# Introduction
This is the largest fertile land problem posted by Tushar Santoki on hackerrank:
https://www.hackerrank.com/contests/codestar-long-programming-contest/challenges/largest-fertile-land

The challenge is as follows:
- You are given a really long string as an input.
- Some of that string is a rectangular plot of land that has fertile and baren patches.
- The rest of the string is instructions on what the output should be.

## The concept
This repository has a mechanism for calculating the largest rectangle of fertile land contained within any rectangluar plot of land with fertile and baren patches. The instructions say that the answer should contain the areas of fertile patches in subrectangles within the entire plot of land. The number of areas depends on how many subrectangles are requested in the input string.

## Input format
The inputs for this problem are as follows:
 - N M
 - (string with N lines each line has M characters)
 - Q
 - a b (1)
 - a b (2)
 - ...
 - a b (Q)

Here N and M indicates the size of the plot of land.
Q is the number of subplots to be evaluated.
a and b are integers between 1 and N, they indicate the rows of the plot that are within that particular subplot.

## Output Format
The outputs for this problem should look like this:
 - c (1)
 - c (2)
 - ...
 - c (Q)

Each c is the area of the largest rectangle of fertile land within the subplot specified by the input.

## Repository Guide
The algorithm for finding the largest rectangle of fertile land within a rectangular plot of land is found in calculate_land.py
The setup for taking in the input, and sending back the output is found in largest_fertile_land.py.

## Setup
This repository uses no libraries asside from the default libraries in python. However, it is incompatible with versions of python older than 3.