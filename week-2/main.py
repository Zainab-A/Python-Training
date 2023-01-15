class book:
    def __init__(self,t,a,pub,pri,cpy=0):
        self.title=t
        self.author=a
        self.publisher=pub
        self.price=pri
        self.copies=cpy
    def get_title(self):
        return self._title
    def set_title(self, t):
        self._title=t
        return
    title=property(get_title, set_title)
    def get_author(self):
        return self._author
    def set_author(self, a):
        self._author=a
        return
    author=property(get_author, set_author)
    def get_publisher(self):
        return self._publisher
    def set_publisher(self, pub):
        self._publisher=pub
        return
    publisher=property(get_publisher, set_publisher)
    def get_price(self):
        return self._price
    def set_price(self,pri):
        self._price=pri
        return
    price=property(get_price, set_price)
    def get_copies(self):
        return self._copies
    def set_copies(self,cpy):
        self._copies=cpy
        return
    copies=property(get_copies, set_copies)
    def get_royalty(self):
        if self.copies<=500:
            self._royalty=self.copies*self.price*10/100
        elif self.copies<=1000:
            self._royalty=500*self.price*10/100+(self.copies-500)*self.price*12.5/100
        else:
            self._royalty=500*self.price*10/100 + 500*self.price*12.5/100 +  (self.copies-1000)*self.price*15/100
        return self._royalty
class ebook(book):
    def __init__(self,t, a, pub, pri, cpy=0, form=None):
        super().__init__(t,a,pub,pri,cpy)
        self.format=form
    def get_format(self):
        return self._format
    def set_format(self, form):
        self._format=form
        return
    format=property(get_format, set_format)
    def get_royalty(self):
        royal=super().get_royalty()
        royal=royal-royal*12/100
        self._royalty=royal
        return self._royalty
if __name__== "__main__":
    print ('print book example')
    b1=book('Harry Potter','J.K Rowling',"Bloomsbury",499,600)
    print ("Royalty earned : ", b1.get_royalty())
    print ('ebook example')
    e1=ebook('Harry Potter','J.K. Rowling',"Bloomsbury",200, 100, 'PDF')
    print ('Royalty earned' , e1.get_royalty())
