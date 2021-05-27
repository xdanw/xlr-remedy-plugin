#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from remedy.RemedyClient import RemedyClient

if remedyServer is None:
    sys.exit("No server provided.")

client = RemedyClient.create_client(remedyServer, username, password)

if matchChangId:
    print "Matching Change Request ID: %s" % entryId
    data = client.get_change_request(formName, entryId)

else:
    print "Matching Entry ID: %s" % entryId
    data = client.get_entry(formName, entryId)

if statusField not in data:
    sys.exit("Field with name [%s] not found in entry [%s], data [%s].\n" % (statusField, data['Request ID'], str(data)))
    
status = data[statusField]
print "Found %s in Remedy with status %s" % (entryId, status)

