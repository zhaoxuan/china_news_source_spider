# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from models import NewsSite


class Pipeline(object):
    def process_item(self, item, spider):
        """
        Pipeline auto callback function.

        Args:
            item:
            spider:

        Returns:
            None.

        Raises:
            None.
        """
        self.save_data(item)

    def save_data(self, item):
        """
        保存数据到数据库.

        Args:
            item:

        Returns:
            None.

        Raises:
            None.
        """
        domain = item['domain']
        name = item['name']

        if NewsSite.select().where(NewsSite.domain == domain).count() == 0:
            fi = NewsSite()
        else:
            fi = NewsSite.get(NewsSite.domain == domain)

        fi.domain = domain
        fi.name = name

        fi.save()
