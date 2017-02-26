# CatanAnalysis [IN PROGRESS]
A Statistical Analysis of The Settlers of Catan Boardgame

## Aim
The aim of this project is to automate gameplay of The Settlers of Catan and hopefully decide which strategies lead to the highest probablity of winning.  

Some questions to answer:
* What is the best position to begin placing settlements in?
* Where is the best position to place your settlements in at the begining?
* Under what circumstances is largest army a better goal than longest road?
* When should you build on a harbor?
* Trading?

In the least, I hope to make the program represent the boardgame as closely as possible (some aspects will be very difficult and probably will be ignored) and allow for 3 to 4 players to play by their own set of algorithmic strategies.

## Running It
```python main.py [-v]```  
[-h] - help  
[-v] - verbose  

## So far
* It generates random boards with harbors and without adjacent 6's and 8's.  
* Has 3 to 4 players randomly place their initial settlements with respect to the distance rule.  
* Dice are rolled and player recieve their appropriate cards.  

^ are vacant positions

Resource and number are paired together at hex center  
* D: Desert  
* B: Brick  
* G: Grain  
* O: Ore  
* S: Sheep (a.k.a. wool)  
* W: Wood (a.k.a lumber)  

3,g,s,w,b,o are harbors

Sample Board:  
```
                   ^          3^           ^
             ^          3^           ^           ^

                  11O         04G         10O

            b^           ^           ^          o^
      b^           ^           ^           ^          o^

            11B         03W         06G         03B

       ^           ^           ^           ^           ^
3^           ^           ^           ^           ^           ^

      08W         08S         04B         06G         09S

3^           ^           ^           ^           ^           ^
      s^           ^           ^           ^          w^

            05W         12G         05W         10S

      s^           ^           ^           ^          w^
             ^           ^           ^           ^

                  09S          D          02O

            3^          g^           ^          3^
                  3^          g^          3^
```                 
