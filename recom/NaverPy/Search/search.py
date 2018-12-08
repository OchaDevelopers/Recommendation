from ..naverpy import NaverPy
from ..Exceptions import InvalidParameterException


class Search(NaverPy):

    def __init__(self, client_id='', secret=''):
        super().__init__(client_id=client_id, secret=secret)

    def blog(self, query, display=10, start=1, sort='sim'):
        '''
        Naver API > 검색 > 블로그
        reference : https://developers.naver.com/docs/search/blog/
        sort => ['sim', 'date']
        '''
        if sort not in ['sim', 'date']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/blog.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def news(self, query, display=10, start=1, sort='sim'):
        '''
        Naver API > 검색 > 뉴스
        reference : https://developers.naver.com/docs/search/news/
        sort => ['sim', 'date']
        '''
        if sort not in ['sim', 'date']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/news.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def book(self, query, display=10, start=1, sort='sim'):
        '''
        Naver API > 검색 > 책
        reference : https://developers.naver.com/docs/search/book/
        sort => ['sim', 'date']
        '''
        if sort not in ['sim', 'date']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/book.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def adult(self, query):
        '''
        Naver API > 검색 > 성인 검색어 판별
        reference : https://developers.naver.com/docs/search/adult/
        '''
        url = 'https://openapi.naver.com/v1/search/adult.json?query={0}'.format(query)
        return self._get(url, headers=self.headers)

    def encyc(self, query, display=10, start=1):
        '''
        Naver API > 검색 > 백과사전
        reference : https://developers.naver.com/docs/search/encyclopedia/
        '''
        url = 'https://openapi.naver.com/v1/search/encyc.json?query={0}&display={1}&start={2}'.format(query, display, start)
        return self._get(url, headers=self.headers)

    def movie(self, query, display=10, start=1, genre='', country='', yearfrom='', yearto=''):
        '''
        Naver API > 검색 > 영화
        reference : https://developers.naver.com/docs/search/movie/
        genre => 1 ~ 28
        country => ['KR', 'JP', 'US', 'HK', 'GB', 'FR', 'ETC']
        yearfrom => 4자리 정수 (연도)
        yearto => 4자리 정수 (연도)
        '''
        if country not in ['KR', 'JP', 'US', 'HK', 'GB', 'FR', 'ETC']:
            raise InvalidParameterException('Invalid parameter \'country\'')
        if (yearfrom == '' and yearto != '') or (yearfrom != '' and yearto == ''):
            raise InvalidParameterException('Use both Parameter \'yearfrom\' & \'yearto\'.')
        url = 'https://openapi.naver.com/v1/search/movie.json?query={0}&display={1}&start={2}&genre={3}&country={4}&yearfrom={5}&yearto={6}'.format(query, display, start, genre, country, yearfrom, yearto)
        return self._get(url, headers=self.headers)

    def cafearticle(self, query, display=10, start=1, sort='sim'):
        '''
        Naver API > 검색 > 카페 글
        reference : https://developers.naver.com/docs/search/cafearticle/
        sort => ['sim', 'date']
        '''
        if sort not in ['sim', 'date']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/cafearticle.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def kin(self, query, display=10, start=1, sort='sim'):
        '''
        Naver API > 검색 > 지식 in
        reference : https://developers.naver.com/docs/search/kin/
        sort => ['sim', 'date', 'point']
        '''
        if sort not in ['sim', 'date', 'point']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/kin.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def local(self, query, display=10, start=1, sort='random'):
        '''
        Naver API > 검색 > 지역
        reference : https://developers.naver.com/docs/search/local/
        sort => ['random', 'comment']
        '''
        if sort not in ['random', 'comment']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/local.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def errata(self, query):
        '''
        Naver API > 검색 > 오타변환
        reference : https://developers.naver.com/docs/search/errata/
        '''
        url = 'https://openapi.naver.com/v1/search/errata.json?query={0}'.format(query)
        return self._get(url, headers=self.headers)

    def webkr(self, query, display=10, start=1):
        '''
        Naver API > 검색 > 웹문서
        reference : https://developers.naver.com/docs/search/web/
        '''
        url = 'https://openapi.naver.com/v1/search/webkr.json?query={0}&display={1}&start={2}'.format(query, display, start)
        return self._get(url, headers=self.headers)

    def image(self, query, display=10, start=1, sort='sim', filter='all'):
        '''
        Naver API > 검색 > 이미지
        reference : https://developers.naver.com/docs/search/image/
        sort => ['sim', 'date']
        filter => ['all', 'large', 'medium', 'small']
        '''
        if sort not in ['sim', 'date']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        if filter not in ['all', 'large', 'medium', 'small']:
            raise InvalidParameterException('Invalid parameter \'filter\'')
        url = 'https://openapi.naver.com/v1/search/image.json?query={0}&display={1}&start={2}&sort={3}&filter={4}'.format(query, display, start, sort, filter)
        return self._get(url, headers=self.headers)

    def shop(self, query, display=10, start=1, sort='sim'):
        '''
        Naver API > 검색 > 쇼핑
        reference : https://developers.naver.com/docs/search/shopping/
        sort => ['sim', 'date', 'asc', 'dsc']
        '''
        if sort not in ['sim', 'date', 'asc', 'dsc']:
            raise InvalidParameterException('Invalid parameter \'sort\'')
        url = 'https://openapi.naver.com/v1/search/shop.json?query={0}&display={1}&start={2}&sort={3}'.format(query, display, start, sort)
        return self._get(url, headers=self.headers)

    def doc(self, query, display=10, start=1):
        '''
        Naver API > 검색 > 전문자료
        reference : https://developers.naver.com/docs/search/doc/
        '''
        url = 'https://openapi.naver.com/v1/search/doc.json?query={0}&display={1}&start={2}'.format(query, display, start)
        return self._get(url, headers=self.headers)
