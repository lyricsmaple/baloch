# Encrypt by Ariya Saputra
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))