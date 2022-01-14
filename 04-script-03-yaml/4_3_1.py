#!/usr/bin/env python3

import json

json_str = '''
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
'''
# Check
json_dump = json.dumps(json_str)
print(str(json_dump))