# sudoku-genetic
## AI course 2nd assignment
A genetic algorithm solver for sudoku

As sudoku contains a lot of local optimums, the following features were impelimented in hope to avoid them:

1. Uniform mutations: It increases diversity to avoid local minimums.
2. Ranking selection: Even though it's computationaly expensive and slow converging but helps with local minimums.
3. A high rate of mutation helps with not getting stuck in local minimums.
4. A very small mutation helps by increasing the domain of global optimum meaning a decrease in number of random restarts.
5. We keep the good parents to avoid premature covergence.

* I also tried to impeliment a 2D format but it was unnecessarily slow. 