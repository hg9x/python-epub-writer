
class EPuB:
    '''
    Main class
    Takes in metadata + list of HTML content in constructor
    `compile` method writes files to a temporary directory,
    downloads (or copies) any <img> tags in the HTML content
    Zips it up and produces a file
    '''

    def __init__(self, metadata, content):
        '''
        Metadata is a dictionary
            * title 
            * author
            * publisher
            * cover

        Content is a list of Strings
        '''
        pass

    def compile(self, tmp_dir, output_dir):
        pass

class Image:
    '''
    Represents an image in HTML content

    Needs to a do a few things:
    * Keep track of the URL (if it is a URL), so it can be downloaded later
    * Download that image (or copy, if it is a filesys path)
    * Creates a UUID that is used as the file name
    * Return the new <img> tag
    '''

    def __init__(self, URL):
        pass