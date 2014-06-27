from libmproxy.flow import Response
from netlib.odict import ODictCaseless

"""
This example shows two ways to redirect flows to other destinations.
"""

def request(context, flow):

    if flow.request.host.endswith("cn"):
        resp = Response(flow.request,
                        [1,1],
                        301, "OK",
                        ODictCaseless([["Location","##"]]),
                        "",
                        None)
        flow.request.reply(resp)

