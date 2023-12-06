# Advent Of Code 2023
This is my repository for the annual [**Advent of Code**](https://adventofcode.com/).
</br>
 
# Notes on each day's challenge
## [Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1)
The problem considered finding digits in a string.

First part required to find the first and last digit in a line 
and create a two-digit number out of them. Second part of the problem 
was identical, but additionally 'digits' that were spelled out with letters had to be considered.

```
Part 1:
adv3nt0fc0de --> 30

Part 2:
xtwone3four  --> 24
```

## [Day 2: Cube Conundrum](https://adventofcode.com/2023/day/2)
Simple parsing problem.

For the first part, it was required to get numbers associated to 
some colors and compare them to given limits to determine if the 
combination was possible. 
In the second part the numbers of each color had to be compared against each other
to determine the largest ones for each color or each line

```
Part 1:
Limits: 12 red, 13 green, 14 blue
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red --> Possible
Game 3: 14 green, 6 blue, 20 red; 5 blue, 4 red --> Impossible

Part 2:
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green --> (R: 6,  G: 3, B: 6)
Game 5: 6 red, 1 blue, 3 green; 15 blue, 14 red         --> (R: 14, G: 3, B: 15)
```

## [Day 3: Gear Ratios](https://adventofcode.com/2023/day/3)
Problem considered finding numbers in the text and checking their neighbouring characters

First part of the problem required locating all numbers that were adjacent to a symbol.
Solution for the second part was a result of multiplication of two numbers adjacent to the same __*__ symbol  

```
Input:              Part 1:                 Part 2:
467..114..          [467, 35, 633]          467 * 35 = 16345
...*......
..35..633.
......#...
```
## [Day 4: Scratchcards](https://adventofcode.com/2023/day/4)
Simple problem about checking list content

The input signified scratch cards where on the left of the divider (__|__)
were winning numbers and on the right my numbers. 

First part of the question considered finding the amount of winning numbers for 
each card and determining amount of points won.
Each winning number would double the amount of points for a card. 
Second part introduced convoluted logic influencing amount of cards based on number of winning numbers. 
So winning two numbers would create a copy of next 2 cards. Those copies along with originals could create 
more copies of next cards... The solution to this part was total number of all cards.
```
Input:
Card 1: 41 48 83 86 17 | 83 86  6 31 18  9 48 53    --> 3 matches 
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19    --> 2 matches
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  0    --> 1 match
Card 4: 87 83 26 28 32 | 88 30 70 12 93 22 82 36    --> 0 matches

Part 1:
Card 1 --> 3 matches --> 4 points
Card 2 --> 2 matches --> 2 points
Card 3 --> 1 match   --> 1 point
Card 4 --> 0 matches --> 0 Points

Part 2:
Card id:  Number of matches:  Cards created:  Number of cards:
Card 1    --> 3 matches       --> 2, 3, 4     --> 1  
Card 2    --> 2 matches       --> 3, 4        --> 2  
Card 3    --> 1 match         --> 4           --> 4
Card 4    --> 0 matches       --> None        --> 8   
```
## [Day 5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)
Challenge was about modifying values in list of numbers based on supplied ranges.
 
Input could be considered as dictionary or a map, where instead of a simple key, 
the key was a range of numbers. Similarly, was with the value. 
Each map contained lines with 3 values: destination_category, source_category and range_length.
This is ilustrated below:
```
seeds: 79 14 55 13

seed-to-soil map:           key     -> value
50 98 2                 --> [98-99] -> [50-51]
52 50 48                --> [50-97] -> [52-99]

soil-to-fertilizer map:
0 15 37                 --> [15-51] -> [0-36]
37 52 2                 --> [52-53] -> [37-38]
39 0 15                 --> [0-14]  -> [39-53]
```

First part of the task was to determine the smallest output number 
after applying all maps to all listed seeds.
```
seeds: 79 14 55 13

Seed 79:
      └┐
Apply 79 to 'seed-to-soil map' --> 81
       ┌───────────────────────────┘
Apply 81 to 'soil-to-fertilizer map' --> 81
```
Second part was similar, but introduced a significant twist - 
seeds instead of individual values had to be considered in pairs and created ranges.
Where similarly as before with maps, first value would be a lower bound of a range
and second was the range_length:  
```
seeds: 79 14 55 13  --> seeds [79-93] [55-67]
```