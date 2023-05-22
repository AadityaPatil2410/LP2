import webapp2
import urllib2
# import urllib.parse
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>')
        self.response.write('<h1>Search For University From its Name</h1>')
        self.response.write('<form action="/details" method="post" >')
        self.response.write('<h2>Name of University:</h2> <input type="text" name="uni">  <br><br>')
        self.response.write('<input type="submit" value="Search">')
        self.response.write('</form></body></html>')

class UniversityDetailsHandler(webapp2.RequestHandler):
    def post(self):
        uni = self.request.get('uni')
        encoded_name = urllib2.quote(uni)

        url = 'http://universities.hipolabs.com/search?name=' + encoded_name
        data = urllib2.urlopen(url).read()
        data_dict = json.loads(data)
        self.response.write('<h1>University Data</h1> <br>')
        for i in range(len(data_dict)):
            web= data_dict[i]['web_pages'][0]
            self.response.write('<html><body>')
            self.response.write(str(i+1)+ ") ")
            self.response.write('Web Page: ' + str(web) + '<br>')
            self.response.write('Country: ' + data_dict[i]['country'] + '<br>')
            self.response.write('Domain: ' + str(data_dict[i]['domains'][0]) + '<br>')
            self.response.write('Name: ' + data_dict[i]['name'] + '<br>')
            self.response.write('<br><br>')
        self.response.write('</html></body>')

app = webapp2.WSGIApplication([('/',MainPage),('/details' , UniversityDetailsHandler)],debug= True)        
