# MMA Stats

## Overview
https://mma-stats-38214.web.app/

- A website that displays an elo rating of UFC mixed martial arts fighters.  
- All data is taken from [ufcstats.com](http://www.ufcstats.com/statistics/events/completed).
- Includes every UFC main event and Fight Night.

Petite-Vue is used for reactivity, Firebase is used for hosting.

## Ranking System

### Data Collection

The MMA Rank algorithm currently only uses fights from [ufcstats.com](http://www.ufcstats.com/statistics/events/completed). Stats from other MMA organizations are not included. Unofficial UFC fights <i>(such as Dana White's Contender Series)</i>, and fights from UFC purchased organizations <i>(such as Strikeforce and PRIDE)</i>, are also not included.

Only the events listed in the link above are used in this dataset <i>(every UFC main event and Fight Night)</i>.

### Ranking Algorithm

The initial rating for a new fighter is 1000 points.

The ranking algorithm is an ELO system with a maximum single match rating gain of 64. This value was chosen over the more common value of 32 due to the smaller sample size in MMA, as compared to chess or tennis.
    
An ELO system is zero-sum, meaning that the winner of a match will gain the same number of points as the loser will lose. The amount of points won and lost in a match is calculated based on the likelihood of victory or defeat. 

Put simply, fighters will gain many points for beating higher ranked opponents, and gain relatively few points for beating lower ranked opponents. The inverse is also true. Fighters will lose more points for losing to lower ranked opponents, and lose less points for losing to 
higher ranked opponents.

Only fighters with 3 or more matches in a division will be ranked in that division. A fighter's rating will carry over across weight classes. This means that each fighter has only a single rating, which is affected by all matches across weight classes. 

### Known Biases

1. #### Limited Dataset

    Likely the most impactful bias of this algorithm is that the dataset only contains UFC fights. Many high level UFC fighters had impressive careers in other organizations, which will not be reflected in the rankings. In addition, fighters that are stronger than their rating may suggest will also have an impact on the rating of higher rated opponents that they match against. 

    There are plans to expand this dataset in the future, however currently this remains a large bias impacting the results of the rankings.

2. #### Bias Towards Current Fighters

    The nature of a zero-sum system means that the rankings will always be biased towards fighters at their peak. Many would consider Anderson Silva one of the greatest MMA fighters of all time. However, he is nowhere near the top of the rankings due to many losses at the end of his career.
            
    By contrast, many current fighters with less impressive peak ranks are very high on the rankings. This is the eb-and-flow of an ELO system that punishes losing as much as it rewards winning. Fighters with less ambitious careers may be overrated due to a lack of losses.

3. #### Limited Sample Size

    One problem with an MMA ranking system (as compared to tennis or chess), is the relative lack of matches from competetors. In the FIDE chess ranking system, players must have at least 5 matches before they can be ranked. In the UFC, many fighters are signed and cut before even reaching this point.
            
    Where this bias is most apparent is near the bottom of this ranking system. The practice, the lowest rated fighters are not the weakest in the UFC, but rather, the fighters that were good enough to accumulate many losses. Many fighters have 2-3 matches, lose all of them, and are immediately cut. These are likely the weakest fighters in the UFC, however the sample size of fights is too low for their rating to reflect their true skill. 
        








        