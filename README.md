# DataMade cookiecutter for scrapy scrapers

This cookiecutter sets up a new scrapy project for you. It defers in a few ways from what you would get from `scrapy startproject` to align
with DataMade's scraping practices.

1. `scrapy crawl` will [exit after the first exception](https://github.com/datamade/cookiecutter-scrapy/blob/762d09274c8276bd16ad139559b0a3d71000819a/%7B%7Bcookiecutter.project_name%7D%7D/%7B%7Bcookiecutter.project_name%7D%7D/settings.py#L96).
2. if an error is encountered, `scrapy crawl` will exit with a non-zero exit code.
3. the project contains a `setup.py` file wich will allow you to install the scraper with `pip` like a normal package. when installed this way, you can run `scrapy crawl your_spider_name` without having to be in a scrapy project.  
