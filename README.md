# MMA Rank

## Overview
https://mmastats.ca/

- A website that displays the elo rating of every UFC MMA fighter.  
- All data is taken from [ufcstats.com](http://www.ufcstats.com/statistics/events/completed).
- Includes every UFC main event and Fight Night.

Petite-Vue used for reactivity, Firebase used for hosting.

## Ranking System

### Data Collection

The MMA Rank algorithm uses data from [ufcstats.com](http://www.ufcstats.com/statistics/events/completed). Stats from other MMA organizations are not included. Unofficial UFC fights <i>(such as Dana White's Contender Series)</i>, and fights from other UFC owned organizations <i>(such as Strikeforce and PRIDE)</i>, are not included.

Only the events listed in the link above are used in this dataset <i>(every UFC main event and Fight Night)</i>.

### Ranking Algorithm

The rating for a new fighter is 1000 points.

The ranking algorithm is an ELO system with a maximum single match rating gain of 64. This value was chosen over the more common value of 32 in order to produce a larger rating disparity over a smaller sample size.
    
The winner of a match will gain the same number of points as the loser will lose. The amount of points won and lost in a match is calculated based on the likelihood of victory or defeat. 

Fighters will gain many points for beating higher ranked opponents, and gain relatively few points for beating lower ranked opponents. Inversely, fighters will lose more points for losing to lower ranked opponents, and lose less points for losing to higher ranked opponents.

Only fighters with 3 or more matches in a division will be ranked in that division. A fighter's rating will carry over across weight classes. This means that each fighter has a single rating, which is affected by all matches across weight classes. 

### Known Biases

1. #### Limited Dataset

    Likely the most impactful bias of this algorithm is that the dataset only contains UFC fights. Many high level UFC fighters had impressive careers in other organizations prior to the UFC, which will not be reflected in the rankings. Fighters that are stronger than their rating may suggest will impact the ratings of their opponents, who will win less or lose more than they should, if the 'true rating' of their opponent was taken into account. 

    The scope of data collection may expand in the future.

2. #### Bias Towards Current Fighters

    The nature of a zero-sum system means that the rankings will always be biased towards fighters currently at their peak. Many fighters had higher peak rankings, but now place lower in the rankings due to late career losses.
            
    Many active fighters with lower peak ranks are very high on the rankings. This is the result of an ELO system that punishes losing as much as it rewards winning. Fighters with less ambitious careers are likely to be overrated by this system.

3. #### Limited Sample Size

    One problem with an MMA ranking system (as compared to tennis or chess), is the relative lack of matches from competetors. In the FIDE chess ranking system, players must play at least 5 matches before they can be ranked. In the UFC, many fighters are signed and cut before reaching this point.
            
    Where this bias is most apparent is near the bottom of the ranking system. The lowest rated fighters are likely not the weakest in the UFC, but rather, they are the fighters that were good enough to accumulate many losses. Fighters with only a few matches are likely not rated accurately. 






        
