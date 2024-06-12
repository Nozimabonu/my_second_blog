from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):  # har doim request keladi majburan

    result = """
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="base.css"

            <title>My Blog</title>
        </head>


        <body>

            <h1 style= "color:green;"> Hello information about myself </h1>
            <style>
                h1 {
                    text-align: center;
                    color:green;
                    padding: auto;
                }

                h2 {
                    text-align: center;
                    color:blue;
                }
            </style>
            <h2>Hello </h2>
            <h3>My name is Nozimabonu</h3>
            <h4>My last name is Hamidova</h4>
            <h5>I'm 17 years old</h5>

            <div class="box-1">
                <h1>My_blog</h1>

                    <p>
                        My family: There are four of us in my family.
                            My parents are Hadichabanu and I. The rules that exist in every family also exist in our family.
                            Everyone has their place in the family and we all sit at the table as a family. Each of us has our own duties.
                            I consider my family to be one of the peaceful and peaceful families.
                            I consider my place and responsibility in the family to be very big, because sometimes when I check my sister, I see my mistakes.
                            I think that the way I treat my parents, depending on me, my sister will be the same.
                            That's why I always try to be worthy of my place and think that I will achieve it.
                            My sister also has her own problems. If we know our problems and correct our mistakes, then our family will be strong and peaceful.
                            For this we need to have more knowledge. I believe that I am one of the luckiest people in the world, because I have a loving family. My family is my pride.

                    </p>
            /div>

            <br>
            <h2>About myself</h2>
            <p>
             If I write about myself.
             I am the oldest child in the family.
             My family is very kind to each other.
             I love my family very much.
            <a href="https://t.me/b_15_09" target= "_blank">My telegram account</a>
            </p>
            <br>
            <h3>Hello Guys</h3>
            <a href="http://www.google.com/" target="_blank">Google</a>
            <br>
            <form method="get">
                <label>Username:
                    <input type="text" name="username"
                </label>
                <br>
                <label>Password:
                    <input type="password" name="password">
                </label>

                <input type="submit" placeholder="">
            </form>
            <!-- <label> Gender:
            <input type="radio">
            <input type="radio">
            </label> -->

            <ol>
                <li>Apple</li>
                <li>Orange</li>
                <li>Cherry</li>
                <li>Banana</li>
                <li>Cucumber</li>
            </ol>

            <img src="picture.png" width="300px" height="200px">


        </body>

    </html>

    """

    return HttpResponse(result)  # Javobini http ko'rinishida yubor <--(1
    # return HttpResponse('Hello Guys!')  # Javobini http ko'rinishida yubor <--(2
