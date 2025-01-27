import argparse

import scrapy.signals as signals
from scrapy.commands.crawl import Command as ExistingCrawlCommand
from scrapy.signalmanager import dispatcher


class Command(ExistingCrawlCommand):

    def failing_exit_code_on_error(self, *args, **kwargs):
        self.exitcode = 1

    def run(self, args: list[str], opts: argparse.Namespace) -> None:

        dispatcher.connect(self.failing_exit_code_on_error, signal=signals.spider_error)
        dispatcher.connect(self.failing_exit_code_on_error, signal=signals.item_error)

        super().run(args, opts)
