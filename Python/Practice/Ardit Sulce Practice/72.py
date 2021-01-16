import webbrowser

query = input("Google search:- ")
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)
webbrowser.open_new(url)
