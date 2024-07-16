from urllib.request import urlopen

def web_crawly():
  url = "http://olympus.realpython.org/profiles/aphrodite"
  # Pass url to urlopen to open the web page HTML
  page = urlopen(url)
  # Read the HTML from the web page
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  print("Here the result is shown>\n")
  print(html)
