__author__ = 'evemorgen'
import urllib, urllib2, cookielib
from cookielib import CookieJar
import os

# -*- coding: utf-8 -*-

#Ściąganie HTML ze strony
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
        (r'__VIEWSTATE',r'/wEPDwUKMTgxMTA3NTE0Mw8WAh4DaGFzZRYCZg9kFgJmD2QWAgIBD2QWBAICD2QWAgIBD2QWAgIBD2QWAgICDxQrAAIUKwACDxYEHgtfIURhdGFCb3VuZGceF0VuYWJsZUFqYXhTa2luUmVuZGVyaW5naGQPFCsAARQrAAIPFggeBFRleHQFHVd5c3p1a2l3YXJrYSBwb2R6aWHFgnUgZ29kemluHgtOYXZpZ2F0ZVVybAUTL1BvZHpHb2R6aW5Ub2suYXNweB4FVmFsdWUFHVd5c3p1a2l3YXJrYSBwb2R6aWHFgnUgZ29kemluHgdUb29sVGlwBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbmRkDxQrAQFmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ZBYCZg8PFggfAwUdV3lzenVraXdhcmthIHBvZHppYcWCdSBnb2R6aW4fBAUTL1BvZHpHb2R6aW5Ub2suYXNweB8FBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbh8GBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbmRkAgQPZBYCAgMPZBYOAgEPFgIeCWlubmVyaHRtbAUtV2lydHVhbG5hIFVjemVsbmlhPCEtLSBzdGF0dXM6IDQ2MTg2NDM1MiAtLT4gZAINDw8WAh4ETW9kZQsqJVN5c3RlbS5XZWIuVUkuV2ViQ29udHJvbHMuVGV4dEJveE1vZGUCZGQCFQ8PFgIfAwUZT2R6eXNraXdhbmllIGhhc8WCYTxiciAvPmRkAhcPZBYCAgMPEGQPFgJmAgEWAgUHc3R1ZGVudAUIZHlkYWt0eWsWAWZkAhkPZBYEAgEPDxYCHwMFNDxiciAvPkx1YiB6YWxvZ3VqIHNpxJkgamFrbyBzdHVkZW50IHByemV6IE9mZmljZTM2NTpkZAIDDw8WAh8DBQhQcnplamTFumRkAhsPDxYEHwMFGFNlcndpcyBBYnNvbHdlbnTDs3c8YnIvPh4HVmlzaWJsZWhkZAIfDw8WAh8JaGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBUpjdGwwMCRjdGwwMCRUb3BNZW51UGxhY2VIb2xkZXIkVG9wTWVudUNvbnRlbnRQbGFjZUhvbGRlciRNZW51VG9wMyRtZW51VG9wMwAbwxvI81q+FMa4qP7qLeUjmXV+'),
        (r'__VIEWSTATEGENERATOR',r'BBDE9B47'),
        (r'ctl00_ctl00_TopMenuPlaceHolder_TopMenuContentPlaceHolder_MenuTop3_menuTop3_ClientState',r''),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtHaslo',r'HASLO'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtIdent',r'NRINDEKSU'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$rbKto',r'student'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$butLoguj',r'Zaloguj'),
                 )
    encodedFields = urllib.urlencode(formFields)
    response = opener.open(uri,encodedFields)
    thePage = response.read()
    return thePage

#Parsowanie strony pod kątem samej tabelki z ocenami
def parseDziekanat(strona):
    htmlAll = strona.replace('\n','')
    pocz = htmlAll.find('<table class="grid')
    kon  = htmlAll.find('</table>')
    return htmlAll[pocz:kon]

#Wysyłanie email z linux
def sendMail(tresc):
    email = 'evemorgen1911@gmail.com'
    adres = '| mail -s \'Zmienilo sie cos w dziekanacie\' ' + email
    os.system('echo \'' + tresc + '\' ' + adres)

#MAIN
if not os.path.isfile('stary.html'):
    temp = open('stary.html','w')
    temp.write(parseDziekanat(getHTMLdziekanat()))
    temp.close()
else:
    temp = open('stary.html','r')
    stary = temp.read()
    nowy = parseDziekanat(getHTMLdziekanat())
    if stary != nowy:
        sendMail('Tutaj pozniej bedzie info co przybylo')
        temp.close()
        open('stary.html','w').write(nowy)








