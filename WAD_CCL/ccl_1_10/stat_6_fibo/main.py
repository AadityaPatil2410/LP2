

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        i = 0
        f1=0
        f2=1
        while i < 8:
        	res=f1+f2
                self.response.write(str(res) +" ")
                f1=f2
                f2=res
                i+=1
            

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


