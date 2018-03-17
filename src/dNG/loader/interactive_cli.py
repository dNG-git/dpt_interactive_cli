# -*- coding: utf-8 -*-

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?pas;interactive_cli

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasInteractiveCliVersion)#
#echo(__FILEPATH__)#
"""

# pylint: disable=import-error

from .cli import Cli
from .interactive_cli_mixin import InteractiveCliMixin

class InteractiveCli(Cli, InteractiveCliMixin):
    """
"InteractiveCli" extends simple ones with input and output aware methods.

:author:     direct Netware Group et al.
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: interactive_cli
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
    """

    # pylint: disable=unused-argument

    def __init__(self):
        """
Constructor __init__(InteractiveCli)

:param args: Parsed command line arguments

:since: v1.0.0
        """

        Cli.__init__(self)
        InteractiveCliMixin.__init__(self)
    #
#
