#
# Copyright 2016 Stephen Kelly <steveire@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os, sys

import rules_engine
sys.path.append(os.path.dirname(os.path.dirname(rules_engine.__file__)))
import Qt5Ruleset

def _container_discard_base(container, sip, matcher):
    sip["base_specifiers"] = ""

def local_container_rules():
    return [
        [".*", "KCompletionMatches", ".*", ".*", ".*", _container_discard_base],
    ]

def local_function_rules():
    return [
        ["KCompletionBase", "keyBindingMap", ".*", ".*", ".*", rules_engine.function_discard],
        ["KCompletionBase", "getKeyBindings", ".*", ".*", ".*", rules_engine.function_discard],
        ["KCompletionBase", "setKeyBindingMap", ".*", ".*", ".*", rules_engine.function_discard],
        ["KCompletionMatches", "KCompletionMatches", ".*", ".*", ".*KCompletionMatchesWrapper.*", rules_engine.function_discard],
    ]

class RuleSet(Qt5Ruleset.RuleSet):
    def __init__(self):
        Qt5Ruleset.RuleSet.__init__(self)
        self._fn_db = rules_engine.FunctionRuleDb(lambda: local_function_rules() + Qt5Ruleset.function_rules())
        self._container_db = rules_engine.ContainerRuleDb(lambda: local_container_rules() + Qt5Ruleset.container_rules())
