import unittest
import CRUD


class TestCRUD(unittest.TestCase):
    def test_AddPost(self):
        post = self.app.addPost(**self.param)
        self.assertEqual(post.author, self.param["author"])
        self.assertEqual(post.post, self.param["post"])

    def test_GetPost(self):
        post = self.app.addPost(**self.param)

        retrievedPost = self.app.getPost(post.id)
        self.assertEqual(retrievedPost, post)

    def test_Bug_Id_is_not_added_to_post(self):
        post = self.app.addPost(**self.param)
        self.assertIsInstance(post.id, int)
        
    def test_SavingAndLoading(self):
        self.data = []
        for i in range(2814):
            post = self.app.addPost(**self.param)
            self.data.append(post)
        
        self.app.save()
        
        app2 = CRUD.App()
        app2.load()

        for post in self.data:
            app2.getPost(post.id)

    def test_DeletePost(self):
        post = self.app.addPost(**self.param)
        self.app.delete(post.id)
        
        with self.assertRaises(CRUD.POSTNOTFOUND):
            self.app.getPost(post.id)

    def test_GetAllPost(self):
        for i in range(2814):
            self.app.addPost(**self.param)
        
        posts = self.app.getAllPosts()
        self.assertEqual(len(posts), 2814)

    def test_GetInvalidPost(self):
        with self.assertRaises(CRUD.POSTNOTFOUND):
            self.app.getPost(2814)

    def test_LoadTwice(self):
        for i in range(2814):
            self.app.addPost(**self.param)
        
        self.app.save()
        
        app2 = CRUD.App()
        app2.load()
        app2.load()
        
        posts = app2.getAllPosts()
        self.assertEqual(len(posts), 2814)

    def setUp(self):
        self.app = CRUD.App()
        self.param = {
            "author": "Anonymous",
            "post": "Hello world",
        }

#    def tearDown(self):
#        self.fail()


if __name__ == '__main__':
    unittest.main()