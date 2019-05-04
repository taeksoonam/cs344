% Taek Soo Nam CS344

%A)
	%i)
		directlyIn(katarina, olga).
		directlyIn(olga, natasha).
		directlyIn(natasha, irina).
		in(X, Y) :- directlyIn(X, Y).
		in(X, Y) :- directlyIn(X, Z), in(Z, Y).

	%ii)

		tran(eins, one).
		tran(zwei, two).
		tran(drei, three).
		tran(vier, four).
		tran(fuenf, five).
		tran(sechs, six).
		tran(sieben, seven).
		tran(acht, eight).
		tran(neun, nine).

		%Base Case
		trantran ([], []).

		%Actual Case
		trantran([X|Y], [A|B]) :-
			tran(X, A),
			trantran(Y, B).


%B)

% Yes, in class we have demonstrated how modus ponens. In prolog, use the generalized modus ponens.
% The example in class is implemented in prolog version below:

	%modus ponens:
		% p -> q
		% p
		% therefore q
 
 	%Prolog:
		q :- p. 
		p.
		?- q. 

