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
        self.response.write('<form action="/" method="post"><div>')
        self.response.write('<textarea name="content" rows="3" cols="60"></textarea>')
        self.response.write('</div><div><input type="submit" value="Send Feedback">')
        self.response.write('</div></form>')
        self.response.write('</body></html>')
        
    def post(self):
        self.response.write('processing from data...')
        feedback = self.request.get('content')
        self.response.write('<p>'+feedback+'</p>')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
