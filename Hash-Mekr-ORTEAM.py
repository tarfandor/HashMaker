import hashlib
 
print ("""
		|------------------------------------|
		|      Hash Maker Version 3.0        |
		|<=================================>>|
		|---------->  OPTIONS <--------------|
		|---------->-1 MD5    <--------------|
		|---------->-2 SHA1   <--------------|
		|---------->-3 SHA224 <--------------|
		|---------->-4 SHA256 <--------------|
		|---------->-5 SHA384 <--------------|
		|---------->-6 SHA512 <--------------|
		|<=================================>>|
		|CREATOR: ORTEAM                     |
		|My Telegram Channel :	T.me/GagteOR |
		|------------------------------------|
""")

inputer = input('Enter Your password for hashling :' )
model = input("select the number options : ")

if model == "1":
 md5 = hashlib.md5(inputer.encode())
 print("""
	|------------------------------------|
	|       Md5 Your Password is         |
	|<=================================>>|
	|""",md5.hexdigest(),"""  |
	|<=================================>>|
	|CREATOR: ORTEAM                     |
	|My Telegram Channel :	T.me/GagteOR |
	|------------------------------------|""")
elif model == "2":
 sha1 = hashlib.sha1(inputer.encode())
 print("""
	|------------------------------------------|
	|          Sha1 Your Password is           |
	|<=======================================>>|
	|""",sha1.hexdigest(),"""|
	|<=======================================>>|
	|CREATOR: ORTEAM                           |
	|My Telegram Channel :	T.me/GagteOR       |
	|------------------------------------------|""")
elif model == "3":
 sha224 = hashlib.sha224(inputer.encode())
 print("""
	|----------------------------------------------------------|
	|                Sha224 Your Password is                   |
	|<=======================================================>>|
	|""",sha224.hexdigest(),"""|
	|<=======================================================>>|
	|CREATOR: ORTEAM                                           |
	|My Telegram Channel :	T.me/GagteOR                       |
	|----------------------------------------------------------|""")
elif model == "4":
 sha256 = hashlib.sha256(inputer.encode())
 print("""
	|------------------------------------------------------------------|
	|                    Sha256 Your Password is                       |
	|<===============================================================>>|
	|""",sha256.hexdigest(),"""|
	|<===============================================================>>|
	|CREATOR: ORTEAM                                                   |
	|My Telegram Channel :	T.me/GagteOR                               |
	|------------------------------------------------------------------|""")
elif model == "5":
 sha384 = hashlib.sha384(inputer.encode())
 print("""
	|--------------------------------------------------------------------------------------------------|
	|                                  Sha384 Your Password is                                         |
	|<===============================================================================================>>|
	|""",sha384.hexdigest(),"""|
	|<===============================================================================================>>|
	|CREATOR: ORTEAM                                                                                   |
	|My Telegram Channel :	T.me/GagteOR                                                               |
	|--------------------------------------------------------------------------------------------------|""")
elif model == "6":
 sha512 = hashlib.sha512(inputer.encode())
 print("""
	|----------------------------------------------------------------------------------------------------------------------------------|
	|                                               Sha512 Your Password is                                                            |
	|<===============================================================================================================================>>|
	|""",sha512.hexdigest(),"""|
	|<===============================================================================================================================>>|
	|CREATOR: ORTEAM                                                                                                                   |
	|My Telegram Channel :	T.me/GagteOR                                                                                               |
	|----------------------------------------------------------------------------------------------------------------------------------|""")
else:
 exit()