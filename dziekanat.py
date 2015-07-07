__author__ = 'evemorgen'
import urllib, urllib2, cookielib
from cookielib import CookieJar
import os

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
        (r'__VIEWSTATE',r'/wEPDwUKMTgxMTA3NTE0Mw8WAh4DaGFzZRYCZg9kFgJmD2QWAgIBD2QWBAICD2QWAgIBD2QWAgIBD2QWAgICDxQrAAIUKwACDxYEHgtfIURhdGFCb3VuZGceF0VuYWJsZUFqYXhTa2luUmVuZGVyaW5naGQPFCsAARQrAAIPFggeBFRleHQFHVd5c3p1a2l3YXJrYSBwb2R6aWHFgnUgZ29kemluHgtOYXZpZ2F0ZVVybAUTL1BvZHpHb2R6aW5Ub2suYXNweB4FVmFsdWUFHVd5c3p1a2l3YXJrYSBwb2R6aWHFgnUgZ29kemluHgdUb29sVGlwBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbmRkDxQrAQFmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ZBYCZg8PFggfAwUdV3lzenVraXdhcmthIHBvZHppYcWCdSBnb2R6aW4fBAUTL1BvZHpHb2R6aW5Ub2suYXNweB8FBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbh8GBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbmRkAgQPZBYCAgMPZBYOAgEPFgIeCWlubmVyaHRtbAUtV2lydHVhbG5hIFVjemVsbmlhPCEtLSBzdGF0dXM6IDQ2MTg2NDM1MiAtLT4gZAINDw8WAh4ETW9kZQsqJVN5c3RlbS5XZWIuVUkuV2ViQ29udHJvbHMuVGV4dEJveE1vZGUCZGQCFQ8PFgIfAwUZT2R6eXNraXdhbmllIGhhc8WCYTxiciAvPmRkAhcPZBYCAgMPEGQPFgJmAgEWAgUHc3R1ZGVudAUIZHlkYWt0eWsWAWZkAhkPZBYEAgEPDxYCHwMFNDxiciAvPkx1YiB6YWxvZ3VqIHNpxJkgamFrbyBzdHVkZW50IHByemV6IE9mZmljZTM2NTpkZAIDDw8WAh8DBQhQcnplamTFumRkAhsPDxYEHwMFGFNlcndpcyBBYnNvbHdlbnTDs3c8YnIvPh4HVmlzaWJsZWhkZAIfDw8WAh8JaGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBUpjdGwwMCRjdGwwMCRUb3BNZW51UGxhY2VIb2xkZXIkVG9wTWVudUNvbnRlbnRQbGFjZUhvbGRlciRNZW51VG9wMyRtZW51VG9wMwAbwxvI81q+FMa4qP7qLeUjmXV+'),
        (r'__VIEWSTATEGENERATOR',r'BBDE9B47'),
        (r'ctl00_ctl00_TopMenuPlaceHolder_TopMenuContentPlaceHolder_MenuTop3_menuTop3_ClientState',r''),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtHaslo',r'TU_WSTAW_SWOJE_HASLO_DO_DZIEKANATU'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtIdent',r'TU_WSTAW_SWOJ_NUMER_INDEKSU'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$rbKto',r'student'),
        (r'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$butLoguj',r'Zaloguj'),
                 )
    encodedFields = urllib.urlencode(formFields)
    response = opener.open(uri,encodedFields)
    thePage = response.read()
    return thePage

#Parsowanie strony pod katem samej tabelki z ocenami
def parseDziekanat(strona):
    htmlAll = strona.replace('\n','')
    pocz = htmlAll.find('<table class="grid')
    kon  = htmlAll.find('</table>')
    return htmlAll[pocz:kon]

#Wysylanie email z linux
def sendMail(tresc):
    email = ''
    adres = '| mail -s \'Zmienilo sie cos w dziekanacie\' ' + email
    os.system('echo \'' + tresc + '\' ' + adres)
#Wyciaganie z tabelki oceny, nazwy przedmiotu oraz kategori oceny.
def getOcenaAndPrzedmiot(nowy,stary):
    ocenaPocz = 0
    while (nowy[ocenaPocz] == stary[ocenaPocz]) and (ocenaPocz < len(nowy) - 1):
        ocenaPocz += 1
    ocenaKon = ocenaPocz
    while nowy[ocenaKon] != '<':
        ocenaKon += 1
    coKon = ocenaPocz - len('</td><td>')
    coPocz = coKon-1
    while nowy[coPocz] != '>':
        coPocz -= 1
    coPocz += 1

    przedmiotPocz = przedmiotKon = coPocz - len('</td><td>')
    while nowy[przedmiotPocz] != '>':
        przedmiotPocz -= 1
    przedmiotPocz += 1

    if nowy[ocenaPocz] == '<':
        while nowy[ocenaPocz] != '>':
            ocenaPocz += 1
        ocenaPocz += 1
        ocenaKon = ocenaPocz
        while nowy[ocenaKon] != '<':
            ocenaKon += 1

    ocena = nowy[ocenaPocz:ocenaKon]
    co = nowy[coPocz:coKon]
    przedmiot = nowy[przedmiotPocz:przedmiotKon]
    return przedmiot + ' - ' + co + ' - ' + ocena

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
        sendMail(getOcenaAndPrzedmiot(nowy, stray))
        temp.close()
        open('stary.html','w').write(nowy)

