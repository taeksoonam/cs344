%Read LPN! Chapter 2 and do the following exercises:

	%A)From LPN!
		%i)Exercise 2.1, questions 1, 2, 8, 9, 14 - Give the necessary instantiations.
			%1) unifies
				
			%2) doesn't unify - it is case-sensitive

			%8) unifies

			%9) unifies

			%14) doesn't unify - assigning same variable to different constants
		%ii)Exercise 2.2 - Explain how Prolog does its unification and reasoning. If you have issues getting the results you’d expect, are there things you can do to game the system?
			%number 2 and 3 will not work, since we did not specify wizard(harry) and magic(wizard).
			%In Prolog, unification and reasoning work by evaluating whether two clauses/terms can become equal. 
			%If they are equal, they unify and connect them together according to the element's equality.


	%B)Does inference in propositional logic use unification? Why or why not?
		%No, it doesn't. Because when p -> q, and if it is p, it's q. This itself is considered as inference.
		%However, in unification of Prolog, the terms/numbers/values have to be equal, which does not use inference.

	%C)Does Prolog inferencing use resolution? Why or why not?
		%Yes, it does. We can exemplify such as:

		cs344 :- AI.

		csMajorRequirements :- cs108, cs112, cs344.

		Then, we can use inference like: csMajorRequirements :- cs108, cs,112, AI.

		Resource: https://athena.ecs.csus.edu/~logicp/unification-resolution.html
