import base64

message = r"C:\Users\imani\AppData\Roaming\Mozilla\Firefox\Profiles\qic8u2xz.default"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

# options=Options()
# firefox_profile = FirefoxProfile()
# firefox_profile.profile_dir = r"C:\Users\imani\AppData\Roaming\Mozilla\Firefox\Profiles\na2ocyg2.Sel00"
# options.profile = firefox_profile