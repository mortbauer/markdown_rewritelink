## Markdown Extension to have custom callback to rewrite links

# Installation

    pip install git+git://github.com/mortbauer/markdown_rewritelink.git

# Usage

    >>> import markdown
    >>> from markdown_rewritelink import RewriteLinkExtension
    >>> def mycallback(link):
            modified_link = link + '/hallo'
            return modified_link
    >>> rewritelink = RewriteLinkExtension(config={'rewrite_link_callback':mycallback})
    >>> html = markdown.markdown(src, extensions=[rewritelink])
    >>> print(html)


Dependencies
------------

* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)


All rights reserved.

This software is released under the modified BSD License. 
