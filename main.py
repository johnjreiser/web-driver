import WebDriver
import getpass
import pdfkit

web = WebDriver.AuthenticatedWeb("https://bugzilla.rowan.edu/bugzilla/")

username = input("ID: ")
password = getpass.getpass("Password: ")

web.authenticate(username, password)

for bug in (3460, 3461, 3462):
    page = web.go("https://bugzilla.rowan.edu/bugzilla/show_bug.cgi?id={}".format(bug))
    pdfkit.from_file(page.page_source, "~/bug{}.pdf".format(bug))
