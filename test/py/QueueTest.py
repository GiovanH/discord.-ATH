#!/usr/bin/env python
from athast import *
from athparser import TildeAthInterp

ath_script = Serialize([ProcreateStmt(VarExpr('LOOP'), IntExpr(1)), ProcreateStmt(VarExpr('QUEUE'), VarExpr('NULL')), TildeAthLoop(False, VarExpr('LOOP'), Serialize([PrintFunc([StringExpr('Select action:\\n')]), PrintFunc([StringExpr('[1] Add an item to queue\\n')]), PrintFunc([StringExpr('[2] View queue\\n')]), PrintFunc([StringExpr('[3] Exit\\n')]), InputStmt(VarExpr('CHOICE'), StringExpr('')), DebateStmt(BinaryExpr('==', VarExpr('CHOICE'), IntExpr(3)), Serialize([KillFunc(VarExpr('LOOP'), [])], LOOP), [UnlessStmt(BinaryExpr('==', VarExpr('CHOICE'), IntExpr(2)), Serialize([ProcreateStmt(VarExpr('BLAH'), IntExpr(0)), ProcreateStmt(VarExpr('STACK'), VarExpr('NULL')), ReplicateStmt(VarExpr('TEMP'), VarExpr('QUEUE')), TildeAthLoop(False, VarExpr('BLAH'), Serialize([BifurcateStmt(VarExpr('TEMP'), VarExpr('HEAD'), VarExpr('TEMP')), DebateStmt(VarExpr('TEMP'), Serialize([PrintFunc([StringExpr('~s\\n'), VarExpr('HEAD')]), AggregateStmt(VarExpr('STACK'), VarExpr('HEAD'), VarExpr('STACK'))], BLAH), [UnlessStmt(None, Serialize([KillFunc(VarExpr('BLAH'), [])], BLAH))])], BLAH)), PrintFunc([StringExpr('Stack print done.\\n')]), ProcreateStmt(VarExpr('OOF'), IntExpr(0)), TildeAthLoop(False, VarExpr('OOF'), Serialize([BifurcateStmt(VarExpr('STACK'), VarExpr('STACK'), VarExpr('TAIL')), PrintFunc([StringExpr('I went oof.\\n')]), DebateStmt(VarExpr('STACK'), Serialize([PrintFunc([StringExpr('~s\\n'), VarExpr('TAIL')])], OOF), [UnlessStmt(None, Serialize([KillFunc(VarExpr('OOF'), [])], OOF))])], OOF)), PrintFunc([StringExpr('Queue print done.\\n')])], LOOP)), UnlessStmt(BinaryExpr('==', VarExpr('CHOICE'), IntExpr(1)), Serialize([InputStmt(VarExpr('ITEM'), StringExpr('Input string to add: ')), AggregateStmt(VarExpr('ITEM'), VarExpr('QUEUE'), VarExpr('QUEUE'))], LOOP)), UnlessStmt(None, Serialize([PrintFunc([StringExpr('Invalid input.')])], LOOP))])], LOOP)), KillFunc(VarExpr('THIS'), [])], THIS)
TildeAthInterp().execute(ath_script)
