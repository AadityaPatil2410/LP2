import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        
        i=0
        while(i<10):
            self.response.write(str(i+1)+")Name: Aditya Patil<br>")
            self.response.write("Seat Number: 33256<br>")
            #elf.response.write("Department: IT<br>")
            self.response.write('<br>')
            i+=1
        

app =webapp2.WSGIApplication([('/',MainPage)],debug=True)

#cloud terminal command : py google-cloud-sdk/bin/dev_appserver.py C:\Users\sahil\CCL_trial\1_to_3\app.yaml
