import re
import six
import pyjade

from pyjade.ext.jinja import Compiler as JinjaCompiler
from jinja2.ext import babel_extract, extract_from_ast


def extract_jade(fileobj, keywords, comment_tags, options):
	"""
	Extract messages from .jade files.

	NOTE: Line numbers are currently broken
	
	:param fileobj: the file-like object the messages should be extracted
					from
	:param keywords: a list of keywords (i.e. function names) that should
					 be recognized as translation functions
	:param comment_tags: a list of translator tags to search for and
						 include in the results
	:param options: a dictionary of additional options (optional)
	:return: an iterator over ``(lineno, funcname, message, comments)``
			 tuples
	:rtype: ``iterator``
	"""
	src_jade = six.b("").join(fileobj.readlines())
	parser = pyjade.parser.Parser(src_jade)
	block = parser.parse()

	compiler = JinjaCompiler(block, pretty=True)
	src_jinja = compiler.compile()

	new_fileobj = six.BytesIO(bytes(src_jinja, 'UTF-8'))

	def drop_lineno(v):
		return (0, v[1], v[2], v[3])

	return map(drop_lineno, babel_extract(new_fileobj, keywords, comment_tags, options))
	