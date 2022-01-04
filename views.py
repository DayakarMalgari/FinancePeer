
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import utils
########################################################################################################################
# dummy index view, just to load the index.html file
########################################################################################################################


def index(request):

    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

# static html

class StaticView(TemplateView):

   template_name = "static.html"
########################################################################################################################
# dummy index view, just to load the index.html file for admin urls
########################################################################################################################
def admin(request):

    return render(request, 'index.html', locals())

#########################################################################################################################
#  view for login and store the username in session
#########################################################################################################################

def login_WS(request):
    username = 'not logged in'
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            request.session['username'] = username
    else:
        MyLoginForm = LoginForm()

    return render(request, 'loggedin.html', {"username": username})

def formViewS(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', {"username": username})
    else:
        return render(request, 'login.html', {})

# -*- coding: utf-8 -*-
########################################################################################################################
# login form
# -*- coding: utf-8 -*-
#########################################################################################################################
#  view for login and authenticate by django's authentication
#########################################################################################################################

from myapp.forms import LoginForm
from myapp.models import loginTab
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import ObjectDoesNotExist as ObjDoNotExist
from django.contrib.auth import authenticate         #, login, logout
#from .forms import UserForm, UserRegistrationForm
#from django.http import HttpResponse
from django.contrib.auth.models import User

def loginMSI(request):
    InvalidData = False
    emailfound = False
    emaiidnotfound = False
    passwrong = False
    unknowerror = False
    emailnotentered = False
    passwordnotentered = False
    emaiidalreadyloggedin = False
    Invalidcredent = False
    email_id = ''
    password = ''

    if request.method == "POST":
        # Get the posted form

        email_id = 'not logged in'
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.data.get('email_id') == '':
            emailnotentered = True
            return render(request, 'login.html', locals())
        if MyLoginForm.data.get('password') == '':
            passwordnotentered = True
            return render(request, 'login.html', locals())

        if MyLoginForm.is_valid():

           email_id = MyLoginForm.cleaned_data["email_id"]
           password = MyLoginForm.cleaned_data["password"]
########################################################################################################################
           user = authenticate(
               request,
               username=email_id,
               email=email_id,
               password=password
           )
           if user is None:

               Invalidcredent = True
               return render(request, 'login.html', locals())
           else:
########################################################################################################################
               try:

                  Mylogindb = loginTab._default_manager.get(email_id=MyLoginForm.data.get('email_id'))

                  if Mylogindb.password != MyLoginForm.data.get('password'):

                       passwrong = True
                       return render(request, 'login.html', locals())
               except ObjectDoesNotExist or loginTab._default_manager.DoesNotExist:

                   emaiidnotfound = True
                   return render(request, 'login.html', locals())
               except:

                   unknowerror = True
                   return render(request, 'login.html', locals())



               if request.session.has_key('username'):

                   if request.session['username']==email_id:
                        emaiidalreadyloggedin = True
                   else:
                        request.session['username'] = email_id
               else:

                   request.session['username'] = email_id

        else:

            # just loding the login form,no flags here
            return render(request, 'login.html', locals())

    else:

        MyLoginForm = LoginForm(request.GET)
    context = {
        'form': MyLoginForm,
        'email_id': email_id,
    }

    return render(request, 'welcome_toFP.html', context)
########################################################################################################################
# view for loading sign-up page
########################################################################################################################
def Signup(request):
    unknownerror = False
    emailfound = False
    fullnamenotentered = False
    context = {
    'fullnamenotentered': fullnamenotentered,
    'unknownerror' : unknownerror,
    'emailfound' : emailfound,}
    return render(request, 'login_signup.html', context)
########################################################################################################################
# view for validating sign-up page
########################################################################################################################
def loginMSU(request):
    emailfound = False
    emailnotentered = False
    passwordnotentered = False
    fullnamenotentered = False
    unknowerror = False
    signup = False
    email_id = ''
    passwrod = ''


    if request.method == "POST":

        # Get the posted form
        MyLoginForm = LoginForm(request.POST)


        if MyLoginForm.data.get('email_id') == '':
            emailnotentered = True
            return render(request, 'login_signup.html', locals())
        if MyLoginForm.data.get('password') == '':
            passwordnotentered = True
            return render(request, 'login_signup.html', locals())
        if MyLoginForm.data.get('username') == '':
            fullnamenotentered = True
            return render(request, 'login_signup.html', locals())

        if MyLoginForm.is_valid():
            # Get the posted form
            email_id = MyLoginForm.cleaned_data["email_id"]
            password = MyLoginForm.cleaned_data["password"]
            username = MyLoginForm.cleaned_data["email_id"]
            try:
                Mylogindb = loginTab._default_manager.get(email_id=MyLoginForm.data.get('email_id'))
                if Mylogindb.email_id == MyLoginForm.data.get('email_id'):
                    emailfound = True
                    return render(request, 'login.html', locals())

            except ObjectDoesNotExist or ObjDoNotExist or loginTab._default_manager.DoesNotExist:

            #############################################################################bbbbbbbbbb
                newuser = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email_id
                )
                #https://www.programink.com/django-tutorial/django-authentication.html
            ###############################################################################bbbbbbbb
                log = loginTab()
                log.email_id = MyLoginForm.cleaned_data["email_id"]
                log.password = MyLoginForm.cleaned_data["password"]
                log.username = MyLoginForm.cleaned_data["email_id"]
                try:
                    newuser.save()                                                  ###########bbbbbb
                    log.save()
                    signup=True
                except Exception as e:
                    print(e)
                    unknowerror = True
                    return render(request, 'login_signup.html', locals())
            except Exception as e:
                    print(e)
                    unknowerror = True
                    return render(request, 'login_signup.html', locals())
        else:
            InvalidData = True
            return render(request, 'login_signup.html', locals())

    else:

        MyLoginForm = LoginForm(request.GET)
    context = {
        'MyLoginForm': MyLoginForm,
        'signup': signup,
        'email_id': email_id,
    }
    return render(request, 'login.html', context)
#########################################################################################################################
#  view for deleting session variable on logout
#########################################################################################################################

def logout(request):

    try:

       del request.session['username']

    except Exception as e:
       print(e)
       pass
    loggedout=True
    return render(request, 'login.html', {'loggedout':loggedout})
#########################################################################################################################
#  view for processing file upload page
#########################################################################################################################
from myapp.forms import FinancePeerJsonForm
from myapp.models import FinancePeerJsonTab

def uploadfile(request):
    unknownerror = False
    emailnotentered = False
    filenotselected = False
    emaiidnotfound = False
    InvalidData=False
    integrity = False
    saved = False
    JsonFile = ' '
    JsonData = ' '
    email_id = ' '
    from django.core.files.storage import FileSystemStorage

    if request.method == "POST":

        # Get the posted form
        MyFinancePeerJsonForm = FinancePeerJsonForm(request.POST, request.FILES)
        MyFinancePeerJsonForm.email_id = request.session['username']
        if MyFinancePeerJsonForm.data.get('email_id') == '' :

            emailnotentered = True
            return render(request, 'UploadFile.html', locals())
        if MyFinancePeerJsonForm.data.get('JsonFile') == '' :

            filenotselected = True
            return render(request, 'UploadFile.html', locals())

        if MyFinancePeerJsonForm.data.get('email_id') != request.session['username']:
            email_id = MyFinancePeerJsonForm.data.get('email_id')
            emaiidnotfound = True
            return render(request, 'UploadFile.html', locals())

        if MyFinancePeerJsonForm.is_valid():

            fpjt = FinancePeerJsonTab()
            fpjt.email_id = request.session['username']

            fpjt.JsonFile = MyFinancePeerJsonForm.cleaned_data["JsonFile"]
            jsonfile = MyFinancePeerJsonForm.cleaned_data["JsonFile"]

            #print(jsonfile.read().decode())
            try:

                fpjt.save()          # this saves the file as is in the database table at /media folder
                uploaded_file = request.FILES['JsonFile']
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)
                jsoncount=perform_database_load(filename) # this is where it loads the data into rdbms table

                if jsoncount ==0:
                    integrity = True
                else:
                    saved = True

                email_id = request.session['username']
                JsonFile = MyFinancePeerJsonForm.cleaned_data["JsonFile"]

            except Exception as e :
                print('err 1',e)
                unknownerror = True

        else:

            pass
    else:

        MyFinancePeerJsonForm = FinancePeerJsonForm()

    email_id = request.session['username']
    MyFinancePeerJsonForm.email_id = request.session['username']

    context = {
     'form': MyFinancePeerJsonForm,
     'unknownerror': unknownerror,
     'saved': saved,
     'integrity': integrity,
     'JsonFile': JsonFile,
     'email_id':email_id,
    }

    return render(request, 'UploadFile.html',context)

#########################################################################################################################
#  view for loading uploaded json file into postgre database table
#########################################################################################################################

import json

import os
def perform_database_load(jsonfile):
    pathf = os.path.join('media/', jsonfile)
    with open(pathf) as f:
        data = json.load(f)

    jsoncount = 0

    try:
        for a in range(len(data)):
            fpdt = FinancePeerDetailsTab()
            fpdt.FP_ID     = data[a]["id"]
            fpdt.FP_UserID = data[a]["userId"]
            fpdt.FP_Title  = data[a]["title"]
            fpdt.FP_Body   = data[a]["body"]

            fpdt.save()
            jsoncount+=1
    except Exception as e:
        print('error loading database at record: ',jsoncount," ",e)
        jsoncount =0
        return jsoncount

    return jsoncount


#########################################################################################################################
#  view for removing special characters from search fields entered on the user searcg page
#########################################################################################################################
from myapp.forms import FinancePeerDetailsForm
from myapp.models import FinancePeerDetailsTab

from django.db.utils import OperationalError

def rep_spec_char(str1):

    str1 = str1.replace('/',"  ")
    str1 = str1.replace('(', "  ")
    str1 = str1.replace(')', "  ")
    str1 = str1.replace(',', "  ")
    str1 = str1.replace('*', "  ")
    str1 = str1.replace('?', "  ")
    str1 = str1.replace('!', "  ")
    str1 = str1.replace('~', "  ")
    str1 = str1.replace('`', "  ")
    str1 = str1.replace('@', "  ")
    str1 = str1.replace('#', "  ")
    str1 = str1.replace('$', "  ")
    str1 = str1.replace('%', "  ")
    str1 = str1.replace('^', "  ")
    str1 = str1.replace('&', "  ")
    str1 = str1.replace('_', "  ")
    str1 = str1.replace('-', "  ")
    str1 = str1.replace('=', "  ")
    str1 = str1.replace('\\', "  ")
    str1 = str1.replace('<', "  ")
    str1 = str1.replace('>', "  ")
    str1 = str1.replace('"', "  ")
    str1 = str1.replace("'", "  ")
    str1 = str1.replace('|', "  ")
    str1 = str1.replace('{', "  ")
    str1 = str1.replace('}', "  ")
    str1 = str1.replace('[', "  ")
    str1 = str1.replace("]", "  ")

    return str1
#########################################################################################################################
#  view for processing search page
#########################################################################################################################

def welcome_toFP(request):
    unknownerror = False
    criterianotentered = False
    jsonDocsnotfound = False
    toomanykeys = False

    totcount = 0
    links = []
    kys = []

    if request.method == "POST" :
#HERE
        MyFinancePeerDetailsForm = FinancePeerDetailsForm(request.POST)
        FP_Title = request.GET.get('FP_Title')
        FP_UserID = request.GET.get('FP_UserID')
        FP_ID = request.GET.get('FP_ID')
        FP_tsi = request.GET.get('FP_tsi')



        if ((MyFinancePeerDetailsForm.data.get('FP_Title') == '' ) and
           (MyFinancePeerDetailsForm.data.get('FP_UserID') == '' ) and
           (MyFinancePeerDetailsForm.data.get('FP_ID') == '' )):

            criterianotentered = True
            return render(request, 'welcome_toFP.html', locals())


        try:
            fpdtData = FinancePeerDetailsTab._default_manager.filter(FP_Title__contains='}{}{}{}{}{}{}{}{}{}{')
            if ((MyFinancePeerDetailsForm.data.get('FP_ID') != 0) and
                    (MyFinancePeerDetailsForm.data.get('FP_ID')!= "") and
                (MyFinancePeerDetailsForm.data.get('FP_ID') != None ) and
                    int(MyFinancePeerDetailsForm.data.get('FP_ID')) > 0):
                tmp = MyFinancePeerDetailsForm.data.get('FP_ID')
                ########################################################################################################
                #  part of code to process ID search field
                ########################################################################################################

                try:

                    fpdtData = FinancePeerDetailsTab._default_manager.get(FP_ID=tmp)
                    try:
                        links.append(fpdtData)
                    except Exception as e:
                        print('e11', e)
                        unknownerror = True
                except ObjectDoesNotExist or ObjDoNotExist:

                    pass
                except Exception as e:
                    print('e12', e)
                    unknownerror = True
                ########################################################################################################
                #  code to process USERID search field of user search page
                ########################################################################################################

            elif ((MyFinancePeerDetailsForm.data.get('FP_UserID') != 0) and
                  (MyFinancePeerDetailsForm.data.get('FP_UserID') != "") and
                  (MyFinancePeerDetailsForm.data.get('FP_UserID') != None) and
                  int(MyFinancePeerDetailsForm.data.get('FP_UserID'))> 0 ):
                tmp = MyFinancePeerDetailsForm.data.get('FP_UserID')

                try:
                    fpdtData = FinancePeerDetailsTab._default_manager.filter(FP_UserID=tmp)
                    try:
                        links.extend(fpdtData)
                    except Exception as e:
                        print('e13', e)
                        unknownerror = True
                except ObjectDoesNotExist or ObjDoNotExist:
                    pass
                except Exception as e:
                    print('e14', e)
                    unknownerror = True
                ########################################################################################################
                #  code to process title search box/field of user search page
                ########################################################################################################

            elif MyFinancePeerDetailsForm.data.get('FP_Title') != "":


                if MyFinancePeerDetailsForm.data.get('FP_tsi') :

                    tmpstr = MyFinancePeerDetailsForm.data.get('FP_Title')

                    try:
                        fpdtData = FinancePeerDetailsTab._default_manager.get(FP_Title=tmpstr)
                        try:
                            links.append(fpdtData)
                        except Exception as e:
                            print('e11', e)
                            unknownerror = True
                    except ObjectDoesNotExist or ObjDoNotExist:
                        pass
                    except Exception as e:
                        print('e15', e)
                        unknownerror = True
                else:

                    tmpstr = MyFinancePeerDetailsForm.data.get('FP_Title')
                    keysF = rep_spec_char(str(tmpstr))
                    kys = str(keysF).split(sep=" ")

                    try:

                        for i in range(len(kys)):
                            if ((kys[i] != '') & (len(kys[i]) > 2)):
                                fpdtDataA = \
                                    FinancePeerDetailsTab._default_manager.filter(FP_Title__icontains=kys[i])

                                fpdtData = fpdtDataA.union(fpdtData)

                        try:
                            links.extend(fpdtData)
                        except OperationalError as e:
                            print('SQLITE Users! operational error, too many keys')
                            toomanykeys = True
                        except Exception as e:
                            print('e17', e)
                            unknownerror = True

                    except ObjectDoesNotExist or ObjDoNotExist:

                        pass
                    except Exception as e:
                        print('e18', e)
                        unknownerror = True
            else:
                criterianotentered = True
                return render(request, 'welcome_toFP.html', locals())



            if len(links)==0 and toomanykeys==False:
               jsonDocsnotfound = True
            else:
               totcount = len(links)

            if ((MyFinancePeerDetailsForm.data.get('FP_Title') == None) and
                (MyFinancePeerDetailsForm.data.get('FP_UserID') == None) and
                (MyFinancePeerDetailsForm.data.get('FP_ID') == None)):

                jsonDocsnotfound = False
        except ObjectDoesNotExist or ObjDoNotExist:

            jsonDocsnotfound = True

        except Exception as e:
            print('e19',e)
            unknownerror = True


    else:
        print('at POST else')
        MyFinancePeerDetailsForm = FinancePeerDetailsForm(request.GET)

    context = {
         "toomanykeys":toomanykeys,
        "totcount" : totcount,
        "unknownerror" : unknownerror,
        "jsonDocsnotfound" : jsonDocsnotfound,
        "form" : MyFinancePeerDetailsForm,
        "links" : links,
            }

    return render(request, 'welcome_toFP.html', context)
#########################################################################################################################
#  this part of code is still in progress... to save changes made on user search page
#########################################################################################################################

def ReloadAfterSave(FP_ID,FP_UserID,FP_Title,FP_tsi):
    unknownerror = False
    criterianotentered = False
    jsonDocsnotfound = False
    toomanykeys = False
    totcount = 0
    links = []
    tmp = []
    kys = []
    from myapp.models import FinancePeerDetailsTab
    try:
        fpdtData = FinancePeerDetailsTab._default_manager.filter(FP_Title__contains='}{}{}{}{}{}{}{}{}{}{')
        if ((FP_ID != 0) and (FP_ID != "")):
            tmp = FP_ID
            try:
                fpdtData = FinancePeerDetailsTab._default_manager.get(FP_ID=tmp)
                try:
                    links.append(fpdtData)
                except Exception as e:
                    print('e11', e)
                    unknownerror = True
            except ObjectDoesNotExist or ObjDoNotExist:
                pass
            except Exception as e:
                print('e12', e)
                unknownerror = True
        elif ((FP_UserID != 0) and (FP_UserID != "")):

            tmp = FP_UserID
            try:
                fpdtData = FinancePeerDetailsTab._default_manager.filter(FP_UserID=tmp)
                try:
                    links.extend(fpdtData)
                except Exception as e:
                    print('e13', e)
                    unknownerror = True
            except ObjectDoesNotExist or ObjDoNotExist:
                pass
            except Exception as e:
                print('e14', e)
                unknownerror = True
        elif FP_Title != "":
            if FP_tsi :
                tmpstr = FP_Title
                try:
                    fpdtData = FinancePeerDetailsTab._default_manager.get(FP_Title=tmpstr)
                    try:
                        links.append(fpdtData)
                    except Exception as e:
                        print('e11', e)
                        unknownerror = True
                except ObjectDoesNotExist or ObjDoNotExist:
                    pass
                except Exception as e:
                    print('e15', e)
                    unknownerror = True
            else:
                tmpstr = FP_Title
                keysF = rep_spec_char(str(tmpstr))
                kys = str(keysF).split(sep=" ")

                try:
                    for i in range(len(kys)):
                        if ((kys[i] != '') & (len(kys[i]) > 2)):
                            fpdtDataA = \
                                FinancePeerDetailsTab._default_manager.filter(FP_Title__icontains=kys[i])

                            fpdtData = fpdtDataA.union(fpdtData)
                    try:
                        links.extend(fpdtData)
                    except OperationalError as e:
                        print('SQLITE Users! operational error, too many keys')
                        toomanykeys = True
                    except Exception as e:
                        print('e17', e)
                        unknownerror = True

                except ObjectDoesNotExist or ObjDoNotExist:
                    pass
                except Exception as e:
                    print('e18', e)
                    unknownerror = True

        if len(links)==0 and toomanykeys==False:
           jsonDocsnotfound = True
        else:
           totcount = len(links)

        if ((FP_Title == None) and (FP_UserID == None) and (FP_ID == None)):
            jsonDocsnotfound = False
    except ObjectDoesNotExist or ObjDoNotExist:
        jsonDocsnotfound = True

    except Exception as e:
        print('e19',e)
        unknownerror = True
    from myapp.forms import FinancePeerDetailsForm as MyFinancePeerDetailsForm
    MyFinancePeerDetailsForm.FP_ID = FP_ID
    MyFinancePeerDetailsForm.FP_UserID = FP_UserID
    MyFinancePeerDetailsForm.FP_Title = FP_Title

    context = {
    "totcount" : totcount,
    "toomanykeys" : toomanykeys,
    "unknownerror" : unknownerror,
    "jsonDocsnotfound" : jsonDocsnotfound,
    "form" : MyFinancePeerDetailsForm,
    "links" : links,
        }
    return context

#########################################################################################################################
#  this part of the code is also related to saving the changes made on user search page. Still in progress ........
#########################################################################################################################

def save_changes(request):
    unknownerror = False
    IntegritySave = False
    saved = False
    context = { }

    # Get the posted form
    from myapp.forms import FinancePeerDetailsForm
    from myapp.models import FinancePeerDetailsTab
    MyFinancePeerDetailsForm = FinancePeerDetailsForm(request.GET)


    if request.method == "GET":

        FP_ID = request.GET.get('FP_ID')
        FP_UserID = request.GET.get('FP_UserID')
        FP_Title = request.GET.get('FP_Title')
        FP_tsi = request.GET.get('FP_tsi')

        FP_BodySS = request.GET.get('FP_BodySS')
        FP_BodyS = request.GET.get('FP_BodyS')
        FP_IDS = request.GET.get('FP_IDS')
        FP_UserIDS = request.GET.get('FP_UserIDS')
        FP_TitleS = request.GET.get('FP_TitleS')

        try:

            fpdt = FinancePeerDetailsTab._default_manager.get(FP_ID=request.GET.get('FP_IDS'))

        except ObjectDoesNotExist or ObjDoNotExist:
            pass

        except Exception as e:
            print('err', e)
            unknownerror = True
            return render(request, 'welcome_toFP.html', locals())

        #fpdt = FinancePeerDetailsTab()

        fpdt.FP_ID = FP_IDS
        fpdt.FP_UserID = FP_UserIDS
        fpdt.FP_Title = FP_TitleS
        fpdt.FP_Body = FP_BodyS

        try:

            fpdt.save()
            saved = True
        except utils.IntegrityError:

            IntegritySave = True
        except Exception as e:
            print("inside exception of save")
            print(e)
            unknownerror = True
            # raise ValueError
        cont = ReloadAfterSave(FP_ID, FP_UserID, FP_Title,FP_tsi)
        totcount = cont.get("totcount")
        toomanykeys = cont.get("toomanykeys")

        if not unknownerror:
            unknownerror = cont.get("unknownerror")
        FinancePeerDetailsForm = cont.get("form")
        links = cont.get("links")
        context = {
            "totcount": totcount,
            "toomanykeys": toomanykeys,
            "unknownerror": unknownerror,
            "saved": saved,
            "IntegritySave": IntegritySave,
            "form": MyFinancePeerDetailsForm,
            "links": links,
            'FP_tsi':FP_tsi,
        }

    return render(request, 'welcome_toFP.html', context)

#########################################################################################################################
#  view for displaying all data from the database
#########################################################################################################################
def fulldataview(request):

    unknownerror = False
    criterianotentered = False
    jsonDocsnotfound = False
    toomanykeys = False
    totcount = 0
    links = []
    if request.method == "POST" :

        MyFinancePeerDetailsForm = FinancePeerDetailsForm(request.GET)


        try:

            fpdtData = FinancePeerDetailsTab._default_manager.all()
            try:
               links.extend(fpdtData)
            except Exception as e:
               print('e11', e)
               unknownerror = True

            if len(links)==0 :
               jsonDocsnotfound = True
            else:
               totcount = len(links)

            #if ((MyFinancePeerDetailsForm.data.get('FP_Title') == None) and
            #    (MyFinancePeerDetailsForm.data.get('FP_UserID') == None) and
            #    (MyFinancePeerDetailsForm.data.get('FP_ID') == None)):

            #    jsonDocsnotfound = False
        except Exception as e:
            print('e11', e)
            unknownerror = True
    else:
        print('at GET else')
        MyFinancePeerDetailsForm = FinancePeerDetailsForm(request.GET)

    context = {
        "totcount" : totcount,
        "toomanykeys" : toomanykeys,
        "unknownerror" : unknownerror,
        "criterianotentered" : criterianotentered,
        "jsonDocsnotfound" : jsonDocsnotfound,
        "form" : MyFinancePeerDetailsForm,
        "links" : links,

            }
    return render(request, 'welcome_toFPA.html', context)
########################################################################################################################

