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
Similarly as before with maps, first value would be a lower bound of a range
and second was the range_length:  
```
seeds: 79 14 55 13  --> seeds [79-93] [55-67]
```
## [Day 6: Wait For It](https://adventofcode.com/2023/day/6)
Simple problem about finding a smallest number in a range that fulfills requirement

Challenge introduced idea of toy boat races where the button on a boat had to be pressed for
*x* amount of time, for the boat to travel with speed of *x*. Input showed the required time
to complete a race and the distance that needs to be beaten. 
```
Time:      7  15   30
Distance:  9  40  200
```
Part one required to determine number of ways that each race can be beaten. 
For example first race could be won in 4 ways:
```
Hold button time    Total distance    Race won
0                   0                 False
1                   6                 False
2                   10                True
3                   12                True
4                   12                True
5                   10                True
6                   6                 False
7                   0                 False

-----------------------> True = 4, False = 4
```
Second part removed whitespaces between numbers converting it to one
long race. Surprisingly, my naive approach used for part 1 was still feasible,
and returns the answer in about 10s. However, by using interval search approach, 
it is possible to get the process with O(log(n)) time complexity.

Sample race for part two: 
```
Time:      71530
Distance:  940200

-> Shortest button hold time to win is 14
-> Longest is 71516
---> Since all hold times beteeen shortest and longest time will result in win
     it gives 71503 ways of winning  
```
## [Day 7: Camel Cards](https://adventofcode.com/2023/day/7)
Sorting problem based on poker-hand class

This challenge involved reading input as hands of cards. The goal was to sort 
hands from weakest to strongest based on poker formations and then returning
the bid multiplied by hand's rank (position after sorting).
```
Card  Bid --> Rank --> Winning
32T3K 765     1        765 
T55J5 684     4        2736
KK677 28      3        84
KTJJT 220     2        440
QQQJA 483     5        2415

---> Sum of winnings: 6440
```
Second part introduced new rule in form of replacing Jack with Joker. Rule stated 
that Joker acts like a wildcard when it comes to determining formation,
but has the lowest numerical value. This meant that *JKKT9* was weaker than *KK6TT* in first part 
(*one pair* vs *two pairs*) but in part two it was considered as stronger hand 
because *J* acts like *K* making it *three-of-a-kind*. However, hand *JJJJJ* is weaker than *22222*
because *J* has lower numerical value than *2*.

## [Day 8: Haunted Wasteland](https://adventofcode.com/2023/day/8)
Directed graph traversal problem

This challenge's input represents the structure of the directed graph, 
where from each node traversal is possible to only two others. First line
of the input determined which of these nodes should be chosen as next one to move to
(*L* means the first of the two, and *R* the second) 
and worked like circular list so used direction is moved to the end.
```
LRLR

AAA = (CCB, XXX)
CCB = (XXX, ZZZ)
ZZZ = (CCB, XXX)
DDA = (DDB, XXX)
DDB = (DDC, DDC)
DDC = (DDZ, DDZ)
DDZ = (DDB, DDB)
XXX = (XXX, XXX)
```
Part one required to find the number of steps required to get from node *AAA* to *ZZZ*.
```
Current node  Directions list  Direction  Options     Next node
AAA           [LRLR]           L          (CCB, XXX)  CCB
CCB           [RLRL]           R          (XXX, ZZZ)  ZZZ
ZZZ           [LRLR]           L          (CCB, XXX)  ---

---> Number of steps: 2             
```
Second part increased the difficulty by changing the way starting and nodes are determined.
For this, each node ending with *A* was a starting position and each ending with *Z* was final node.
Now, simultaneously starting as each starting position each path needed to end at the same time.
```
Step  Current nodes  Direction  Options     Next node

1     AAA            L          (CCB, XXX)  CCB
      DDA            L          (DDB, XXX)  DDB
      
2     CCB            R          (XXX, ZZZ)  ZZZ ┬─ only one final pos.
      DDB            R          (DDC, DDC)  DDC ┘  --> continue
      
3     ZZZ            L          (CCB, XXX)  CCB ┬─ only one final pos.
      DDC            L          (DDZ, DDZ)  DDZ ┘  --> continue   
....
6     CCB            R          (XXX, ZZZ)  ZZZ ┬─ both final positions
      DDC            R          (DDZ, DDZ)  DDZ ┘  --> finish  

---> Number of steps: 6 
```
The naive solution for finding number of steps by simply counting them until
final positions would take to much time. However, the input was constructed in
such a way that nodes ending with 'Z' when searching to next finish node loop back to themselves.
Additionally, it takes them the same number of steps that 
starting nodes (ending with 'A') need to get to them.
```
CCA --> CCZ (2 steps) & CCZ --> next '..Z' = CCZ (2 steps)
DDA --> DDZ (3 steps) & DDZ --> next '..Z' = DDZ (3 steps)
```
Because of that, the answer for this part is the *least common multiplier*
of all numbers of steps.

## [Day 9: Mirage Maintenance](https://adventofcode.com/2023/day/9)
Simple problem involving lists recursively creating new lists

The problem required to predict the next value from a sequence of numbers.
To do this, it was needed to find differences between each adjacent value in a list and 
by doing so, create a new list. Recursively continue the process until the resulting list 
consists only of *0*s. Then *0* is added to the list and by climbing up the lists next value is 
predicted by adding last item of the list to the last item of the list below.

Input consisted of multiple lines of numbers, here is the example for one of them:
```
Line: 10 13 16 21 30 45
  
10  13  16  21  30  45 ────────────┬─> 68 (23 + 45)
   3   3   5   9  15 ──────────┬─> 23 (8 + 15)
     0   2   4   6 ────────┬─> 8 (2 + 6)
       2   2   2 ──────┬─> 2 (0 + 2)
         0   0 ──> add 0
         
--> Predicted value: 68
```
Part two of the problem was very similar to part one, with the only difference
that the extrapolated was done backwards. This could be done by modifying algorithm
from part one to take first value instead of the last one and subtract first value from the list below.
```
Line: 10 13 16 21 30 45

(10 - 5) 5 <─┬──────── 10  13  16  21  30  45
  (3 - (-2)) 5 <─┬────── 3   3   5   9  15
        (0 - 2) -2 <─┬──── 0   2   4   6
             (2 - 0) 2 <─┬── 2   2   2
                     add 0 <── 0   0

--> Predicted value: 5
```
Alternatively, solution for part two could be achieved by mirroring the original list and simply using 
algorithm from part one.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```