import hashlib

h = hashlib.sha256()

h.update(b"something")
some = h.hexdigest()
print(some)
