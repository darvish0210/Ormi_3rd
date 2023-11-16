from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from accounts.models import User

class Test(TestCase):
    def test_connection(self):
        
        # 접속확인
        print('# 접속확인 테스트')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

### 상속확인
# 위 4개 페이지에서 header, body, footer가 제대로 상속 되는지 확인


def test_tag(self):
        print('# 상속 확인')

        ## ./
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertEqual(None, headbar)

        # bodybar = soup.body
        # self.assertIn('index', bodybar.text)

        # footer = soup.footer
        # self.assertIn(None, footer)

        ## /about/
        response = self.client.get('/about/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertIn('Document', headbar.text)

        bodybar = soup.body
        self.assertIn('about', bodybar.text)

        # footer = soup.footer
        # self.assertIn(None, footer)


        ## /contact/
        response = self.client.get('/contact/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertIn('Document', headbar.text)

        bodybar = soup.body
        self.assertIn('contact', bodybar.text)

        # footer = soup.footer
        # self.assertIn(None, footer)
        
        ## /blog/
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertIn('Blog', headbar.text)

        bodybar = soup.body
        self.assertIn('blog', bodybar.text)

        # footer = soup.footer
        # self.assertIn(None, footer)
        


'''
### 게시물 리스트 확인
   - 게시물이 없으면 ‘게시물이 존재하지 않습니다. 첫번째 게시물에 주인공이 되세요!’가 출력되어야 합니다.
   
   
   - 게시물이 있으면 h2가 1개 이상이어야 합니다.
   - 게시물 작성은 아래 구조로 되어 있습니다.
   

'''


def test_post_list(self):
        print('# 게시물 리스트 확인')
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')

        if Post.objects.count() == 0:
            print('게시물이 없는 경우')
            self.assertIn('아직 게시물이 없습니다.', soup.body.text)
        else:
            print('게시물이 있는 경우')
            print(Post.objects.count())
            print(len(soup.body.select('h2')))
            self.assertGreater(len(soup.body.select('h2')), 1) # h2태그가 1개 이상
'''
### 게시물 상세페이지 확인
   - 제목 자리에 제목이 들어있는지
   - 내용 자리에 내용이 들어있는지
   - 최종 수정 날짜에 수정날짜가 들어가 있는지
   - 상속이 제대로 이뤄져 있는지
   	- 메뉴, 푸터

'''

def test_post_detail(self):
        print('게시물 상세페이지 확인')
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World.',
            author = self.user_hojun
        )

        # 상세페이지 정상적으로 불러오는지 확인
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        detail = soup.body.main.text
        detail_content = detail.split('\n')

        # 제목 자리에 제목이 들어있는지
        self.assertEqual(detail_content[1], '첫 번째 포스트입니다.')
        
        # 내용 자리에 내용이 들어있는지
        self.assertEqual(detail_content[2], 'Hello World.')

        # 최종 수정 날짜에 수정날짜가 들어가 있는지
        self.assertIn(detail_content[3][:-8], post_001.updated_at.strftime('%Y년 %m월 %d일'))
        
        # 상속이 제대로 이뤄져 있는지
        navbar = soup.nav
        self.assertIn('Home', navbar.text)
        self.assertIn('About', navbar.text)
        self.assertIn('Blog', navbar.text)