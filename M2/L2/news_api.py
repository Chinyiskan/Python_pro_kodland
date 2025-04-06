import datetime
from newsapi.newsapi_client import NewsApiClient

class NewsAPIWrapper:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key=api_key)
        self.categories = {
            "medioambiente": "environment",
            "cambio_climatico": "climate change",
            "reciclaje": "recycling"
        }
    
    def get_news(self, categoria, page_size=5):
        if categoria not in self.categories:
            raise ValueError("Categoría no válida.")
        query = self.categories[categoria]
        fecha_desde = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        response = self.newsapi.get_everything(
            q=query,
            language='es',
            from_param=fecha_desde,
            sort_by='relevancy',
            page_size=page_size
        )
        return response
