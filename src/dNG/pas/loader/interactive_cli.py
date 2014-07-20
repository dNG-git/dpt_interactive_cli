# -*- coding: utf-8 -*-
##j## BOF

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;interactive_cli

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.py?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasInteractiveCliVersion)#
#echo(__FILEPATH__)#
"""

from .cli import Cli
from .interactive_cli_mixin import InteractiveCliMixin

class InteractiveCli(Cli, InteractiveCliMixin):
#
	"""
"InteractiveCli" extends simple ones with input and output aware methods.

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: interactive_cli
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	# pylint: disable=unused-argument

	def __init__(self):
	#
		"""
Constructor __init__(InteractiveCli)

:param args: Parsed command line arguments

:since: v0.1.00
		"""

		Cli.__init__(self)
		InteractiveCliMixin.__init__(self)
	#
#

##j## EOF