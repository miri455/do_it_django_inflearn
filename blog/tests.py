from django.test import TestCase
from bs4 import BeautifulSoup
from .models import Post

class TestView(TestCase):
    def setUP(self):
        self.client = Client()

    def test_post_list(self):
        self.assertEqual(2,2)
        # 1.1 open post list
        response = self.client.get('/blog/')
        # 1.2 load page normally
        self.assertEqual(response.status_code, 200)
        # 1.3 'Blog' is included on page title
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn('Blog',soup.title.text)
        # 1.4 has a NavBar
        navbar = soup.nav
        # 1.5 Blog,About me are included on NavBar
        self.assertIn('Blog', navbar.text)
        self.assertIn('About me', navbar.text)

        # 2.1 when no any post
        self.assertEqual(Post.objects.count(), 0)
        # 2.2 show "pany post is not yet" on main part
        main_area = soup.find('div', id='main-area')
        self.assertIn('any post is not yet', main_area.text)

        # 3.1 if you have 2 posts,
        post_001 = Post.objects.create(
            title = 'This is first post',
            content = 'Hello world. We are the World.',
        )

        post_002 = Post.objects.create(
            title='This is second post',
            content='I like chinese foods',
        )
        self.assertEqual(Post.objects.count(),2)

        # 3.2 when refresh post list page,
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        # 3.3 2titles are on the main part
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 3.4 no "any post is not yet"
        self.assertNotIn('any post is not yet', main_area.text)

# Create your tests here.
