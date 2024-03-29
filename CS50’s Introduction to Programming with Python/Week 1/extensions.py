def extensions():
    ask = input("Enter the name of extensions: ").strip().lower()
    if  ".jpg" in ask:
        print("image/jpeg")
    elif  ".jpeg" in ask:
        print("image/jpeg")
    elif ".png"in ask:
        print("image/png")
    elif ".gif" in ask:
        print("image/gif")
    elif ".pdf" in ask:
        print("application/pdf")
    elif ".txt" in ask :
        print("text/plain")
    elif ".zip" in ask:
        print("application/zip")
    else:
        print("application/octet-stream")
extensions()
