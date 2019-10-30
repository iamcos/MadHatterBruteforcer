import base64, zlib
import base64
import zlib


json_str = zlib.decompress(base64.b64decode(data), 16 + zlib.MAX_WBITS).decode("utf-8")
print(json_str)
