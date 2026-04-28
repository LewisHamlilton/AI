male(aditya).
male(gourish).
male(kirtikumar).
male(amrut).
male(durgadas).
male(rakshad).
male(chatya).

female(anjali).
female(prafula).
female(trupti).
female(arpita).
female(aditi).
female(anjana).
female(madhvi).

father(gourish, aditya).
father(gourish, aditi).
father(kirtikumar, arpita).
father(chatya, rakshad).
father(amrut, gourish).
father(amrut, trupti).
father(durgadas, anjali).
father(durgadas, anjana).

mother(anjali, aditya).
mother(anjali, aditi).
mother(trupti, arpita).
mother(anjana, rakshad).
mother(prafula, gourish).
mother(prafula, trupti).
mother(madhvi, anjali).
mother(madhvi, anjana).

parent(F, M, C) :-
    father(F, C),
    mother(M, C).

grandfather(GF, C) :-
    ( father(GF, F), father(F, C)
    ; father(GF, M), mother(M, C)
    ).

grandmother(GM, C) :-
    ( mother(GM, F), father(F, C)
    ; mother(GM, M), mother(M, C)
    ).

brother(B, C) :-
    father(F, B), father(F, C),
    mother(M, B), mother(M, C),
    male(B),
    B \= C.

sister(S, C) :-
    father(F, S), father(F, C),
    mother(M, S), mother(M, C),
    female(S),
    S \= C.

siblings(X, Y) :-
    father(F, X), father(F, Y),
    mother(M, X), mother(M, Y),
    X \= Y.

uncle(U, C) :-
    ( father(F, C), brother(U, F)
    ; mother(M, C), brother(U, M)
    ).

aunt(A, C) :-
    ( father(F, C), sister(A, F)
    ; mother(M, C), sister(A, M)
    ).

cousin(X, Y) :- (father(P1, X); mother(P1, X)), 
                (father(P2, Y); mother(P2, Y)), 
                siblings(P1, P2).
