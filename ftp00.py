#!/usr/bin/python
# -*- coding: utf-8 -*-
from ftplib import FTP
print "Conectando a servidor ftp."
#Servidor ftp.
ftp = FTP('ftp.foo.cl')
print "Ingresando Credenciales."
#Usuario y contraseña.
ftp.login('user','password')
#Navegamos por los directorios.
ftp.cwd('carpeta1')
ftp.cwd('carpeta2')
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
