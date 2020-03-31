from bs4 import BeautifulSoup
from uuid import uuid4
from pathlib import Path
import shutil
from epub_writer import TEMPLATES as t
import aiofiles
import aiohttp
import asyncio

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

        Content is a list of dictionaries
            * title 
            * html

        '''

        self.title = metadata.get('title', '')
        self.author = metadata.get('author', '')
        self.publisher = metadata.get('publisher', '')
        self.cover = metadata.get('cover', '')


        self.images = []
        self.chapters = []
        for item in content:
            #some parsing has to be done; we need to make sure all images are 
            #downloaded
            soup = BeautifulSoup(item.get('html', ''), 'html.parser')
            for img in soup.find_all('img'):
                src = img['src']
                image = Image(src)
                img['src'] = image.new_src()
                self.images.append(image)

            #then we just stick it in the mako template
            html_string = t.PAGE.render(title=item.get('title', ''), body=soup.prettify()) 

            chapter = Chapter(html_string)
            self.chapters.append(chapter)

        
    #TODO: Error checking for both
    async def write_chapters(self, tmp_dir):
        for chapter in self.chapters:
            full_dir = tmp_dir / chapter.filepath()
            async with aiofiles.open(str(full_dir), 'w') as f:
                await f.write(chapter.HTML)
    
    async def write_images(self, tmp_dir):
        async with aiohttp.ClientSession() as session:
            for image in self.images:
                full_dir = tmp_dir / image.filepath()
                async with session.get(image.src) as resp:
                    if resp.status == 200:
                        async with aiofiles.open(str(full_dir), 'wb') as f:
                            await f.write(await resp.read())
    
    async def async_compile(self, tmp_dir, output_dir):
        pass

    def compile(self, tmp_dir, output_dir):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.write_chapters(tmp_dir))

class Chapter:
    '''
    Represents a chapter in the epub
    Has an HTML string, and a UUID
    UUID represents final path
    '''

    def __init__(self, HTML):
        self.HTML = HTML
        self.UUID = str(uuid4())
    
    def filepath(self):
        return Path('OEBPS/Text') / Path(f'{self.UUID}.xhtml')

    def __str__(self):
        return f'...{self.HTML[:20]}... | {self.UUID}'
    
    def __repr__(self):
        return str(self)

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
        self.src = URL
        self.UUID = str(uuid4())

    def new_src(self):
        return f'../Images/{self.UUID}.png'
    
    def filepath(self):
        return Path('OEBPS/Images') / Path(f'{self.UUID}.png')
    
    def __str__(self):
        return f'{self.new_src()} | {self.src}'
    
    def __repr__(self):
        return str(self)