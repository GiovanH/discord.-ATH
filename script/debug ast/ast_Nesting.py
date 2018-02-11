#!/usr/bin/env python
from athast import *
from symbol import ThisSymbol
from tildeath import TildeAthInterp

ast = AthAstList([
    TildeAthLoop(False, AthAstList([
        InputStmt('NUM', StringExpr('Enter a number: ')),
        CondJumpStmt(BinaryExpr('<', VarExpr('NUM'), IntExpr(8)), 40),
        PrintStmt([StringExpr('Your number is less than 8.\\n')]),
        CondJumpStmt(BinaryExpr('<', VarExpr('NUM'), IntExpr(4)), 19),
        PrintStmt([StringExpr('Your number is less than 4.\\n')]),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(3)), 3),
        PrintStmt([StringExpr('Congrats, your number is 3.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 46),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(2)), 3),
        PrintStmt([StringExpr('Congrats, your number is 2.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 42),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(1)), 3),
        PrintStmt([StringExpr('Congrats, your number is 1.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 38),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(0)), 3),
        PrintStmt([StringExpr('Congrats, your number is 0.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 34),
        PrintStmt([StringExpr('Negative? How deplorable.\\n')]),
        CondJumpStmt(None, 32),
        CondJumpStmt(BinaryExpr('>', VarExpr('NUM'), IntExpr(4)), 15),
        PrintStmt([StringExpr('Your number is more than 4.\\n')]),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(5)), 3),
        PrintStmt([StringExpr('Congrats, your number is 5.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 26),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(6)), 3),
        PrintStmt([StringExpr('Congrats, your number is 6.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 22),
        CondJumpStmt(BinaryExpr('==', VarExpr('NUM'), IntExpr(7)), 3),
        PrintStmt([StringExpr('Congrats, your number is 7.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 18),
        PrintStmt([StringExpr('This should never fuckin print.\\n')]),
        CondJumpStmt(None, 16),
        PrintStmt([StringExpr('Congrats, your number is 4.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 13),
        CondJumpStmt(BinaryExpr('>', VarExpr('NUM'), IntExpr(8)), 10),
        PrintStmt([StringExpr('Your number is more than 8.\\n')]),
        CondJumpStmt(BinaryExpr('<', VarExpr('NUM'), IntExpr(12)), 2),
        PrintStmt([StringExpr('Your number is less than 12.\\n')]),
        CondJumpStmt(None, 8),
        CondJumpStmt(BinaryExpr('>', VarExpr('NUM'), IntExpr(12)), 2),
        PrintStmt([StringExpr('Your number is more than 12.\\n')]),
        CondJumpStmt(None, 5),
        PrintStmt([StringExpr('Congrats, your number is 12.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        CondJumpStmt(None, 2),
        PrintStmt([StringExpr('Congrats, your number is 8.\\n')]),
        PrintStmt([StringExpr('Look at how achieved you are.\\n')]),
        PrintStmt([StringExpr('Time to end the program, mate.\\n')]),
        KillStmt(['THIS'])
        ], 'THIS'),
    ExecuteStmt([VarExpr('NULL')])
    )
    ], 'THIS')
interp = TildeAthInterp()
interp.bltin_vars['THIS'] = ThisSymbol('Nesting.~ATH', ast)
interp.execute(ast)
