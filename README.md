<h1>"BillBlakeBot"<h1>
============
<p><h4>This python library is available for use under a <a href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons license</a>. Please give attribution to myself and Megan Speir if you choose to use or fork this script.</h4></p>  

<p><h4><a href="www.twitter.com/autoblake">@autoblake</a> is a Twitter bot that tweets Markov-chain generated lines from David Erdman's <i>The Complete Poetry and Prose of William Blake</i>.</h4></p>

<p><h2>About</h2></p>
<p>@autoblake is a fork of Megan Speir's <a href = "https://github.com/MeganSpeir/Markov-Tweet">"Markov_Tweet.py"</a> that grabs words from Blake's corpus, then forms a chain of text based upon the probability that one particular word follows another. 

<p><h2>Installation</h2></p>
<p>To create your own text-based Markov Twitter bot, do the following:</p>
<ol><li>Download the python libraries that "BillBlakeBot" needs to function. Make sure you get the most recent versions.</li>
<ul><li><a href="https://pypi.python.org/pypi/virtualenv">virtualenv</a>: Allows you to sidestep security issues that pop up whenever python scripts require write access to your server. "virtualenv" also includes several libraries like "pip" and "easy_install" that make installing new libraries much easier.</li>
<li><a href="https://pypi.python.org/pypi/simplejson">simplejson</a>:Allows you to access the Twitter API, in order to generate tweets.</li>
<li><a href="https://pypi.python.org/pypi/oauth2">oauth2</a>: Sends requests to the Twitter API, in the form of consumer keys and access tokens.</li>
<li><a href="https://code.google.com/p/httplib2/">httplib2</a>: HTTP Client Library that gives the program the ability to execute HTTP requests.</li>
<li><a href="https://github.com/MeganSpeir/Markov-Tweet/tree/master/python-twitter">python twitter</a>: Allows you to interface with the Twitter API.</li></ul>
<li>Find a server to host your bot, and ssh connect to that server using the command line. <a href="http://gssg-www.stanford.edu/public/ssh/SSHExamples.html">Here</a> is a good overview of using ssh to connect to a remote server with the command line.</li>
<li>Make the following changes to the code in the package:</li>
<ul><li>In "markov_class.py</li></ul>
<ul><ul><li>Change <code>twitter_handle</code> on line 53 with your intended handle.</li>
<li>If you are unhappy with the number of words in the sentence, the amount of randomness, or the patterns, you may want to change the value on line 36 to suit your particular needs. The base is "2", but different corpuses work differently.</li></ul></ul>
<ul><li>In "markov_tweet.py</li></ul>
<ul><ul><li>Change <code>handle = "autoblake"</code> with your intended handle.</li>
<li>Create an application on <a href="http://dev.twitter.com">http://dev.twitter.com</a>, change the settings for "OAuth" and "Your Access Token" to "read and write" (default is read-only), generate an access token, and take note of the consumer key, consumer secret, access token, and access token secret.</li>
<li>Put the specified values in the appropriate spaces in lines 33-6 (ex, tokens and secrets are often written in this manner "5g&i983T$fq").
<li>If you wish to use a corpus besides blake.txt, save intended corpus in a txt file (NOT a .doc file), place in "BillBlakeBot" folder, and replace <code>f=open(blake.txt)</code> on line 25 with the filename of your corpus.</li>
<li>If you are unhappy with the result of the Markov chain you generate, change <code>order = int(2)</code> on line 10 with a different Markov order. Higher order numbers tend to generate more repetition, while lower order numbers tend to generate more randomness.</li></ul></ul>  
<li>Upload the "Markov-Tweet" folder to your server.</li>
<li>Initiate the script by ssh-ing back into your server and, in the correct folder, typing <code>python markov_tweet.py</code>.
<li>If the script works, set it to initiate every few hours (3-6 at the least) by setting it to Cron, either with your web service (most hosts have an interface for cronjobs) or by following the instructions <a href="http://stackoverflow.com/questions/373335/suggestions-for-a-cron-like-scheduler-in-python">here</a>.</li></ol>








 

 
