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

from getpass import getpass
from time import ctime
import os
import sys

class InteractiveCliMixin(object):
#
	"""
This mixin provides methods to handle console input and output.

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: interactive_cli
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def __init__(self):
	#
		"""
Constructor __init__(InteractiveCliMixin)

:since: v0.1.00
		"""

		self.output_pid = os.getpid()
		"""
PID used for output separation
		"""
		self.output_stream = sys.stdout
		"""
Output stream used for writing
		"""
	#

	def input(self, prompt):
	#
		"""
Outputs the given line. Additional positional arguments are used for string formatting.

:param line: Output line

:since: v0.1.00
		"""

		try: _return = raw_input(prompt)
		except NameError: _return = input(prompt)

		return _return
	#

	def output(self, line, *args):
	#
		"""
Outputs the given line. Additional positional arguments are used for string formatting.

:param line: Output line

:since: v0.1.00
		"""

		# pylint: disable=star-args

		output = (line.format(*args)
		          if (len(args) > 0) else
		          line
		         )

		self.output_stream.writelines(( output, os.linesep ))
	#

	def output_info(self, line, *args):
	#
		"""
Outputs the given line. Additional positional arguments are used for string formatting.

:param line: Output line

:since: v0.1.00
		"""

		# pylint: disable=star-args

		line = (line.format(*args)
		        if (len(args) > 0) else
		        line
		       )

		self.output("[{0}({1:d}) {2}] {3}".format(self.__class__.__name__, self.output_pid, ctime(), line))
	#

	def secure_input(self, prompt):
	#
		"""
Outputs the given line. Additional positional arguments are used for string formatting.

:param line: Output line

:since: v0.1.00
		"""

		return getpass(prompt)
	#
#

##j## EOF