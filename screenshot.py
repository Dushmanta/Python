#!/usr/bin/python
from selenium import webdriver
from PIL import Image
from cStringIO import StringIO

verbose = 1

browser = webdriver.Firefox()
browser.get('http://google.com')


js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

scrollheight = browser.execute_script(js)

if verbose > 0: 
    print scrollheight

slices = []
offset = 0
while offset < scrollheight:
    if verbose > 0: 
        print offset

    browser.execute_script("window.scrollTo(0, %s);" % offset)
    img = Image.open(StringIO(browser.get_screenshot_as_png()))
    offset += img.size[1]
    slices.append(img)

    if verbose > 0:
        browser.get_screenshot_as_file('%s/screen_%s.png' % ('/tmp', offset))
        print scrollheight


screenshot = Image.new('RGB', (slices[0].size[0], offset))
offset = 0
for img in slices:
    screenshot.paste(img, (0, offset))
    offset += img.size[1]

screenshot.save('/tmp/test.png')
