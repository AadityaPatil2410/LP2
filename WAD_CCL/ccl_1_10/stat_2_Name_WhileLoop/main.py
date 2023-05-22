import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        #self.response.write("Hello World")
        #i=0
        #while(i<10):
            #self.response.write("Name: Aditya Patil<br>")
            #self.response.write("Seat Number: 33256<br>")
            #self.response.write("Department: IT<br>")
            #self.response.write('<br>')
            #i+=1
        for x in range(5):
        	self.response.write(str(x+1)+")")
        	self.response.write("Name: Aditya Patil<br>")
        	self.response.write("  Seat No: T190058658<br>")
        	self.response.write("  Dept: IT<br>")
        	self.response.write("<br>")

app =webapp2.WSGIApplication([('/',MainPage)],debug=True)

#cloud terminal command : py google-cloud-sdk/bin/dev_appserver.py C:\Users\sahil\CCL_trial\1_to_3\app.yaml
