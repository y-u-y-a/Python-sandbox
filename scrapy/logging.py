2020-10-27 13:11:00 [scrapy.utils.log] INFO: Scrapy 2.4.0 started (bot: src)
2020-10-27 13:11:00 [scrapy.utils.log] INFO: Versions: lxml 4.6.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.8 (default, Sep 21 2020, 21:58:35) - [Clang 11.0.0 (clang-1100.0.33.16)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1h  22 Sep 2020), cryptography 3.2, Platform Darwin-18.7.0-x86_64-i386-64bit
2020-10-27 13:11:00 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-10-27 13:11:00 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'src',
 'DOWNLOAD_DELAY': 2,
 'HTTPCACHE_ENABLED': True,
 'LOG_FILE': 'index.txt',
 'NEWSPIDER_MODULE': 'src.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['src.spiders']}
2020-10-27 13:11:01 [scrapy.extensions.telnet] INFO: Telnet Password: 6038ec49f32f35e2
2020-10-27 13:11:01 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-10-27 13:11:01 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats',
 'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware']
2020-10-27 13:11:01 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-10-27 13:11:01 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-10-27 13:11:01 [scrapy.core.engine] INFO: Spider opened
2020-10-27 13:11:01 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-10-27 13:11:01 [scrapy.extensions.httpcache] DEBUG: Using filesystem cache storage in /Users/yuya/develop/Sub/Python-sandbox/scrapy/.scrapy/httpcache
2020-10-27 13:11:01 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-10-27 13:11:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://job.mynavi.jp/robots.txt> (referer: None) ['cached']
2020-10-27 13:11:01 [scrapy.core.engine] DEBUG: Crawled (405) <GET https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/doSearchTypeIndustryArea> (referer: None) ['cached']
2020-10-27 13:11:01 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <405 https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/doSearchTypeIndustryArea>: HTTP status code is not handled or not allowed
2020-10-27 13:11:01 [scrapy.core.engine] INFO: Closing spider (finished)
2020-10-27 13:11:01 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 552,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 23853,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/405': 1,
 'elapsed_time_seconds': 0.138231,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 10, 27, 4, 11, 1, 345869),
 'httpcache/hit': 2,
 'httperror/response_ignored_count': 1,
 'httperror/response_ignored_status_count/405': 1,
 'log_count/DEBUG': 3,
 'log_count/INFO': 11,
 'memusage/max': 54071296,
 'memusage/startup': 54067200,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2020, 10, 27, 4, 11, 1, 207638)}
2020-10-27 13:11:01 [scrapy.core.engine] INFO: Spider closed (finished)
2020-10-27 13:11:30 [scrapy.utils.log] INFO: Scrapy 2.4.0 started (bot: src)
2020-10-27 13:11:30 [scrapy.utils.log] INFO: Versions: lxml 4.6.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.8 (default, Sep 21 2020, 21:58:35) - [Clang 11.0.0 (clang-1100.0.33.16)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1h  22 Sep 2020), cryptography 3.2, Platform Darwin-18.7.0-x86_64-i386-64bit
2020-10-27 13:11:30 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-10-27 13:11:30 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'src',
 'DOWNLOAD_DELAY': 2,
 'HTTPCACHE_ENABLED': True,
 'LOG_FILE': 'index.txt',
 'NEWSPIDER_MODULE': 'src.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['src.spiders']}
2020-10-27 13:11:30 [scrapy.extensions.telnet] INFO: Telnet Password: d027cd0e19d5f495
2020-10-27 13:11:30 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-10-27 13:11:30 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats',
 'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware']
2020-10-27 13:11:30 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-10-27 13:11:30 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-10-27 13:11:30 [scrapy.core.engine] INFO: Spider opened
2020-10-27 13:11:30 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-10-27 13:11:30 [scrapy.extensions.httpcache] DEBUG: Using filesystem cache storage in /Users/yuya/develop/Sub/Python-sandbox/scrapy/.scrapy/httpcache
2020-10-27 13:11:30 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-10-27 13:11:30 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://job.mynavi.jp/robots.txt> (referer: None) ['cached']
2020-10-27 13:11:30 [scrapy.core.engine] DEBUG: Crawled (405) <GET https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/doSearchTypeIndustryArea> (referer: None) ['cached']
2020-10-27 13:11:30 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <405 https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/doSearchTypeIndustryArea>: HTTP status code is not handled or not allowed
2020-10-27 13:11:30 [scrapy.core.engine] INFO: Closing spider (finished)
2020-10-27 13:11:30 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 552,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 23853,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/405': 1,
 'elapsed_time_seconds': 0.131944,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 10, 27, 4, 11, 30, 576371),
 'httpcache/hit': 2,
 'httperror/response_ignored_count': 1,
 'httperror/response_ignored_status_count/405': 1,
 'log_count/DEBUG': 3,
 'log_count/INFO': 11,
 'memusage/max': 53809152,
 'memusage/startup': 53805056,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2020, 10, 27, 4, 11, 30, 444427)}
2020-10-27 13:11:30 [scrapy.core.engine] INFO: Spider closed (finished)
2020-10-27 13:12:33 [scrapy.utils.log] INFO: Scrapy 2.4.0 started (bot: src)
2020-10-27 13:12:33 [scrapy.utils.log] INFO: Versions: lxml 4.6.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.8 (default, Sep 21 2020, 21:58:35) - [Clang 11.0.0 (clang-1100.0.33.16)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1h  22 Sep 2020), cryptography 3.2, Platform Darwin-18.7.0-x86_64-i386-64bit
2020-10-27 13:12:33 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-10-27 13:12:33 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'src',
 'DOWNLOAD_DELAY': 2,
 'HTTPCACHE_ENABLED': True,
 'LOG_FILE': 'index.txt',
 'NEWSPIDER_MODULE': 'src.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['src.spiders']}
2020-10-27 13:12:33 [scrapy.extensions.telnet] INFO: Telnet Password: 1e99422fb33906f7
2020-10-27 13:12:33 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-10-27 13:12:33 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats',
 'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware']
2020-10-27 13:12:33 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-10-27 13:12:33 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-10-27 13:12:33 [scrapy.core.engine] INFO: Spider opened
2020-10-27 13:12:33 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-10-27 13:12:33 [scrapy.extensions.httpcache] DEBUG: Using filesystem cache storage in /Users/yuya/develop/Sub/Python-sandbox/scrapy/.scrapy/httpcache
2020-10-27 13:12:33 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-10-27 13:12:33 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://blog.scrapinghub.com/robots.txt> from <GET http://blog.scrapinghub.com/robots.txt>
2020-10-27 13:12:33 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://blog.scrapinghub.com/robots.txt> (referer: None) ['cached']
2020-10-27 13:12:33 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://blog.scrapinghub.com/> from <GET http://blog.scrapinghub.com/>
2020-10-27 13:12:33 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://blog.scrapinghub.com/> (referer: None) ['cached']
2020-10-27 13:12:33 [scrapy.core.scraper] DEBUG: Scraped from <200 https://blog.scrapinghub.com/>
{'data': 'サンプルデータ', 'title': 'タイトル', 'url': 'localhost:8000'}
2020-10-27 13:12:33 [scrapy.core.engine] INFO: Closing spider (finished)
2020-10-27 13:12:33 [scrapy.extensions.feedexport] INFO: Stored csv feed (1 items) in: index.csv
2020-10-27 13:12:33 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 1272,
 'downloader/request_count': 4,
 'downloader/request_method_count/GET': 4,
 'downloader/response_bytes': 14000,
 'downloader/response_count': 4,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/301': 2,
 'elapsed_time_seconds': 0.159262,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 10, 27, 4, 12, 33, 532495),
 'httpcache/hit': 4,
 'item_scraped_count': 1,
 'log_count/DEBUG': 6,
 'log_count/INFO': 11,
 'memusage/max': 53985280,
 'memusage/startup': 53981184,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 10, 27, 4, 12, 33, 373233)}
2020-10-27 13:12:33 [scrapy.core.engine] INFO: Spider closed (finished)
2020-10-27 13:19:08 [scrapy.utils.log] INFO: Scrapy 2.4.0 started (bot: src)
2020-10-27 13:19:08 [scrapy.utils.log] INFO: Versions: lxml 4.6.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.8 (default, Sep 21 2020, 21:58:35) - [Clang 11.0.0 (clang-1100.0.33.16)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1h  22 Sep 2020), cryptography 3.2, Platform Darwin-18.7.0-x86_64-i386-64bit
2020-10-27 13:19:08 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-10-27 13:19:08 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'src',
 'DOWNLOAD_DELAY': 2,
 'HTTPCACHE_ENABLED': True,
 'LOG_FILE': 'logging.py',
 'NEWSPIDER_MODULE': 'src.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['src.spiders']}
2020-10-27 13:19:08 [scrapy.extensions.telnet] INFO: Telnet Password: 151b3a6743a3e801
2020-10-27 13:19:08 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-10-27 13:19:08 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats',
 'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware']
2020-10-27 13:19:08 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-10-27 13:19:08 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-10-27 13:19:08 [scrapy.core.engine] INFO: Spider opened
2020-10-27 13:19:08 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-10-27 13:19:08 [scrapy.extensions.httpcache] DEBUG: Using filesystem cache storage in /Users/yuya/develop/Sub/Python-sandbox/scrapy/.scrapy/httpcache
2020-10-27 13:19:08 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-10-27 13:19:08 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://job.mynavi.jp/robots.txt> (referer: None) ['cached']
2020-10-27 13:19:08 [scrapy.core.engine] DEBUG: Crawled (405) <GET https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/doSearchTypeIndustryArea> (referer: None) ['cached']
2020-10-27 13:19:08 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <405 https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/doSearchTypeIndustryArea>: HTTP status code is not handled or not allowed
2020-10-27 13:19:08 [scrapy.core.engine] INFO: Closing spider (finished)
2020-10-27 13:19:08 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 552,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 23853,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/405': 1,
 'elapsed_time_seconds': 0.142149,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 10, 27, 4, 19, 8, 432228),
 'httpcache/hit': 2,
 'httperror/response_ignored_count': 1,
 'httperror/response_ignored_status_count/405': 1,
 'log_count/DEBUG': 3,
 'log_count/INFO': 11,
 'memusage/max': 53821440,
 'memusage/startup': 53817344,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2020, 10, 27, 4, 19, 8, 290079)}
2020-10-27 13:19:08 [scrapy.core.engine] INFO: Spider closed (finished)
2020-10-27 13:19:18 [scrapy.utils.log] INFO: Scrapy 2.4.0 started (bot: src)
2020-10-27 13:19:18 [scrapy.utils.log] INFO: Versions: lxml 4.6.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.8 (default, Sep 21 2020, 21:58:35) - [Clang 11.0.0 (clang-1100.0.33.16)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1h  22 Sep 2020), cryptography 3.2, Platform Darwin-18.7.0-x86_64-i386-64bit
2020-10-27 13:19:18 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-10-27 13:19:18 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'src',
 'DOWNLOAD_DELAY': 2,
 'HTTPCACHE_ENABLED': True,
 'LOG_FILE': 'logging.py',
 'NEWSPIDER_MODULE': 'src.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['src.spiders']}
2020-10-27 13:19:18 [scrapy.extensions.telnet] INFO: Telnet Password: 83a2f0638633a4fc
2020-10-27 13:19:19 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-10-27 13:19:19 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats',
 'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware']
2020-10-27 13:19:19 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-10-27 13:19:19 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-10-27 13:19:19 [scrapy.core.engine] INFO: Spider opened
2020-10-27 13:19:19 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-10-27 13:19:19 [scrapy.extensions.httpcache] DEBUG: Using filesystem cache storage in /Users/yuya/develop/Sub/Python-sandbox/scrapy/.scrapy/httpcache
2020-10-27 13:19:19 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-10-27 13:19:19 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://job.mynavi.jp/robots.txt> (referer: None) ['cached']
2020-10-27 13:19:19 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://job.mynavi.jp/> (referer: None)
2020-10-27 13:19:19 [scrapy.core.scraper] DEBUG: Scraped from <200 https://job.mynavi.jp/>
{'data': 'サンプルデータ', 'title': 'タイトル', 'url': 'localhost:8000'}
2020-10-27 13:19:19 [scrapy.core.engine] INFO: Closing spider (finished)
2020-10-27 13:19:19 [scrapy.extensions.feedexport] INFO: Stored csv feed (1 items) in: index.csv
2020-10-27 13:19:19 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 495,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6098,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 0.235797,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 10, 27, 4, 19, 19, 306251),
 'httpcache/firsthand': 1,
 'httpcache/hit': 1,
 'httpcache/miss': 1,
 'httpcache/store': 1,
 'item_scraped_count': 1,
 'log_count/DEBUG': 4,
 'log_count/INFO': 11,
 'memusage/max': 54181888,
 'memusage/startup': 54177792,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2020, 10, 27, 4, 19, 19, 70454)}
2020-10-27 13:19:19 [scrapy.core.engine] INFO: Spider closed (finished)
