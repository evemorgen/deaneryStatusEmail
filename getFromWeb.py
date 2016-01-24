__author__ = 'evemorgen'
import urllib, urllib2, cookielib
from cookielib import CookieJar
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import codecs
import os
import csv

from sekret import *

# -*- coding: utf-8 -*-

#sciaganie HTML ze strony
def getHTMLdziekanat():
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    cookies = cookielib.CookieJar()
    uri = 'https://dziekanat.agh.edu.pl/Logowanie2.aspx?ReturnUrl=%2fOcenyP.aspx'
    headers = {
        'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
        'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    formFields = (
        (r'ctl00_ctl00_ScriptManager1_HiddenField',r''),
        (r'__EVENTTARGET',r''),
        (r'__EVENTARGUMENT',r''),
        (r'__VIEWSTATE',r'/wEPDwUKLTczODIwNjU2MA8WBB4KbnJTZW1lc3RydQICHh9JbmRla3NLb2x1bW55UG9Pc3RhdG5pbVRlcm1pbmllAg0WAmYPZBYCZg9kFgRmD2QWAgIJD2QWAgIDDw8WAh4HVmlzaWJsZWhkZAIBD2QWBAICD2QWBGYPZBYCAgIPFCsAAhQrAAIPFgQeC18hRGF0YUJvdW5kZx4XRW5hYmxlQWpheFNraW5SZW5kZXJpbmdoZGRkZAIBD2QWAgICDxQrAAIUKwACDxYEHwNnHwRoZA8UKwABFCsAAg8WCB4EVGV4dAUHV3lsb2d1ah4LTmF2aWdhdGVVcmwFDS9XeWxvZ3VqLmFzcHgeBVZhbHVlBQdXeWxvZ3VqHgdUb29sVGlwBRVXeWxvZ293dWplIHogc2Vyd2lzdS5kZA8UKwEBZhYBBXRUZWxlcmlrLldlYi5VSS5SYWRNZW51SXRlbSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAxMi4zLjEyMDUuMzUsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MTIxZmFlNzgxNjViYTNkNGQWAmYPDxYIHwUFB1d5bG9ndWofBgUNL1d5bG9ndWouYXNweB8HBQdXeWxvZ3VqHwgFFVd5bG9nb3d1amUgeiBzZXJ3aXN1LmRkAgQPZBYEZg9kFgJmDxQrAAIUKwACDxYIHg1EYXRhVGV4dEZpZWxkBQRUZXh0HhREYXRhTmF2aWdhdGVVcmxGaWVsZAULTmF2aWdhdGVVcmwfA2cfBGhkDxQrAAkUKwACDxYEHwUFFEVsZWt0cm9uaWN6bnkgaW5kZWtzHwYFASNkEBYKZgIBAgICAwIEAgUCBgIHAggCCRYKFCsAAg8WBB8FBQxEYW5lIG9zb2Jvd2UfBgULV3luaWsyLmFzcHhkZBQrAAIPFgQfBQUMVG9rIHN0dWRpw7N3HwYFD1Rva1N0dWRpb3cuYXNweGRkFCsAAg8WBB8FBRFQcnplYmllZyBzdHVkacOzdx8GBRRQcnplYmllZ1N0dWRpb3cuYXNweGRkFCsAAg8WBB8FBQVPY2VueR8GBQtPY2VueVAuYXNweGRkFCsAAg8WBB8FBQhQcmFrdHlraR8GBQ1QcmFrdHlraS5hc3B4ZGQUKwACDxYEHwUFDE5hZ3JvZHkvS2FyeR8GBRBOYWdyb2R5S2FyeS5hc3B4ZGQUKwACDxYEHwUFD1ByYWNhIGR5cGxvbW93YR8GBQ1QcmFjYUR5cC5hc3B4ZGQUKwACDxYEHwUFFcWad2lhZGVjdHdvIG9kZWrFm2NpYR8GBRdTd2lhZGVjdHdvT2RlanNjaWEuYXNweGRkFCsAAg8WBB8FBRVLb250YWt0IHogRHppZWthbmF0ZW0fBgUORHppZWthbmF0LmFzcHhkZBQrAAIPFgQfBQUOV3lkcnVrIGluZGVrc3UfBgUSV3lkcnVrSW5kZWtzdS5hc3B4ZGQPFgpmZmZmZmZmZmZmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0FCsAAg8WBB8FBQxUd29qZSBzdHVkaWEfBgUBI2QQFgdmAgECAgIDAgQCBQIGFgcUKwACDxYEHwUFD1BvZHppYcWCIGdvZHppbh8GBQ9Qb2R6R29kemluLmFzcHhkZBQrAAIPFgQfBQUXV3lkcnVrIHBvZHppYcWCdSBnb2R6aW4fBgUSUG9kekdvZHpEcnVrMC5hc3B4ZGQUKwACDxYEHwUFEE9jZW55IGN6xIVzdGtvd2UfBgUPT2NlbnlDemFzdC5hc3B4ZGQUKwACDxYEHwUFCVN0eXBlbmRpYR8GBQ5TdHlwZW5kaWEuYXNweGRkFCsAAg8WBB8FBQ9Nb2R1xYJ5IGkgZ3J1cHkfBgUQTW9kdWx5R3J1cHkuYXNweGRkFCsAAg8WBB8FBQtQcm93YWR6xIVjeR8GBQ9Qcm93YWR6YWN5LmFzcHhkZBQrAAIPFgQfBQUNUGxhbiBzdHVkacOzdx8GBRBQbGFuU3R1ZGlvdy5hc3B4ZGQPFgdmZmZmZmZmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0FCsAAg8WBB8FBRNXeWLDs3IgcHJ6ZWRtaW90w7N3HwYFF1d5Ym9yUHJ6ZWRtaW90b3dDQy5hc3B4ZGQUKwACDxYEHwUFFFR3b2plIGRhbmUgZmluYW5zb3dlHwYFASNkEBYDZgIBAgIWAxQrAAIPFgQfBQUNS29udGEgYmFua293ZR8GBRFLb250YUJhbmtvd2UuYXNweGRkFCsAAg8WBB8FBRROYWxpY3plbmlhIGkgd3DFgmF0eR8GBQ9Ld2VzdHVyYUNDLmFzcHhkZBQrAAIPFgQfBQUHV3DFgmF0eR8GBQtXcGxhdHkuYXNweGRkDxYDZmZmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0FCsAAg8WBB8FBQtPZ8WCb3N6ZW5pYR8GBQ9PZ2xvc3plbmlhLmFzcHhkZBQrAAIPFgQfBQUKVXN0YXdpZW5pYR8GBQEjZBAWAWYWARQrAAIPFgQfBQUNWm1pYW5hIGhhc8WCYR8GBRBabWlhbmFIYXNsYS5hc3B4ZGQPFgFmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0FCsAAg8WBB8FBQdBbmtpZXR5HwYFEnN0YXJ0LmFzcHg/dHlwPWFua2RkFCsAAg8WBB8FBQ5EYW5lIGRvZGF0a293ZR8GBRJEYW5lRG9kYXRrb3dlLmFzcHhkZBQrAAIPFgQfBQUHV3lsb2d1ah8GBQxXeWxvZ3VqLmFzcHhkZA8UKwEJZmZmZmZmZmZmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ZBYSZg8PFgQfBQUURWxla3Ryb25pY3pueSBpbmRla3MfBgUBI2QWFGYPDxYEHwUFDERhbmUgb3NvYm93ZR8GBQtXeW5pazIuYXNweGRkAgEPDxYEHwUFDFRvayBzdHVkacOzdx8GBQ9Ub2tTdHVkaW93LmFzcHhkZAICDw8WBB8FBRFQcnplYmllZyBzdHVkacOzdx8GBRRQcnplYmllZ1N0dWRpb3cuYXNweGRkAgMPDxYEHwUFBU9jZW55HwYFC09jZW55UC5hc3B4ZGQCBA8PFgQfBQUIUHJha3R5a2kfBgUNUHJha3R5a2kuYXNweGRkAgUPDxYEHwUFDE5hZ3JvZHkvS2FyeR8GBRBOYWdyb2R5S2FyeS5hc3B4ZGQCBg8PFgQfBQUPUHJhY2EgZHlwbG9tb3dhHwYFDVByYWNhRHlwLmFzcHhkZAIHDw8WBB8FBRXFmndpYWRlY3R3byBvZGVqxZtjaWEfBgUXU3dpYWRlY3R3b09kZWpzY2lhLmFzcHhkZAIIDw8WBB8FBRVLb250YWt0IHogRHppZWthbmF0ZW0fBgUORHppZWthbmF0LmFzcHhkZAIJDw8WBB8FBQ5XeWRydWsgaW5kZWtzdR8GBRJXeWRydWtJbmRla3N1LmFzcHhkZAIBDw8WBB8FBQxUd29qZSBzdHVkaWEfBgUBI2QWDmYPDxYEHwUFD1BvZHppYcWCIGdvZHppbh8GBQ9Qb2R6R29kemluLmFzcHhkZAIBDw8WBB8FBRdXeWRydWsgcG9kemlhxYJ1IGdvZHppbh8GBRJQb2R6R29kekRydWswLmFzcHhkZAICDw8WBB8FBRBPY2VueSBjesSFc3Rrb3dlHwYFD09jZW55Q3phc3QuYXNweGRkAgMPDxYEHwUFCVN0eXBlbmRpYR8GBQ5TdHlwZW5kaWEuYXNweGRkAgQPDxYEHwUFD01vZHXFgnkgaSBncnVweR8GBRBNb2R1bHlHcnVweS5hc3B4ZGQCBQ8PFgQfBQULUHJvd2FkesSFY3kfBgUPUHJvd2FkemFjeS5hc3B4ZGQCBg8PFgQfBQUNUGxhbiBzdHVkacOzdx8GBRBQbGFuU3R1ZGlvdy5hc3B4ZGQCAg8PFgQfBQUTV3liw7NyIHByemVkbWlvdMOzdx8GBRdXeWJvclByemVkbWlvdG93Q0MuYXNweGRkAgMPDxYEHwUFFFR3b2plIGRhbmUgZmluYW5zb3dlHwYFASNkFgZmDw8WBB8FBQ1Lb250YSBiYW5rb3dlHwYFEUtvbnRhQmFua293ZS5hc3B4ZGQCAQ8PFgQfBQUUTmFsaWN6ZW5pYSBpIHdwxYJhdHkfBgUPS3dlc3R1cmFDQy5hc3B4ZGQCAg8PFgQfBQUHV3DFgmF0eR8GBQtXcGxhdHkuYXNweGRkAgQPDxYEHwUFC09nxYJvc3plbmlhHwYFD09nbG9zemVuaWEuYXNweGRkAgUPDxYEHwUFClVzdGF3aWVuaWEfBgUBI2QWAmYPDxYEHwUFDVptaWFuYSBoYXPFgmEfBgUQWm1pYW5hSGFzbGEuYXNweGRkAgYPDxYEHwUFB0Fua2lldHkfBgUSc3RhcnQuYXNweD90eXA9YW5rZGQCBw8PFgQfBQUORGFuZSBkb2RhdGtvd2UfBgUSRGFuZURvZGF0a293ZS5hc3B4ZGQCCA8PFgQfBQUHV3lsb2d1ah8GBQxXeWxvZ3VqLmFzcHhkZAIGD2QWBAIDDw8WAh8CaGRkAgcPZBYSAgEPEA8WBB8FBRZQb2thxbwgd3N6eXN0a2llIGZvcm15HwJoZGRkZAIFDw8WAh8CZ2QWBgIBDw8WAh8FBU1Qb3R3aWVyZHplbmllIHBvcHJhd25vxZtjaSBkYW55Y2ggbW/FvGVzeiBkb2tvbmHEhyBkbyBkbmlhOiA8Yj4yNC4wMi4yMDE2PC9iPmRkAgIPEA8WAh8FBUBQb3R3aWVyZHphbSBwcmF3aWTFgm93b8WbxIcgaSBrb21wbGV0bm/Fm8SHIHdwcm93YWR6b255Y2ggZGFueWNoZGRkZAIDDw8WAh8FBQ1aYXBpc3ogd3liw7NyZGQCBw9kFgICAQ8PFgIfBQWvATxwPlR5cCBwcnplZG1pb3R1OjwvcD48cD5QIC0gcG9kc3Rhd293eS9vYm93acSFemtvd3k8L3A+PHA+RSAtIG9iaWVyYWxueTwvcD48cD5EIC0gZG9kYXRrb3d5PC9wPjxwPlIgLSByw7PFvG5pY2UgcHJvZ3JhbW93ZTwvcD48cD5QUCAtIHBvd3RhcnphbmllIHByemVkbWlvdHU8L3A+PHA+SSAtIElUUzwvcD5kZAIJDxYCHglpbm5lcmh0bWwFgAHFmnJlZG5pYSB3YcW8b25hIHogb2NlbiB1enlza2FueWNoIHphIHNlbWVzdHI6IDxiciAvPsWacmVkbmlhIHdhxbxvbmEgeiBvY2VuIHV6eXNrYW55Y2ggemEgcm9rOiA8YnIgLz5aZ3JvbWFkem9uZSBwdW5rdHkgRUNUUzogMGQCCw8PFggfBQUXV3lkcnVrIHdwaXN1IGRvIGluZGVrc3UeCENzc0NsYXNzBQlwcnp5Y2lza00eBF8hU0ICAh8CaGRkAg0PDxYIHwUFF1d5ZHJ1ayB3cGlzdSBkbyBpbmRla3N1HwwFCXByenljaXNrTR8NAgIfAmhkZAIPDw8WCB8FBSNLYXJ0YSBPa3Jlc293eWNoIE9zacSFZ25pxJnEhyAtIERPQx8MBQlwcnp5Y2lza00fDQICHwJoZGQCEQ8PFggfBQUjS2FydGEgT2tyZXNvd3ljaCBPc2nEhWduacSZxIcgLSBQREYfDAUJcHJ6eWNpc2tNHw0CAh8CaGRkAhkPDxYCHwJoZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgQFNmN0bDAwJGN0bDAwJFRvcE1lbnVQbGFjZUhvbGRlciR3dW1hc3Rlck1lbnVUb3AkbWVudVRvcAUwY3RsMDAkY3RsMDAkVG9wTWVudVBsYWNlSG9sZGVyJE1lbnVUb3AyJG1lbnVUb3AyBTdjdGwwMCRjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkd3VtYXN0ZXJNZW51TGVmdCRyYWRNZW51BURjdGwwMCRjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkUmlnaHRDb250ZW50UGxhY2VIb2xkZXIkY2JfQWtjZXB0YWNqYYG6S+r1E5tgtvxWU7Xmgth1nvVK'),
        (r'__VIEWSTATEGENERATOR',r'/wEWBAKkm4nGDwLw5aCjAgK964KWDAKAnfm2CejLIfDJEFlspQpGL56W1Tmr1oXN'),
        (r'ctl00_ctl00_TopMenuPlaceHolder_TopMenuContentPlaceHolder_MenuTop3_menuTop3_ClientState',r''),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtHaslo',haslo),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtIdent',login),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$rbKto',r'student'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$butLoguj',r'Zaloguj'),
    )
    encodedFields = urllib.urlencode(formFields)
    response = opener.open(uri,encodedFields)
    thePage = response.read()
    return thePage

class CoolParser(HTMLParser):
    tabelka = ""
    def handle_starttag(self, tag, attrs):
        if(tag == "tr"):
            self.tabelka = self.tabelka + "\n"
    def handle_endtag(self, tag):
        if(tag == "td"):
            self.tabelka += ","
    # print "End tag  :", tag
    def handle_data(self, data):
        self.tabelka = self.tabelka + data
    def handle_comment(self, data):
        pass
        #print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        pass
        #print "Named ent:", c
    def handle_charref(self, name):
        pass
        #if name.startswith('x'):
        #    c = unichr(int(name[1:], 16))
        #else:
        #    c = unichr(int(name))
        #print "Num ent  :", c
    def handle_decl(self, data):
        pass
        #print "Decl     :", data
    def getTabelka(self):
        return self.tabelka


def stripGradeTable(stronka):
    return stronka[stronka.find('<table'):stronka.find('</table>')+len('</table>')]

def saveStringToFile(string, fileName):
    codecs.open(fileName,'w','utf-8').write(unicode(string,'utf-8'))

def getPrevGrades():
    if not os.path.isfile('stare.csv'):
        strona = getHTMLdziekanat()
        strona = stripGradeTable(strona)
        parser = CoolParser()
        parser.feed(strona)
        saveStringToFile(parser.getTabelka(),'stare.csv')
    else:
        strona = getHTMLdziekanat()
        strona = stripGradeTable(strona)
        parser = CoolParser()
        parser.feed(strona)
        saveStringToFile(parser.getTabelka(),'nowe.csv')

        with open('stare.csv', 'rb') as f:
            reader = csv.reader(f)
            stare = list(reader)

        with open('nowe.csv', 'rb') as f:
            reader = csv.reader(f)
            nowe = list(reader)

        string = ""

        for a,b in zip(nowe, stare):
            if cmp(a,b) != 0:
                for i in range(0,5):
                    if a[i] != "":
                        if(i > 1):
                            tmp = a[i]
                            string += tmp[0:3];
                        else:
                            string += a[i]
                    if i < 5 and a[i+1] != "":
                        string += " - "
                string += "\n"

        if string != "":
            strona = getHTMLdziekanat()
            strona = stripGradeTable(strona)
            parser = CoolParser()
            parser.feed(strona)
            saveStringToFile(parser.getTabelka(),'stare.csv')
        return string

def sendMail(tresc):
    email = mail
    adres = '| mailx -s \"Deanery status\" ' + "\"" + email + "\""
    open("tresc","w").write("Subject: Deanery status \nContent-Type: text/plain; charset=\"utf-8\" \n" + tresc)
    os.system('/usr/sbin/sendmail ' + mail + ' < tresc')
    print '/usr/sbin/sendmail ' + mail + ' < tresc'

a = getPrevGrades()
if a != "":
	sendMail(a)
os.system('rm nowe.csv')
