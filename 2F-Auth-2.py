# Code
# The following code is enough. I have also uploaded it to GitHub as separate module called onetimepass (available here: https://github.com/tadeck/onetimepass).

import hmac, base64, struct, hashlib, time

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)
# It has two functions:

# get_hotp_token() generates one-time token (that should invalidate after single use),
# get_totp_token() generates token based on time (changed in 30-second intervals),
# Parameters
# When it comes to parameters:

# secret is a secret value known to server (the above script) and client (Google Authenticator, by providing it as password within application),
# intervals_no is the number incremeneted after each generation of the token (this should be probably resolved on the server by checking some finite number of integers after last successful one checked in the past)
# How to use it
# Generate secret (it must be correct parameter for base64.b32decode()) - preferably 16-char (no = signs), as it surely worked for both script and Google Authenticator.
# Use get_hotp_token() if you want one-time passwords invalidated after each use. In Google Authenticator this type of passwords i mentioned as based on the counter. For checking it on the server you will need to check several values of intervals_no (as you have no quarantee that user did not generate the pass between the requests for some reason), but not less than the last working intervals_no value (thus you should probably store it somewhere).
# Use get_totp_token(), if you want a token working in 30-second intervals. You have to make sure both systems have correct time set (meaning that they both generate the same Unix timestamp in any given moment in time).
# Make sure to protect yourself from brute-force attack. If time-based password is used, then trying 1000000 values in less than 30 seconds gives 100% chance of guessing the password. In case of HMAC-based passowrds (HOTPs) it seems to be even worse.
