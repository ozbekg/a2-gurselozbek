
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, request
from hash_password import create_hash
global first
global last 
global comments
from bottle import static_file

import datetime
import time
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')




comments = []
hash_pw = "0c86f2dfd04b5d52de85408b658cd99e053d9010b38c56da20673c9a891e9746"

def html_index():
	#cmnts= html_comments()
	content = """
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Breaking Bad</title>
        <link href="https://fonts.googleapis.com/css?family=PT+Mono" rel="stylesheet">
        <link rel="stylesheet" type="text/css"
              href="/static/css/style.css">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">


    </head>
    <body>
        <header>
            <div class="container">
                <div class="logo">
                    <a href="/">
                        <img src="/static/img/logo2.png"/> </a>    
                </div>
                <div class="nav">
                    <ul>
                        <li><a class="active" href="/">Home</a></li>
                        <li><a href="/cast">Cast</a></li>
                        <li><a href="/awards">Awards</a></li>
                    </ul>
                </div>
            </div>
        </header>
        <section class="caption">
                <div class="container">

                    <p class="shadow">
                        Breaking Bad is a crime drama TV series. The show viewed for 5 seasons and highly accepted as one of the best TV series.
                    </p>
                </div>
        </section>

        <section class="content">
            <div class="container">


                <div class="half">
                    <h3>Storyline</h3>
                    <p>
                        Walter White is a chemistry genius and works as a teacher in high school. He lives with his wife and a disabled child.
                    </p>
                    <p>
                        He is diagnosed with lung cancer and given amount of time to live.
                    </p>

                    <p>
                        To ensure his family's future financial security, White chooses to enter the risky world of drugs.
                    </p>

                    <p>
                        Teaming up with his former student Jesse Pinkman, he begins to producing and selling methamphetamine.
                    </p>
                </div>
            </div>
        </section>
        <section class="content">
            <div class="container">
				<form method="post" action="/">
			    <textarea id="comment" name="comment" placeholder="Write something.." style="height:200px"></textarea>
			    <input type="password" id="password" name="password" placeholder="Password">           
				<input type="submit" value="Submit">                
			    </form>	
		    	<div class="comments">%s</div>          
            </div>
        </section>
    </body>
</html>""" %(html_comments())
	return content

def html_cast():
	content = """
<!doctype html>	
<html>
    <head>
        <meta charset="UTF-8">
        <title>Breaking Bad</title>
        <link href="https://fonts.googleapis.com/css?family=PT+Mono" rel="stylesheet">
        <link rel="stylesheet" type="text/css"
              href="/static/css/style.css">
    </head>
    <body>
        <header>
            <div class="container">
                <div class="logo">
                    <a href="/">
                        <img alt="logo" src="/static/img/logo2.png"/> </a>
                </div>
                <div class="nav">
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a class="active" href="/cast">Cast</a></li>
                        <li><a href="/awards">Awards</a></li>
                    </ul>
                </div>
            </div>
        </header>

        <section id="cast">
           <div class="container">
                <div id="content">
                        <div style="grid-area: A;text-align: right" class="info">
                            <h4>Walter White</h4>
                            <h5>Bryan Cranston</h5>
                        </div>

                        <div class="image-wrapper" style="grid-area: B;">
                            <img class="croppedImg" src="/static/img/ww.jpg" alt="Walter White" >
                        </div>


                        <div class="image-wrapper" style="grid-area: E;">
                            <img alt="Aaron Paul" class="croppedImg" src="/static/img/jp.jpg"/>
                        </div>
                        <div style="grid-area: F;text-align: left" class="info">
                            <h4>Jesse Pinkman</h4>
                            <h5>Aaron Paul</h5>
                        </div>




                        <div style="grid-area: G;text-align: right" class="info">
                            <h4> Skyler White</h4>
                            <h5>Anna Gunn	</h5>
                        </div>

                        <div class="image-wrapper" style="grid-area: H;">
                            <img alt="Skyler" class="croppedImg" src="/static/img/skyler.jpg"/>
                        </div>


                        <div class="image-wrapper" style="grid-area: I;">
                            <img alt="Hank"class="croppedImg" src="/static/img/hank.jpg"/>
                        </div>
                        <div style="grid-area: J;text-align: left" class="info">
                            <h4> Hank Schrader</h4>
                            <h5>Dean Norris	</h5>
                        </div>


                        <div style="grid-area: K;text-align: right" class="info">
                            <h4> Marie Schrader</h4>
                            <h5>Betsy Brandt	</h5>
                        </div>

                        <div class="image-wrapper" style="grid-area: L;">
                            <img alt="marie" class="croppedImg" src="/static/img/marie.jpg"/>
                        </div>


                        <div class="image-wrapper" style="grid-area: M;">
                            <img alt="junior" class="croppedImg" src="/static/img/jr.jpg"/>
                        </div>
                        <div style="grid-area: N;text-align: left" class="info">
                            <h4> Walter White, Jr.</h4>
                            <h5>RJ Mitte</h5>
                        </div>

                        <div style="grid-area: O;text-align: right" class="info">
                            <h4> Saul Goodman</h4>
                            <h5>Bob Odenkirk	</h5>
                        </div>

                        <div class="image-wrapper" style="grid-area: P;">
                            <img alt="saul" class="croppedImg" src="/static/img/saul.jpg"/>
                        </div>


                        <div class="image-wrapper" style="grid-area: R;">
                            <img  alt="mike" class="croppedImg" src="/static/img/mike.jpg"/>
                        </div>
                        <div style="grid-area: S;text-align: left" class="info">
                            <h4> Mike Ehrmantraut</h4>
                            <h5>Jonathan Banks	</h5>
                        </div>
               </div>
               <br><hr><br>
                <h4>References</h4>
                <a target="_blank" class="reference" href="https://www.imdb.com/title/tt0903747/">https://www.imdb.com/title/tt0903747/</a>
                <br>
           </div>
        </section>
    </body>
</html>

	"""
	return content
def html_awards():
	content = """
	<!doctype html>
	<html>
	    <head>
	        <meta charset="UTF-8">
	        <title>Breaking Bad</title>
	        <link href="https://fonts.googleapis.com/css?family=PT+Mono" rel="stylesheet">
	        <link rel="stylesheet" type="text/css"
	              href="/static/css/style.css">
	    </head>
	    <body>
	        <header>
	            <div class="container">
	                <div class="logo">
	                    <a href="/">
	                        <img src="/static/img/logo2.png" alt="logo"/> </a>
	                </div>
	                <div class="nav">
	                    <ul>
	                        <li><a href="/">Home</a></li>
	                        <li><a href="/cast">Cast</a></li>
	                        <li><a class="active" href="/awards">Awards</a></li>
	                    </ul>
	                </div>
	            </div>
	        </header>

	        <section id="awards">
	            <div class="container">

	                <img src="/static/img/breaking_bad.jpg" alt="award">

	                <table>
	                    <tr>
	                        <th>Contest</th>
	                        <th>Year</th>
	                        <th>Category</th>
	                        <th>Winner</th>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2008    </td>
	                        <td>Outstanding Lead Actor in a Drama Series	</td>
	                        <td>Bryan Cranston (for "Pilot")	</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2009</td>
	                        <td>Outstanding Lead Actor in a Drama Series</td>
	                        <td>Bryan Cranston (for "Phoenix")	</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2010</td>
	                        <td>Outstanding Lead Actor in a Drama Series	</td>
	                        <td>Bryan Cranston (for "Full Measure")	</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2010</td>
	                        <td>Outstanding Supporting Actor in a Drama Series	</td>
	                        <td>Aaron Paul (for "Half Measures")</td>
	                    </tr>

	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2012</td>
	                        <td>Outstanding Supporting Actor in a Drama Series	</td>
	                        <td>Aaron Paul (for "End Times")</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2013</td>
	                        <td>Outstanding Drama Series		</td>
	                        <td>Breaking Bad</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2013</td>
	                        <td>Outstanding Supporting Actress in a Drama Series		</td>
	                        <td>Anna Gunn (for "Fifty-One")</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2014</td>
	                        <td>Outstanding Drama Series			</td>
	                        <td>Breaking Bad</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2014</td>
	                        <td>Outstanding Writing for a Drama Series</td>
	                        <td>Moira Walley-Beckett (for "Ozymandias")</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2014</td>
	                        <td>Outstanding Lead Actor in a Drama Series	</td>
	                        <td>Bryan Cranston (for "Ozymandias")	</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2014</td>
	                        <td>Outstanding Supporting Actress in a Drama Series		</td>
	                        <td>Anna Gunn (for "Ozymandias")	</td>
	                    </tr>
	                    <tr>
	                        <td>Primetime Emmy Awards</td>
	                        <td>2014</td>
	                        <td>Outstanding Supporting Actor in a Drama Series		</td>
	                        <td>Aaron Paul (for "Confessions")	</td>
	                    </tr>

	                    <tr>
	                        <td>Creative Arts Emmy Awards</td>
	                        <td>2008</td>
	                        <td>Outstanding Single-Camera Picture Editing for a Drama Series		</td>
	                        <td>Lynne Willingham</td>
	                    </tr>
	                    <tr>
	                        <td>Creative Arts Emmy Awards</td>
	                        <td>2009</td>
	                        <td>Outstanding Single-Camera Picture Editing for a Drama Series		</td>
	                        <td>Lynne Willingham</td>
	                    </tr>
	                    <tr>
	                        <td>Creative Arts Emmy Awards</td>
	                        <td>2013</td>
	                        <td>Outstanding Single-Camera Picture Editing for a Drama Series		</td>
	                        <td>Kelley Dixon	</td>
	                    </tr>
	                    <tr>
	                        <td>Creative Arts Emmy Awards</td>
	                        <td>2014</td>
	                        <td>Outstanding Single-Camera Picture Editing for a Drama Series		</td>
	                        <td>Skip MacDonald	</td>
	                    </tr>
	                    <tr>
	                        <td>Golden Globe Awards</td>
	                        <td>2014</td>
	                        <td>Best Television Series – Drama</td>
	                        <td>Breaking Bad</td>
	                    </tr>
	                    <tr>
	                        <td>Golden Globe Awards</td>
	                        <td>2014</td>
	                        <td>Best Actor in a Television Series – Drama	</td>
	                        <td>Bryan Cranston	</td>
	                    </tr>

	                </table>
	                <br><hr><br>
	                <h4>References</h4>
	                <a target="_blank" class="reference" href="https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_Breaking_Bad">https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_Breaking_Bad</a>
	                <br>
	            </div>
	        </section>
	    </body>
	</html>

	"""
	return content
def html_comments():
	global comments
	text = '<ul>'
	for i in range(0,len(comments)):
		text += '<li class="comment"><i class="far fa-comment"></i>'+comments[i]["comment"]+'<span class="timestamp">'+comments[i]["time"]+'</span></li>'
	text += '</ul>'
	return text

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page


@route('/', method="POST")
def formhandler():

    """Handle the form submission"""
    global hash_pw
    comment = request.forms.get('comment')
    password = request.forms.get('password')
    password = create_hash(password)
    global comments
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    dic = {"comment":comment,"time":st} 
    if hash_pw == password:
    	comments.insert(0,dic)
    return html_index()


route('/', 'GET', html_index)
route('/cast', 'GET', html_cast)
route('/awards', 'GET', html_awards)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

