###
#
#   Version: 1.0.0
#   Date: 2020-03-29
#   Author: Yves Vindevogel (vindevoy)
#
###

import cherrypy

from dataloader import DataLoader
from settings import Settings
from singleton import Singleton
from templateloader import TemplateLoader


class Application(metaclass=Singleton):
    @cherrypy.expose
    def index(self, page_index=1):
        template = TemplateLoader('src/theme/default').get_template('screen_index.html')
        rendered = template.render(data=DataLoader().get_index_data(page_index))

        return rendered

    @cherrypy.expose
    def pages(self, page):
        # page on the URL: http://www.yoursite.ext/pages/page

        template = TemplateLoader('src/theme/default').get_template('screen_page.html')
        rendered = template.render(data=DataLoader().get_page_data(page))

        return rendered

    @cherrypy.expose
    def posts(self, post):
        template = TemplateLoader('src/theme/default').get_template('screen_post.html')
        rendered = template.render(data=DataLoader().get_post_data(post))

        return rendered

    @cherrypy.expose
    def categories(self, category, page_index=1):
        template = TemplateLoader('src/theme/default').get_template('screen_category.html')
        rendered = template.render(data=DataLoader().get_category_data(category, page_index))

        return rendered

    @cherrypy.expose
    def print_page(self, page):
        template = TemplateLoader('src/theme/default').get_template('print_page.html')
        rendered = template.render(data=DataLoader().get_page_data(page))

        return rendered

    @cherrypy.expose
    def print_post(self, post):
        template = TemplateLoader('src/theme/default').get_template('print_post.html')
        rendered = template.render(data=DataLoader().get_post_data(post))

        return rendered


if __name__ == '__main__':
    cherrypy.quickstart(Application(), config=Settings().server_config)
