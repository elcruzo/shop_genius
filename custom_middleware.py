import scrapy
import time


class MyCustomException(Exception):
    def __init__(self, message="A custom exception occurred"):
        self.message = message
        super().__init__(self.message)

class CustomMiddleware:
    def __init__(self, settings):
        
        self.settings = settings
        

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        
        middleware = cls(crawler.settings)
        return middleware

    def process_request(self, request, spider):
        delay = self.settings.getfloat('DOWNLOAD_DELAY', 0)
        if delay > 0:
            time.sleep(delay)

    def process_response(self, request, response, spider):
        
        if response.status == 200:
            data = response.css('your-css-selector::text').get()
            
            return response

        elif response.status == 404:
            self.logger.error(f'Page not found: {request.url}')
            

        elif response.status == 503:  
            self.logger.warning(f'Service unavailable: {request.url}')
            
        return response

    def process_exception(self, request, exception, spider):
        # Log the exception for debugging purposes
        self.logger.error(f'Exception occurred while processing {request.url}: {str(exception)}')

        
        if isinstance(exception, MyCustomException):           
            self.logger.error(f'Custom exception occurred: {str(exception)}')
           

        elif isinstance(exception, TimeoutError):
            self.logger.warning(f'Timeout error occurred: {str(exception)}')
            

        elif isinstance(exception, ConnectionError):  
            self.logger.error(f'Connection error occurred: {str(exception)}')
            

        return scrapy.http.HtmlResponse(url=request.url, status=500, body='Unknown Error Ocurred')

