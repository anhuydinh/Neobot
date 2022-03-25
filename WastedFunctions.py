#--------------Useless, inefficient

# def importing():
#     warning_msg = "System restarted due to module installing\nIf the program don't run properly, please modify your pip installation directory"
#     try:
#         from instapy import InstaPy
#     except:
#         os.write("pip install instapy")
#         print(warning_msg)
#     try:
#         from PIL import Image
#     except:
#         os.write("pip install Pillow")
#         print(warning_msg)
#     try:
#         import subprocess
#     except:
#         os.write("pip install subprocess")
#         print(warning_msg)
# importing()

#----------Check logs, moved to __init__
# if os.path.isdir('logs') == True:
#     pass
# else: #
#     os.mkdir("logs")

# functions.check_logs()