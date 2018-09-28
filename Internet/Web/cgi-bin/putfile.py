#!/usr/bin/python3
"""
################################################################################
extract file uploaded by HTTP from web browser; users visit putifle.html to
get the upload form page, which then triggers this script on server; this is
very powerful, and very dangerous: you will usually want to check the filename,
etc; this may only work if file or dir is writable: a Unix 'chmod 777 uploads'
may suffice; file pathnames may arrive in client's path format: handle here;

caveat: could open output file in text mode to write receiving platform's line
ends since file content always str from the cgi module, but this is a temporary
solution anyhow--the cgi module doesn't handle binary file uploads in 3.1 at all;
################################################################################
"""

import cgi, os, sys
import posixpath, ntpath, macpath               # for client paths
debugmode    = False                            # True=print form info

loadtextauto = False                            # True=read file at once
uploaddir    = './uploads'                      # dir to store files

sys.stderr   = sys.stdout                       # show error msgs
form         = cgi.FieldStorage()               # parse form data
print("Content-type: text/html\n")              # with blank line
if debugmode: cgi.print_form(form)              # print form fields

# html templates

html = """
<html><title>Putfile response page</title>
<body>
<h1>Putfile response page</h1>
%s
</body></html>"""

goodhtml = html % """
<p>Your file, '%s', has been saved on the server as '%s'.
<p>An echo of the file's contents received and saved appears below.
</p><pre>%s</pre>
</p><hr>
"""

# process form data

def splitpath(origpath):                                 # get file at end
    for pathmodule in [posixpath, ntpath, macpath]:     # try all clients
        basename = pathmodule.split(origpath)[1]        # may be any server
        if basename != origpath:
            return basename                             # lets spaces pass
    return origpath                                     # failed or no dirs

def saveonserver(fileinfo):                             # use file input form data
    print('<BR>IN SAVEONSERVER FUNCTION <BR>')
    basename = splitpath(fileinfo.value)             # name without dir path
    print('basename', basename, '<br>')
    srvrname = os.path.join(uploaddir, basename)        # store in a dir if set
    print('srvrname', srvrname, '<br>')
    srvrfile = open(srvrname, 'wb')                     # always write bytes here
    print('srvrfile', srvrfile, '<br>')

    if loadtextauto:
        filetext = fileinfo.value                       # reads text into string
        if isinstance(filetext, str):                   # Python 3.1 hack
            filedata = filetedt.encode()
        srvrfile.write(filedata)                        # save in server file
    else:                                               # else read line by line
        print('<br>ELSE<br>')
        numlines, filetext = 0, ''                      # e.g., for huge files
        while True:                                     # content always str here
            line = fileinfo.file.readline()             # or for loop and iterator
            print('LINE=', line, '<br>')
            if not line: break
            if isinstance(line, str):                   # Python 3.1 hack
                line = line.encode()
            srvrfile.write(line)
            filetext += line.decode()                   # ditto
            numlines += 1
        filetext = ('[Lines=%d]\n' % numlines) + filetext
        srvrfile.close()
        os.chmod(srvrname, 0o666)                       # make writable: owned by 'nobody'
        return filetext, srvrname

def main():

    print("form['clientfile']<br>", form, '<br>'
                                    , form['clientfile'], '<br>'
                                    , form['clientfile'].value, '<br>'
                                    , form['clientfile'].file, '<br>'
                                    , form['clientfile'].filename, '<br><br><br>')

    if not 'clientfile' in form:
        print(html % 'Error: no file was received')
    elif not form['clientfile'].value:
        print(html % 'Error: filename is missing')
    else:
        print('MADE IT HERE')
        fileinfo = form['clientfile']
        try:
            filetext, srvrname = saveonserver(fileinfo)
        except:
            errmsg = '<h2>Error</h2><p>%s<p>%s' % tuple(sys.exc_info()[:2])
            print(html % errmsg)
        else:
            print(goodhtml % (cgi.escape(fileinfo.filename),
                              cgi.escape(srvrname),             # returned by saveonserver function
                              cgi.escape(filetext)))            # returned by saveonserver function

main()
