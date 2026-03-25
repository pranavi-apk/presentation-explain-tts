import json, time, urllib.request, urllib.parse, base64
with open('pptx-explainer-171bd8face04.json', 'r') as f:
    sa = json.load(f)

# Quick JWT generation
header = {"alg":"RS256","typ":"JWT"}
now = int(time.time())
claim = {
    "iss": sa["client_email"],
    "scope": "https://www.googleapis.com/auth/drive",
    "aud": sa["token_uri"],
    "exp": now + 3600,
    "iat": now
}

import jwt
# Wait, jwt library might not be installed. Let's just use a curl command in bash if possible?
# Actually, node.js is better since it's a web project.
