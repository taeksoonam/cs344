%A)	From LPN!
%	Exercise 1.4 - Explain why you built the representations as you did.

%	i) Butch is a killer.
		killer(Butch). 
			%fact
%	ii) Mia and Marsellus are married.
		married(Mia,Marsellus). 
			%fact
%	iii) Zed is dead.
		dead(Zed). 
			%fact
%	iv) Marsellus kills everyone who gives Mia a footmassage.
		kills(Marsellus,X):- footmassage(X,Mia).
			%If anyone gives a footmassage to Mia, that Marsellus kills that person
%	v) Mia loves everyone who is a good dancer.
		loves(Mia,X):- dances(X)
			%This rule explains if people in good dance, it means they are good dancers, and therefore Mia loves them since they are good dancers.
%	vi) Jules eats anything that is nutritious or tasty.
		eats(Jules):-
			nutritious(X);
			tasty(X).
				%semicolon represents 'or'

%	Exercise 1.5 - Explain how Prolog comes up with its answers.

%   wizard(ron). 
%   hasWand(harry). 
%   quidditchPlayer(harry). 
%   wizard(X):-  hasBroom(X),  hasWand(X). 
%   hasBroom(X):-  quidditchPlayer(X).

%	i) wizard(ron). - true
%	ii) witch(ron). - undefined procedure
%	iii) wizard(hermione). false
%	iv) witch(hermione). - undefined procedure
%	v) wizard(harry). true
%	vi) wizard(Y). Y = ron, Y = harry
%	vii) witch(Y). underfind procedure


%B) Consider the well-known modus ponens. Does Prolog implement a version of modus ponens in propositional logic form? 
%	 If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?
	%p -> q.
	%This is supposed to mean if p, then q. This is the well-known modus ponens. Prolog also implements a version of modus ponens in such way, except in a different syntax.
	%In the guide, we had an example of 'listens2Music(yolanda):-  happy(yolanda).' This means if yolanda is happy, yoland listens to music. 
	%We can also say yolanda listes to music because she is happy.


%C) Prolog supports representations in the form of Horn clauses. Compare and contrast the representational power they provide with that of propositional logic.
	While the horn clause at least has to contain one positive literal, any program in prolog puts emphasis more on the logic being true or not.

%D) Logical implementations generally distinguish the basic operations of TELL and ASK. Does Prolog support this distinction? If so, how; if not, why not?

%   	A Horn clause is a clause with at most one positive literal. Prolog is built on top of horn clauses. The horn clauses in prolog are used for implications. 

% 4. Logical implementations generally distinguish the basic operations of TELL and ASK. 
%    Does Prolog support this distinction? If so, how; if not, why not?

	 %Yes, it does.
	 %Let's use the example above.
	 %In Prolog, TELL operation can be used as 'wizard(X)', which will tell us who is the wizard.
	 %In Prolog, ASK operation can be used as '?- wizard(Ron)', which asks whether Ron is a wizard, and the answer will either be true or false.