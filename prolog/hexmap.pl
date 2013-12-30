% A description of a hex map based on rules
% :- module('hexmap', [moveone/3]).

% a hex vector (HX, HY)
hx(HX, (HX, _)).
hy(HY, (_, HY)).

origin((0, 0)).
unit((0, -1), 0).
unit((1, 0), 1).
unit((1, 1), 2).
unit((0, 1), 3).
unit((-1, 0), 4).
unit((-1, -1), 5).
unit(HV, N) :- (N < 0 ; N > 5), N1 is N mod 6, unit(HV, N1).

addvector(Result, HV0, HV1) :-
        hx(HX0, HV0),
        hy(HY0, HV0),
        hx(HX1, HV1),
        hy(HY0, HV1),
        Result is (HX0 + HX1, HY0 + HY1).

subvector(Result, HV0, HV1) :-
        hx(HX0, HV0),
        hy(HY0, HV0),
        hx(HX1, HV1),
        hy(HY0, HV1),
        Result is (HX0 - HX1, HY0 - HY1).
        

% movement a single step
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
moveone(NEW, NOW, 0) :- NEW is (hx(HX, NOW), hy(HY, NOW) - 1).
#moveone([HX, HY], [CX, CY], 0) :- HX is CX, HY is CY -1.
#moveone([HX, HY], [CX, CY], 1) :- HX is CX + 1, HY is CY.
#moveone([HX, HY], [CX, CY], 2) :- HX is CX + 1, HY is CY + 1.
#moveone([HX, HY], [CX, CY], 3) :- HX is CX, HY is CY + 1.
#moveone([HX, HY], [CX, CY], 4) :- HX is CX - 1, HY is CY.
#moveone([HX, HY], [CX, CY], 5) :- HX is CX - 1, HY is CY -1.
#moveone([HX, HY], [CX, CY], N) :- 
#        N > 5 ; N < 0,
#        N1 is N mod 6,
#        moveone([HX, HY], [CX, CY], N1).


ybias(YBias, HX) :- 
        HX >= 0,
        YBias is HX // 2.

ybias(YBias, HX) :-
        HX < 0,
        YBias is //(-(HX, 1), 2).
