#!/usr/bin/python
# Copyright 2017 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import smtpd

class SMTPServerMock(smtpd.SMTPServer):

    def __init__(self, *args, **kwargs):
        self.received = False
        smtpd.SMTPServer.__init__(self, *args, **kwargs)

    def process_message(self, *args, **kwargs):
        self.received = True
