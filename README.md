This package shows how to compute the sum of some very strange convergent series.

The harmonic series 1/1 + 1/2 + 1/3 + ... + 1/n + ... diverges. This means that the sum can be made as large as desired by adding enough terms.

Suppose we delete from this series all terms with a "9" in the denominator. That is, we remove 1/9, 1/19, 1/29, etc. Then the remaining series converges to a sum less than 80. This very surprising result was proved by A. J. Kempner in 1914.

We also get convergent series if we pick any other digit string (say, "314159") and compute the sum of 1/n where n contains no "314159".

Unfortunately, these series converge so slowly that it is impossible to compute their sums simply by adding up terms. A more sophisticated algorithm is required. As a result, this computational problem has attracted much interest over the years.

The article, "Summing a Curious, Slowly Convergent Series" by Thomas Schmelzer and Robert Baillie in the American Mathematical Monthly, vol. 115, pages 525-540 (June/July 2008) has an algorithm that computes sums of these and related series quickly, and to high precision.

This Mathematica package implements the algorithm in that article.

The sum of the "no 9" series is about 22.920676619264150. The sum of the series where the denominators contain no "314159" is about 2302582.333863782607892.
