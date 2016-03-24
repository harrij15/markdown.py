'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import *


class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('The quick brown fox jumped over the lazy dog\'s back.'), 
                '<p>The quick brown fox jumped over the lazy dog\'s back.</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')
        
    def test_first_header(self):
        self.assertEqual(run_markdown('#A First Level Header'), '<p><h1>A First Level Header</h1></p>')
        
    def test_second_header(self):
        self.assertEqual(run_markdown('##A Second Level Header'), '<p><h2>A Second Level Header</h2></p>')
        
    def test_third_header(self):
        self.assertEqual(run_markdown('### Header 3'), '<p><h3>Header 3</h3></p>')   
        
    def test_block(self):
        self.assertEqual(run_markdown('> This is a blockquote.\n>\n>  This is the second paragraph in the blockquote.\n>\n> ## This is an H2 in a blockquote'),
                         '<blockquote>\r\n\t<p>This is a blockquote.</p>\r\n\r\n <p>This is the second paragraph in the blockquote.</p>\r\n \r\n<h2>This is an H2 in a blockquote</h2>\r\n</blockquote>')   
        
if __name__ == '__main__':
    unittest.main()

