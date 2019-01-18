#
#   This file is part of m.css.
#
#   Copyright © 2017, 2018, 2019 Vladimír Vondruš <mosra@centrum.cz>
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the "Software"),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#   in all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#   THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#

import shutil
import logging

# 作者
AUTHOR = 'firebird'

# 网站logo文字
M_SITE_LOGO_TEXT = 'FBT'

# 网站名称
SITENAME = 'FBT'

# 网站基本地址，最后没有斜杠，https://或http://
SITEURL = ''

STATIC_URL = '{path}'

# Pelican要处理的内容目录的路径
PATH = 'content'
# 要查看文章的目录和文件列表，相对于 PATH
ARTICLE_PATHS = ['examples']
ARTICLE_EXCLUDES = ['examples/authors', 'examples/categories', 'examples/tags']
# 要查看页面的目录和文件列表，相对于PATH
PAGE_PATHS = ['']

# 日期信息中使用的时区
TIMEZONE = 'Asia/Shanghai'	

DEFAULT_LANG = 'en'

import platform
if platform.system() == 'Windows':
    DATE_FORMATS = {'en': ('usa', '%b %d, %Y')}
else:
    DATE_FORMATS = {'en': ('en_US.UTF-8', '%b %d, %Y')}

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

M_BLOG_NAME = "fbt example articles"
M_BLOG_URL = 'examples/'

#M_FAVICON = ('favicon.ico', 'image/x-icon')
M_FAVICON = ('firebird.png')

M_SOCIAL_TWITTER_SITE = '@czmosra'
M_SOCIAL_TWITTER_SITE_ID = 1537427036
#M_SOCIAL_IMAGE = 'static/site.jpg'
M_SOCIAL_BLOG_SUMMARY = 'Example articles for the FBT'

M_METADATA_AUTHOR_PATH = 'examples/authors'
M_METADATA_CATEGORY_PATH = 'examples/categories'
M_METADATA_TAG_PATH = 'examples/tags'

M_LINKS_NAVBAR1 = [('Blog', 'https://www.firebirdtool.com/blog', '', []),
                   ('Docs', 'https://www.firebirdtool.com/doc-cpplogging', '', [
#                        ('Grid system', 'css/grid/', 'css/grid'),
#                        ('Typography', 'css/typography/', 'css/typography'),
#                        ('Components', 'css/components/', 'css/components'),
#                        ('Page layout', 'css/page-layout/', 'css/page-layout'),
#                        ('Themes', 'css/themes/', 'css/themes')
#                        ]),
#                   ('Pelican', 'pelican/', 'pelican', [
#                        ('Writing content', 'pelican/writing-content/', 'pelican/writing-content'),
#                        ('Theme', 'pelican/theme/', 'pelican/theme')
                        ])]

M_LINKS_NAVBAR2 = [('Tools', 'https://github.com/firebirdtools', '', [
#                        ('HTML sanity', 'plugins/htmlsanity/', 'plugins/htmlsanity'),
 #                       ('Components', 'plugins/components/', 'plugins/components'),
  #                      ('Images', 'plugins/images/', 'plugins/images'),
   #                     ('Math and code', 'plugins/math-and-code/', 'plugins/math-and-code'),
    #                    ('Links and other', 'plugins/links/', 'plugins/links'),
     #                   ('Plots and graphs', 'plugins/plots-and-graphs/', 'plugins/plots-and-graphs'),
      #                  ('Metadata', 'plugins/metadata/', 'plugins/metadata')
                        ]),
#                   ('Doxygen theme', 'doxygen/', 'doxygen', []),
                   ('GitHub', 'https://github.com/firebirdtools/firebirdtools.github.io', '', [])]


#M_FINE_PRINT = """
#| m.css. Copyright © `Vladimír Vondruš <http://mosra.cz>`_, 2017--2019. Site
#  powered by `Pelican <https://getpelican.com>`_ and m.css.
#| Code and content is `available on GitHub under MIT <https://github.com/mosra/m.css>`_.
#  Contact the author via `Gitter <https://gitter.im/mosra/m.css>`_,
#  `e-mail <mosra@centrum.cz>`_ or `Twitter <https://twitter.com/czmosra>`_.
#"""

DEFAULT_PAGINATION = 10

# Pelican的默认设置包括“images”目录，静态文件的目录列表
STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {'static/firebird.png': {'path': 'firebird.png'}}

# 插件目录
PLUGIN_PATHS = ['m.css/pelican-plugins']
PLUGINS = ['m.abbr',
           'm.code',
           'm.components',
           'm.dox',
           'm.dot',
           'm.filesize',
           'm.gl',
           'm.gh',
           'm.htmlsanity',
           'm.images',
           'm.link',
           'm.math',
           'm.metadata',
           'm.plots',
           'm.vk']

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
M_THEME_COLOR = '#22272e'
# 指定要加载的CSS文件
M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Code+Pro:400,400i,600%7CSource+Sans+Pro:400,400i,600,600i&subset=latin-ext',
               'static/m-dark.css',
               # enable so we see the problems right away (not present for
               # publish)
               'static/m-debug.css'
              ]
#M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
               #'static/m-light.css']


# 包含要解析并转换为HTML的reST / Markdown内容的元数据字段列表
FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True
#M_DOX_TAGFILES = [
#    ('../doc/doxygen/corrade.tag', 'https://doc.magnum.graphics/corrade/', ['Corrade::'])]

if not shutil.which('latex'):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True


# 直接用于呈现内容的模板列表。通常，直接模板用于生成内容集合的索引页面（例如，标签和类别索引页面）
DIRECT_TEMPLATES = ['archives']

##########################################################
# {slug}表示该标签下，标记的路径
# 链接到页面的URL
PAGE_URL = '{slug}/'
# 将保存页面的位置。此值必须与PAGE_URL相同
PAGE_SAVE_AS = '{slug}/index.html'
#########################################################

# 存档URL
ARCHIVES_URL = 'examples/'
# 保存文章存档页面的位置
ARCHIVES_SAVE_AS = 'examples/index.html'

# 用于引用文章的URL
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
ARTICLE_SAVE_AS = '{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHORS_SAVE_AS = None # Not used
CATEGORIES_SAVE_AS = None # Not used
TAGS_SAVE_AS = None # Not used

############################################
# 指定从哪里自动生成slug的位置。
SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'


#DEFAULT_METADATA = {}
#############################################