from django.shortcuts import render

# Create your views here.

pro1 = {
    "imgslide3" : "static/img/udemy-wireframe.png", 
    "imgslide1" : "static/img/udemy-web-pt-1.png", 
    "imgslide2" : "static/img/udemy-web-pt-2.png",
    "pdetails" : "Udemy Web Clone Details",
    "projectdate" : "07 December, 2021",
    "drivelink" : "https://drive.google.com/file/d/1rEZNHd4wS14H-oUePc3cfp0wGWlCoZ0A/view?usp=sharing",
    "theproduct" : "An E-Learning Website which is user friendly and can be used to search and learn all kind of courses.",
    "theproblem" : "Different E-Learning websites with lot of steps to take a course and is really annoying by ads",
    "thegoal1" : "The goal is to design a website that is user freindly and allows user to learn or choose a course easily",
    "myrole" : "UX/UI designer as creating a design from conception to delivery.",
    "responsibilities" : "Researching, creating wireframes, low fedility and high fedility prototypes. conducting studies, testing and iterating on designs.",
    "thegoal2" : "07 December 2021",
    "userresearch" : "Conducted researches and studies, created empathy map to understand the users i'm designing for their needs. Majority of the users need courses that are actually genuine and worth Most current E-learning websites have a lot of courses but it is so expensive unlike Udemy-web",
    "pp1t" : "Expensive:",
    "pp2t" : "Genuine:",
    "pp3t" : "Doubt Clearance:",
    "pp1ex" : "Other E-learning website courses are really expensive",
    "pp2ex" : "Most of the courses in other E-learning websites dont provide certificate for completion",
    "pp3ex" : "Unlike other websites, Udemy has a large community for Doubt clearance",
    "cardname" : "Britney",
    "cardage" : "19",
    "doing" : "Student",
    "living" : "Venice, Italy",
    "cardquote" : "As I am a student interested in UI/UX designing, I always search for courses on several E-learning platforms and it's all kinda expensive and most of them are not genuine either",
    "say" : "I want an e-learning website where i can purchase the courses I want and is user freindly",
    "think" : "I Think it would really help to grow my career without any problem",
    "does" : "Continue learning without clearing any doubts and not getting knowledge as i expected",
    "feel" : "Frustrated by ads and nervous about my career",
    "col1" : "#6B6B6B",
    "col2" : "#F8F9FB",
    "col3" : "#151515",
    "col4" : "#A435F0",
    "col5" : "#FFBC00",
    "font" : "Segoe UI",
    "cardprofile" : "https://images.unsplash.com/photo-1571844307880-751c6d86f3f3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1896&q=80",
}

pro2 = {
    "imgslide3" : "static/img/udemy-mob-pt-1.png", 
    "imgslide1" : "static/img/udemy-mob-pt-2.png", 
    "imgslide2" : "static/img/udemy-wireframe.png",
    "pdetails" : "Udemy mobile Clone Details",
    "projectdate" : "28 January, 2022",
    "drivelink" : "https://drive.google.com/file/d/1cdbapvcqlnmmnUBp6X4r6NvEf2fFLndr/view?usp=sharing",
    "theproduct" : "An E-Learning app which is user friendly and can be used to search and learn all kind of courses.",
    "theproblem" : "Different E-Learning apps with lot of steps to take a course and is really annoying by ads",
    "thegoal1" : "The goal is to design a app that is user freindly and allows user to learn or choose a course easily",
    "myrole" : "UX/UI designer as creating a design from conception to delivery.",
    "responsibilities" : "Researching, creating wireframes, low fedility and high fedility prototypes. conducting studies, testing and iterating on designs.",
    "thegoal2" : "07 December 2021",
    "userresearch" : "Conducted researches and studies, created empathy map to understand the users i'm designing for their needs. Majority of the users need courses that are actually genuine and worth Most current E-learning apps have a lot of courses but it is so expensive unlike Udemy-web",
    "pp1t" : "Expensive:",
    "pp2t" : "Genuine:",
    "pp3t" : "Doubt Clearance:",
    "pp1ex" : "Other E-learning app courses are really expensive",
    "pp2ex" : "Most of the courses in other E-learning apps dont provide certificate for completion",
    "pp3ex" : "Unlike other apps, Udemy has a large community for Doubt clearance",
    "cardname" : "Anna",
    "cardage" : "20",
    "doing" : "Student",
    "living" : "Brighton, London",
    "cardquote" : "As I am a student interested in UI/UX designing, I always search for courses on several E-learning platforms and it's all kinda expensive and most of them are not genuine either",
    "say" : "I want an e-learning app where i can purchase the courses I want and is user freindly",
    "think" : "I Think it would really help to grow my career without any problem",
    "does" : "Continue learning without clearing any doubts and not getting knowledge as i expected",
    "feel" : "Frustrated by ads and nervous about my career",
    "col1" : "#6B6B6B",
    "col2" : "#F8F9FB",
    "col3" : "#151515",
    "col4" : "#A435F0",
    "col5" : "#FFBC00",
    "font" : "Segoe UI",
    "cardprofile" : "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
}

pro3 = {
    "imgslide3" : "static/img/ct-pt3.png", 
    "imgslide1" : "static/img/ct-pt1.png", 
    "imgslide2" : "static/img/ct-pt2.png",
    "pdetails" : "Code Translator Details",
    "projectdate" : "10 February, 2022",
    "drivelink" : "https://drive.google.com/file/d/1Z1eUmZdgAZnOOL0eXELDHBs2H9hOgxfR/view?usp=sharing",
    "theproduct" : "An app which can be used to translate programming languages",
    "theproblem" : "When you have to translate a program (eg- c++ to java), it's pretty hard to do hard coding and you may face more time debbuging than actual coding",
    "thegoal1" : "The goal is to create an app which can translate programming languages",
    "myrole" : "UX/UI designer as creating a design from conception to delivery.",
    "responsibilities" : "Researching, creating wireframes, low fedility and high fedility prototypes. conducting studies, testing and iterating on designs.",
    "thegoal2" : "10 February, 2022",
    "userresearch" : "Conducted researches and studies, created empathy map to understand the users i'm designing for their needs. Majority of users need a translator like css to scss(which is already available) but with system programming languages like java to c++ or python to javascript",
    "pp1t" : "Unbegun:",
    "pp2t" : "Customer support:",
    "pp3t" : "Mechanism:",
    "pp1ex" : "Yeah that's right i've done the research, there is no app like this yet except an website which can only translate css to scss",
    "pp2ex" : "lack of customer support",
    "pp3ex" : "As a developer i always wondered how some things or some apps works behind the scenes, but CT will show how it actually works, so that other developers can understand it maybe start a project like this as i did",
    "cardname" : "Linus Torvalds",
    "cardage" : "52",
    "doing" : "Software engineer",
    "living" : "Venice, Italy",
    "cardquote" : "As a software engineer, i've to work with different programming especially java or c++ and sometimes i've to hard code translate it by myself. believe me it's like hell!",
    "say" : "I want an app which can translate codes, It would be really helpfull for millions of developers like me",
    "think" : "I think i might be able to do work 100x faster with this",
    "does" : "Hard code and debbuging more than actual coding",
    "feel" : "Frustrated that there is literally no app build by anyone yet",
    "col1" : "#A6A8A9",
    "col2" : "#F09C49",
    "col3" : "#F7F7AE",
    "col4" : "#075896",
    "col5" : "#1F2F42",
    "font" : "Palatino Linotype",
    "cardprofile" : "data:image/jpeg;base64,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",
}


pro4 = {
    "imgslide3" : "static/img/picsay-pt1.png", 
    "imgslide1" : "static/img/picsay-pt2.png", 
    "imgslide2" : "static/img/picsay-pt3.png",
    "pdetails" : "Picsay Details",
    "projectdate" : "22 February, 2022",
    "drivelink" : "https://drive.google.com/file/d/1ZR-OLgIPXpuz2jYsPaypGVKrYyoewM3-/view?usp=sharing",
    "theproduct" : "An app which is for photographers and to flex their awesome skills by posting the pictures they took",
    "theproblem" : "Similiar app like instagram and tiktok but without no dumb posts",
    "thegoal1" : "The goal is to design a app for photographers",
    "myrole" : "UX/UI designer as creating a design from conception to delivery.",
    "responsibilities" : "Researching, creating wireframes, low fedility and high fedility prototypes. conducting studies, testing and iterating on designs.",
    "thegoal2" : "07 December 2021",
    "userresearch" : "Conducted researches and studies, created empathy map to understand the users i'm designing for their needs. Majority of the users need an app for post and show off their photography skills",
    "pp1t" : "Privacy:",
    "pp2t" : "Escape:",
    "pp3t" : "Security:",
    "pp1ex" : "most of social medias are said to take the user personal datas",
    "pp2ex" : "Moving from other social medias which is not built for appreciate underrated accounts which has to pay a lot of money to get among other celeb accounts",
    "pp3ex" : "Insecure data storage and sensitive data exposure",
    "cardname" : "Jonas",
    "cardage" : "58",
    "doing" : "Photographer",
    "living" : "Venice, Italy",
    "cardquote" : "I am a photgrapher at 60s. recently i've been struggling with lack of motivation and encouragment from others",
    "say" : "As a photographer i want an app to post my photoshoot skills and don't want it to be like other apps, like pay to get promoted and get more reach, actual appreciation from people with similiar interests",
    "think" : "I Think this would really help me to keep me going",
    "does" : "Posting on other social medias where no one actually finds my art interesting",
    "feel" : "Sad and desperate for motivation",
    "col1" : "#3C0000",
    "col2" : "#151719",
    "col3" : "#552BF9",
    "col4" : "#FF0000",
    "col5" : "#959595",
    "font" : "Work Sans",
    "cardprofile" : "https://images.unsplash.com/photo-1615567964485-0ee76b5b3410?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
}


def index(request):
    return render(request, 'index.html')

def project1(request):
    return render(request, 'portfolio-details1.html', pro1)

def project2(request):
    return render(request, 'portfolio-details2.html', pro2)

def project3(request):
    return render(request, 'portfolio-details3.html', pro3)

def project4(request):
    return render(request, 'portfolio-details4.html', pro4)

def project5(request):
    return render(request, 'portfolio-details5.html')

def project6(request):
    return render(request, 'portfolio-details6.html')

def project7(request):
    return render(request, 'portfolio-details7.html')

def project8(request):
    return render(request, 'portfolio-details8.html')

def project9(request):
    return render(request, 'portfolio-details9.html')

def project10(request):
    return render(request, 'portfolio-details10.html')

def project11(request):
    return render(request, 'portfolio-details11.html')

def project12(request):
    return render(request, 'portfolio-details12.html')

def project13(request):
    return render(request, 'portfolio-details13.html')
