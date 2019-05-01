# -*- coding: utf-8 -*-

"""
direct Python Toolbox
All-in-one toolbox to encapsulate Python runtime variants
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?dpt;interactive_cli

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;mpl2
----------------------------------------------------------------------------
#echo(dptInteractiveCliVersion)#
#echo(__FILEPATH__)#
"""

from time import ctime
import os
import sys

from dpt_runtime.traced_exception import TracedException
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.output import create_output, get_default_output, set_default_output
from prompt_toolkit.shortcuts import PromptSession

class InteractiveCliMixin(object):
    """
This mixin provides methods to handle console input and output.

:author:     direct Netware Group et al.
:copyright:  (C) direct Netware Group - All rights reserved
:package:    dpt
:subpackage: interactive_cli
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
    """

    def __init__(self):
        """
Constructor __init__(InteractiveCliMixin)

:since: v1.0.00
        """

        self.prompt_session = None
        """
prompt_toolkit based input prompt session
        """
        self.output_pid = os.getpid()
        """
PID used for output separation
        """

        self.prompt_session = PromptSession(mouse_support = True)
    #

    @property
    def output_stream(self):
        """
Returns the current output stream pointer in use.

:param prompt: Inline prompt

:return: (int) Stream pointer number
:since:  v1.0.0
        """

        return get_default_output().fileno()
    #

    @output_stream.setter
    def output_stream(self, pointer):
        """
Sets the output stream pointer to use.

:param pointer: Stream pointer number

:since: v1.0.0
        """

        set_default_output(create_output(pointer))
    #

    def error(self, _exception):
        """
Prints the stack trace on this error event.

:param _exception: Inner exception

:since: v1.0.0
        """

        if (isinstance(_exception, TracedException)): _exception.print_stack_trace(self.output_stream)
        else: TracedException.print_current_stack_trace(self.output_stream)
    #

    def input(self, prompt):
        """
Reads one line of input.

:param prompt: Inline prompt

:return: (str) Cli input
:since:  v1.0.0
        """

        return self.prompt_session.prompt(prompt)
    #

    def output(self, line, *args):
        """
Outputs the given line. Additional positional arguments are used for string
formatting.

:param line: Output line

:since: v1.0.0
        """

        output = (line.format(*args)
                  if (len(args) > 0) else
                  line
                 )

        print_formatted_text(output)
    #

    def output_error(self, line, *args):
        """
Outputs the given error line. Additional positional arguments are used for
string formatting.

:param line: Output line

:since: v1.0.0
        """

        line = (line.format(*args)
                if (len(args) > 0) else
                line
               )

        self.output_formatted("<small>[{0}({1:d}) {2}]</small> <strong>{3}</strong>",
                              self.__class__.__name__,
                              self.output_pid,
                              ctime(),
                              line
                             )
    #

    def output_formatted(self, line, *args):
        """
Outputs the given HTML-formatted line. Additional positional arguments are
used for string formatting.

:param line: Output line

:since: v1.0.0
        """

        output = HTML(line.format(*args)
                      if (len(args) > 0) else
                      line
                     )

        print_formatted_text(output)
    #

    def output_info(self, line, *args):
        """
Outputs the given informational line. Additional positional arguments are
used for string formatting.

:param line: Output line

:since: v1.0.0
        """

        line = (line.format(*args)
                if (len(args) > 0) else
                line
               )

        self.output_formatted("<small>[{0}({1:d}) {2}]</small> {3}",
                              self.__class__.__name__,
                              self.output_pid,
                              ctime(),
                              line
                             )
    #

    def secure_input(self, prompt):
        """
Reads one line of input without showing the user what he typed.

:param prompt: Inline prompt

:return: (str) Cli input
:since:  v1.0.0
        """

        return self.prompt_session.prompt(prompt, is_password = True)
    #
#
