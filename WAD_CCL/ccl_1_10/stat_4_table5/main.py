"""
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
    	i = 1
        while(i<11):
        	if i == 10:	
            	self.response.write(str(5) + str(" X ") + str(i) + "__" + str("= ") + str(5*i) + "<br>")  	
            else:           	
            	self.response.write(str(5) + str(" X ") + str(i) + "___" + str("= ") + str(5*i) + "<br>")
            i +=1
        

app =webapp2.WSGIApplication([('/',MainPage)],debug=True)

#cloud terminal command : py google-cloud-sdk/bin/dev_appserver.py C:\Users\sahil\CCL_trial\1_to_3\app.yaml


"""
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        i = 1
        while i < 11:
            if i == 10:
                self.response.write(str(5) + str(" X ") + str(i) + "__" + str("= ") + str(5*i) + "<br>")
            else:
                self.response.write(str(5) + str(" X ") + str(i) + "___" + str("= ") + str(5*i) + "<br>")
            i += 1

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


