#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
     self.redirect("https://www.madjabb.com/lnk.asp?o=8456&c=918273&a=279700&k=39F0ADE09EF080B7FCF404F33E39E840&l=7168 ", True)
		# and this is the main code

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
