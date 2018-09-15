#!/usr/bin/env python
from athstmt import *
from athinterpreter import TildeAthInterp

stmts = AthStatementList([
    AthTokenStatement('PROCREATE', [IdentifierToken('LOOP'), None]),
    TildeAthLoop(False, AthStatementList([
        AthTokenStatement('print', [LiteralToken('Hi.\\n', str)]),
        ], pendant='LOOP'),
        AthTokenStatement('EXECUTE', [IdentifierToken('NULL')]))
    ], pendant='THIS')
TildeAthInterp().exec_stmts('InfiniteLoopTest.~ATH', stmts)
