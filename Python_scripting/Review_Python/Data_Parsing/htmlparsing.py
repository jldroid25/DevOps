# Example file for parsing and processing HTML
#

from html.parser import HTMLParser
# For counting meta data in html tags file
metacount = 0

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    # For start tag
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountered start tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        # check if there are attributes on start tag
        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])


    # For end tag
    def handle_endtag(self, tag):
        print("Encountered End-Tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    # For Text data tag
    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered text data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():

    # Instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("404.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

        print("Meta tags found: " + str(metacount))
 
if __name__ == "__main__":
    main()