#!/usr/bin/python
# -*- coding: utf-8 -*-
from ftplib import FTP
print "Conectando a servidor FTP Manager."
ftp = FTP('ftp.imanager.cl')
print "Ingresando Credenciales."
ftp.login('ieb.usuario01','Mngr746')
ftp.cwd('ieb')
ftp.cwd('respaldos')
print "Listando archivos directorio respaldos."
listing = []
i = 0
ftp.retrlines("LIST", listing.append)
while i < len(listing):
    words = listing[i].split(None, 8)
    filename = words[-1].lstrip()
    ftp.retrbinary('RETR '+filename, open(filename,'wb').write)
    print "Descargado archivo "+filename
    i = i + 1


print "Total archivos descargados ", len(listing)
ftp.quit()
