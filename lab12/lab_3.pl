%Create a Prolog program that implements the ridiculous inferences used by 
%Sir Bedevere (Terry Jones) to justify the burning of the witch (Connie Booth) 
%in Monte Python's Holy Grail. 
%Load your rules and demonstrate that the woman is indeed a witch.


%Rules:
%burn witches.
%witches are made of wood.
%wood floats.
%duck floats.
%if weighs similar to duck, she floats, acts like a wood, so witch, so burn.

%witch(X)
%burn(wood)
%burn(witch)
%wood(witch)
%float(wood)
%float(duck)
%similarweight(X,duck)

%if X is witch, X can be burned
witch(X) :- burn(X)

%if X can be burned, X is wood
burn(X) :- wood(X)

%if she is witch, she can float(witch is made of wood and wood can float)
witch(X) :- float(wood)

%if she can float, she has simliar weight to duck
float(X) :- similarweight(X, duck)

%she has similarweight
similarweight(X,duck)

%So burn her

