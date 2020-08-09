---


---

<h1 id="portray---product-ranker-and-trend-analysis">PORTRAY - Product Ranker and Trend Analysis</h1>
<p><a href="https://travis-ci.org/joemccann/dillinger"><img src="https://travis-ci.org/joemccann/dillinger.svg?branch=master" alt="Build Status"></a></p>
<h1 id="index">INDEX:</h1>
<ul>
<li>Introduction</li>
<li>Features</li>
<li>Dependencies and Requirements</li>
<li>Installation</li>
<li>Code Documentation</li>
<li>MRCNN Image Model</li>
<li>Reasoning Behind Algorithms</li>
<li>Future Improvements</li>
</ul>
<blockquote>
<p>FLIPKART GRID 2.0 ROUND 3 SUBMISSION<br>
TEAM ILLUMINATI, NSUT<br>
Members - Prabhav, Ridam, Ritvik</p>
</blockquote>
<h1 id="introduction">Introduction</h1>
<p>The notion of fashion has seen a paradigm shift over the years - gone are the days when it was simply seen as a means to fulfil a necessity, as the modern apparel industry today finds its purpose in the conception, production, promotion, and marketing of style on the basis of desire.</p>
<p>Fashion designers and associated companies face new hurdles every day in terms of anticipating the demands of users, designing products in accordance with the latest trends, and then ensuring maximum sales of these products. And as has become characteristic of the times we live in, they too have turned to technology for plausible solutions in the form of intelligent fashion systems that would keep them ahead in the race.</p>
<p>Our proposed solution to the problem statement: Fashion Intelligence Systems is <em>PORTRAY- Product Ranking and Trend Analysis.</em> A one-of-it’s kind solution modelled as a website, it provides the user insights about the trending and lagging products in terms of <strong>ecommerce analysis</strong> and with respect to the <strong>latest trends</strong> at the click of a button.</p>
<h1 id="features">Features</h1>
<p><strong>1. E-Commerce Based Product Vertical Analysis</strong></p>
<ul>
<li>We utilise multiple features to rank products. Our Algorithm is built on 3 major parts -&gt; A modified TextRank Algorithm, A masking MRCNN Image Segmentation Model and a novel PORTRAY scoring algorithm.</li>
<li>Right now we support three websites -&gt; Nordstrom, Amazon USA, SHEIN USA.</li>
<li>Our enhanced adaptive scraping methods can add a new website in 1 hour and a new product in 30 minutes.</li>
</ul>
<p><em>For ECommerce Analysis, you can simply input the website and product of your choice</em><br>
<img src="https://lh5.googleusercontent.com/Qan-kamVEaLa2kXNOCOjIscmwGBNOHiF1V_3UydyX603jo12Xbn1bW_8ihOIq9f5DjxTt9Xcr57-reYbSudMti1hDc-C537V2WZZdfx_ueZNAaUwUYKobQPec97YgEYVwoJ1dHK9" alt=""></p>
<p><em>Our Algorithm displays the top and bottom products in a format that is easy to comprehend</em><br>
<img src="https://lh5.googleusercontent.com/Px1HvjKtBM983BkIzy2ZSNJrZlCKHcchXDpa08AKFTbwcepyJy2xvfRw1IGZK2dJHZLq46aW1bsGExg1ssdiHEwYfuXJPgAeeEDYJsVYEh8zeT1DdHYq5ecSEqyDLJYcwej2SetB" alt=""></p>
<p><strong>2. Trend Analysis Based on Fashion Blogs</strong></p>
<ul>
<li>We also offere trend based analysis from fashion blogs and articles.</li>
<li>We use the articles and blogs to identify features that are in trend for a particular product vertical. Based on this we serve you the top products.</li>
<li>We also provide the latest and top ranked articles that talk about trends in general</li>
<li>Main features we use are Textual Analysis, Image Analysis and Number of Endorsements.</li>
</ul>
<p><img src="https://lh3.googleusercontent.com/0TqCsHhqHj7uei_2NW5-UE40rdnVjkhAXo9KsxPFKTGP99IS-qqgdtYR30kN1YjYmJ3EacfS9aT9mO6JAUSa6ndZa6RBt9H6rcyt2iT591dPGus05iiMKE5K1r5cNKC-aH9h8YBj" alt=""></p>
<p><img src="https://lh4.googleusercontent.com/GjAeJnTHuH_0uPaYt3nyDaNQxCnme_49D8W9z9LoKfeAFMOcmCXPA49YanOkoiN55Zqpeq9yZ5rQXvxLcVyJND8MG26_CdvBtvAab9c_NxgNtolLIzc3z6fAQ4zuqfbqRhELsOIf" alt=""></p>
<h1 id="dependencies-and-requirements">Dependencies and Requirements</h1>
<p>Before you start using <strong>PORTRAY</strong> on your own device, there are a few basic dependencies you need to have. These are listed below:</p>
<ul>
<li><a href="%5Bhttps://www.python.org/downloads/release/python-360/%5D(https://www.python.org/downloads/release/python-360/)">Python 3.6</a> - Main Programming Language.</li>
<li><a href="%5Bhttps://flask.palletsprojects.com/en/1.1.x/%5D(https://flask.palletsprojects.com/en/1.1.x/)">Flask 1.1</a> - Deployment Solution.</li>
<li><a href="%5Bhttps://pip.pypa.io/en/stable/%5D(https://pip.pypa.io/en/stable/)">pip Package Manager</a> - Package manager for Python.</li>
</ul>
<p>Please make sure of these dependecies before moving ahead.</p>
<h1 id="installation">Installation</h1>
<h4 id="install-locally-and-run-on-local-server">Install Locally and Run on Local Server</h4>
<ol>
<li>Visit our <a href="%5Bhttps://github.com/Prabhav55223/Flipkart-PORTRAY%5D(https://github.com/Prabhav55223/Flipkart-PORTRAY)">GitHub Repository</a>.</li>
<li>Clone the Repo to a Local Folder. <strong>Be sure not to alter the Folder Structure</strong>.</li>
<li>Open a terminal and Change Directory to the Folder. Run the following commads:</li>
</ol>
<pre class=" language-sh"><code class="prism  language-sh">$ pip install -r requirements.txt
$ flask
$ set FLASK_APP = app.py
$ flask run
</code></pre>
<p>And that’s it ! Open a Web Browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>. You should see the User Friendly PORTRAY Homepage.</p>
<h4 id="understanding-each-file-and-foleder">Understanding Each File and Foleder</h4>
<p>We understand that understanding what each folder does can be difficult at the first glance. Hence we have taken the liberty to describe the functionality of <strong>the important</strong> files and folder below:</p>
<ul>
<li><strong>/mrcnn</strong> - For our image analysis and segmentation purposes we utilise a technology called Mask-RCNN. This is an implementation of  <a href="https://arxiv.org/abs/1703.06870">Mask R-CNN</a>  on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It’s based on Feature Pyramid Network (FPN) and a ResNet101 backbone.</li>
<li><strong>/static</strong> - This includes all the static files required for hosting the website. This includes the database for our app, environment variables, CSS, Javascript and Images.</li>
<li><strong>/templates</strong> - HTML-5 files for our website. Our project uses JINGA2 templating for Flask.</li>
<li><strong><a href="http://main.py">main.py</a></strong> - The major chunk of our base code. This file contains most of our important algorithms including code to Use MRCNN, Implement TextRank, Scrape Data, Preprocessing Functions, Scoring and Ranking Algorithms and the main API Function -&gt; predictor().</li>
<li><strong><a href="http://trends.py">trends.py</a></strong> - This file contains the code to scrape articles and blogs from websites. It also contains code for the Trend Analysis Section of our App and the corresponding API Function -&gt; articles().</li>
</ul>
<h1 id="code-documentation">Code Documentation</h1>
<p>Below we give a detailed explanation of the main functions and algorithms we use:</p>
<ol>
<li>
<h3 id="predictor-function-ecommerce-analyser">Predictor Function (Ecommerce Analyser)</h3>
</li>
</ol>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">predictor</span><span class="token punctuation">(</span>choice<span class="token punctuation">,</span> query<span class="token punctuation">)</span>
</code></pre>
<p><em>Parameters</em>- Your website choice and product vertical query.<br>
<em>Description</em> - Runs, in order the following steps to provide results:</p>
<ul>
<li>Check to see if the required data has been scraped before or not. If yes, utilises previous defined pattern to collect data using <strong>Selenium</strong>. Builds a dataframe for the same.</li>
<li>Featues collected are Name of Product, Brand, Star Rating, Number of Ratings, Number of Reviews, Current Views, Reviews Textual Data, Price, Discount, Description and Images.</li>
<li>PreProcess the data.</li>
<li>Apply Weighing Reviews Algorithm (Explained Later)</li>
<li>Ranks Products according to Ranking Algo.</li>
<li>Identifies Features according to Image Analysis.</li>
<li>Return Results.</li>
</ul>
<ol start="2">
<li>
<h3 id="review-weight-class">Review Weight Class</h3>
</li>
</ol>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">WeightingReviews</span><span class="token punctuation">:</span>
    
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> df<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>df <span class="token operator">=</span> df <span class="token comment"># Your Data Frame</span>
        self<span class="token punctuation">.</span>k <span class="token operator">=</span> <span class="token number">0.3</span> <span class="token comment"># Constant for Ranking</span>
</code></pre>
<p><em>Description</em> - Runs a TextRank algorithm, described below, to assign numerical weight (Importance) to each Review.</p>
<ul>
<li><strong>TextRank – is a graph-based ranking model</strong> for text processing which can be used in order to find the most relevant sentences in text and also to find keywords.</li>
<li>In order to find relevant keywords, our textrank algorithm constructs a word network. These words are nothing but the collection of all words in reviews. Graph edges are decided on the basis of the <strong>Levenshtein Distance</strong>.</li>
<li>Then the top keywords are found. The frequency of each keywords in a review creates the weights for the review.</li>
</ul>
<p><img src="https://lh3.googleusercontent.com/yYevBrC9I9baiQkQ3iFHGTKC_txFIokk4zeHBBH1bmTX5kMTgpUjkiPaTwl3Wf3brtPxZMEHmflDoP25iZ-CLYzIVgUKiO2odl8YgytpSa1uO6YZQ946YU_X6CkcNvxVcyHAbh9k" alt=""></p>
<ol start="3">
<li>
<h3 id="e-commerce-scraper-class">E-Commerce Scraper Class</h3>
</li>
</ol>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">DataCollectionEcomm</span><span class="token punctuation">:</span>

    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> base_site<span class="token punctuation">,</span> search<span class="token punctuation">,</span> path<span class="token punctuation">,</span> query <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token string">'T-Shirt'</span><span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>browser <span class="token operator">=</span> self<span class="token punctuation">.</span>genrateBroswer<span class="token punctuation">(</span><span class="token punctuation">)</span>
        self<span class="token punctuation">.</span>links <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
        self<span class="token punctuation">.</span>base_site <span class="token operator">=</span> base_site
        self<span class="token punctuation">.</span>path <span class="token operator">=</span> path
        self<span class="token punctuation">.</span>search <span class="token operator">=</span> search
        self<span class="token punctuation">.</span>query <span class="token operator">=</span> query
        self<span class="token punctuation">.</span>df <span class="token operator">=</span> pd<span class="token punctuation">.</span>DataFrame<span class="token punctuation">(</span>columns<span class="token operator">=</span><span class="token punctuation">[</span><span class="token string">"Name"</span><span class="token punctuation">,</span> <span class="token string">"Brand"</span><span class="token punctuation">,</span> <span class="token string">"Price"</span><span class="token punctuation">,</span> <span class="token string">"Discount"</span><span class="token punctuation">,</span> <span class="token string">"Image_Link"</span><span class="token punctuation">,</span> <span class="token string">"Rating"</span><span class="token punctuation">,</span> <span class="token string">"Number of Ratings"</span><span class="token punctuation">,</span> <span class="token string">"Reviews"</span><span class="token punctuation">,</span> <span class="token string">"Current Views"</span><span class="token punctuation">,</span> <span class="token string">"Description"</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
</code></pre>
<p><em>Description</em> - State of the art adaptive Scraper. It identifies the difference between a dynamic website and static website and utilises Selenium Expected Conditional Statements to scrape data in the fastest manner possible.</p>
<blockquote>
<p>Though our code includes an option to Scrape Data Locally, we recommend requesting for additions through the website. That ensures security and accuracy.</p>
</blockquote>
<ol start="4">
<li>
<h3 id="article-analyser-function">Article Analyser Function</h3>
</li>
</ol>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">articles</span><span class="token punctuation">(</span>website<span class="token punctuation">,</span> product<span class="token punctuation">)</span>
</code></pre>
<p><em>Parameters</em>- Your website choice and product vertical query.<br>
<em>Description</em> - Runs, in order the following steps to provide results:</p>
<ul>
<li>Scrapes latest articles from webisted like VOGUE and builds a database.</li>
<li>Uses a self implemented algorithm based on dictionary to assign each article a category based on the product.</li>
<li>First, returns the top articles based on time of release, relevancy to the product vertical and number of endorsements.</li>
<li>Also runs similarity calculation between description of products in database related to product vertical and gives top 5 products based on that.</li>
</ul>
<h1 id="example-of-image-segmentation">Example of Image Segmentation</h1>
<ol>
<li>
<p>Below example shows the  model segmenting the image into features.<br>
<img src="https://lh6.googleusercontent.com/iwg5fytRrD6qPRZyg_NB9f8-plFa6O_jKnyVAN33xjXibXm8ns7DOUwvPZZGpbwh8raaZKRWyBb2fBntIQVQteafy9V0AYpLNA9lVyFz3cSIini-GgMKbF7aMeVhSiuqWzmatGFx" alt=""><br>
<img src="https://lh5.googleusercontent.com/eza5MOqTC5MJBOMzXdVb9X5SAxViwdG9yceh1J9ItBKwZIB9zmiCUebPoYNeVV9IS5HccGAIV2Oszqp9-usaep1LSj_gDBtSMryqSsqBnDuRjimOQ-FK46d3PoRKJ0x-OawubA1Y" alt=""></p>
</li>
<li>
<p>Featues are shown below.<br>
<img src="https://lh6.googleusercontent.com/emuYET_aaugCt_zgmK676Mh7zuYnVx6JVlmDimXh8OiDHe1cBuv0E5opc_3ixVNBkBGEHZZeL7NwP-ugM9RVfQtaKHnnlIPrjj-diFgjy-Pu6SHLjA0pat8jLe-sahLkWOaiZ07w" alt=""></p>
</li>
<li>
<p>Our Image MRCNN Model was trained on COCO Weights and used the 'Fashionista Open Source Dataset" to train. The results for 3 epochs are shown below.<br>
(Photo from websi</p>
</li>
</ol>
<p><img src="https://lh6.googleusercontent.com/CYz_T1Rr-nRyO1JnsUQKH3rxtDIf0aH1OYxwjbnTcySGvkS5mcZfrYkwje7L_eAaHbcODy-jYnoWaEOPwwk4WpvbFvOAsawF8WcY-IUmRQbPVGovwLT5y8dRdN6zg9esrAYlZ6Br" alt=""></p>
<ol start="4">
<li>Below is an example of a segmented product. We see how the model identifies dress, top, neckline,shoes and pants.<br>
<img src="https://lh5.googleusercontent.com/RMvf08KyrtvE4Jt_lJ2jSFJPRFaaZrB6XvNnhdeb0vY0OJ4GBREASr_SHguAKx_-ZfkgKECyNHKUZ9LW1GCu551IWf4Py-k_eXRuzfMs1JwXwqgnkWT9s1cXyTHD4bwCRVzVDV9S" alt=""></li>
</ol>
<h1 id="reasoning-behind-algorithms">Reasoning Behind Algorithms</h1>
<h3 id="for-ecommerce-analysis">For ECommerce Analysis</h3>
<p>For the purpose of ranking products from eCommerce websites, the approach adopted is described as follows :</p>
<ol>
<li>The following parameters are scraped from the website under consideration-</li>
</ol>
<ul>
<li>Star Rating, Number of Views, Number of Rating- Using the star rating alone gives information regarding the product’s popularity. Coupled with the number of views and number of ratings, it gives us the percentage acceptance of the product.</li>
<li>Customer Review &amp; Customer Rating (Individual)- We use a technique of <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.892.5478&amp;rep=rep1&amp;type=pdf">assigning weights to each review.</a>  We came up with a dictionary of words that are considered “Relevant” to designers and depending on the frequency of such words in a review, and also the correlation and similarity, it is assigned a weight which is multiplied by the rating.</li>
<li>Price and Discount- For discount, <a href="https://www.entrepreneur.com/article/220091">multiple research</a> studies show that an abnormally “High Discount” shows “Obsolete Inventory and slow-selling products”. Hence in our algorithm, we penalise discounts higher than the average calculated mean of Discounts in that season.</li>
<li>For the price, we focus specifically on extremely high priced and extremely low priced. Our algorithm is based around the idea that a negatively rated (Calculated using the above two columns) product with low price must be penalised heavily while a positively rated product with high price must be incentivised heavily.</li>
<li>Image and Description- Utilising a deep neural network, Mask RCNN, we analyse the product’s image to segment out it’s finer features such as ‘sleeves’ and ‘necklines’ which may or may not be mentioned in the description.</li>
</ul>
<ol start="2">
<li>Utilising the above parameters:<br>
First two different scores (r and r2) are calculated. They store information regarding Star Rating, Number of ratings etc and also reflect the weighted score of each review. To perform the assignment of weights, the following steps were followed:</li>
</ol>
<ul>
<li>
<p>A corpus of all reviews was prepared after they were subjected to basic pre-processing</p>
</li>
<li>
<p>Using a self-written function similar to the implementation of python’s Textrank, the top 50 keywords from this corpus were extracted</p>
</li>
<li>
<p>Each review was compared with this corpus of keywords and assigned a score according to the similarity</p>
<p>This gives us the parameter ‘r’.</p>
</li>
<li>
<p>We then penalise OR incentivise this score based on a factor calculated on basis of Deviation from the mean (For both price and discount). So if a product is priced higher than 2 times or lower than 0.5 times the mean AND it enters the second conditional block wherein, if the product has a negative R score it is penalised (due to extreme price and bad rating ) and if it has a positive R, it is incentivised.</p>
</li>
<li>
<p>A similar logic is followed for discount, though the product is not penalised for less or no discount, but only for exceptionally high discount. In the figure, Average is defined as the average of that product vertical reflected in total collected data</p>
</li>
</ul>
<p><em>Figure displaying approach for ranking ECommerce Products</em><br>
<img src="https://lh6.googleusercontent.com/cSrYoLdtbw89HZGGevZud-szB_XuJlFmKc8qitFjUzVf54xC9ESQqsvqw3Ipf-6di1W4ON0ySr6qEVrUx_IO3clvYUf0wkTOZk3BJpq9-UpLT-EpqzR8EzBccF-tFv_QUAI30U6X" alt=""></p>
<ol start="3">
<li>Displaying results</li>
</ol>
<ul>
<li>Based on the final calculated score, the final top and bottom products are displayed in the form of descriptive cards containing product image and score.</li>
<li>In addition, using parameters extracted from Mask RCNN and keywords from the product description, product features are displayed so as to assist the user in observing whatspecific features caused the product to be ranked higher/lower.</li>
</ul>
<h3 id="for-trend-analysis">For Trend Analysis</h3>
<p>Following is the approach for identifying the top and bottom products from a given website based on the latest trends:</p>
<ol>
<li>
<p>Articles from fashion websites are scraped and their data converted to a suitable format<br>
<img src="https://lh4.googleusercontent.com/JrOFRMHHi-YLWjwKrGqDGFlKxy0CsTRMe4pyQ_SJJCmVG77BBsEwvRTrC1vSrdm50tGA3OWQLe81cqwwhMisTiUO4UBLWIcNUuhHQopccYgLNMwo1vKQR9MReR8BG9e9TPpIZAVz" alt=""></p>
</li>
<li>
<p>The date from the articles is converted to a timestamp and based on it, a parameter ‘DScore’ is calculated, with the most recent article getting a score of 10 and the oldest one being allotted a score of 0. This is to ensure that the most recent trends at any given time are considered.</p>
</li>
<li>
<p>Post this, the ‘Title’,‘Text’ and ‘Tags’ of an article are passed through a function that returns keywords that fall under the category of ‘Proper Nouns’. The count of these proper nouns are scaled between 0 and 10 and this is used as ‘EScore’ (Endorsement Score). This parameter serves as a measure of the number of endorsements or celebrity names associated with an article, indicating higher chances of it emerging as a trend.</p>
</li>
<li>
<p>A dictionary is created containing keywords for identifying which product a particular article is primarily talking about. Using this dictionary and by comparing the title and if need be, the text of an article, an article is allotted a category indicating the particular fashion apparel the article is concerned with. If the article talks about trends in general, it is given a category of ‘none’.</p>
</li>
<li>
<p>Following this, using a self-written function, keywords from the Title and Text of the article are extracted, leading to our articles dataframe being converted to this format:</p>
</li>
</ol>
<p><em>Final Articles Data</em><br>
<img src="https://lh3.googleusercontent.com/4qqqjTgJ-sV__M8lCGDy9jn9q1KMUic1moT4EBVqnbad1TUmpq3cFtSzPZREay9nkp1RGtyvUy_CQ7mri7mZFzUl5huuC9_DVEj4sG_E8x2saiciYAmMMwZdpOi6ZNdCE9wjU1Kh" alt=""></p>
<ol start="6">
<li>Next, the data from a given website regarding a given product is converted to a suitable dataframe and it’s columns ‘Name’ and ‘Description’ are subjected to basic pre-processing.</li>
</ol>
<p><em>Tshirt Data from <a href="http://nordstrom.com/">http://nordstrom.com/</a></em><br>
<img src="https://lh5.googleusercontent.com/XojjgjUFSuhDQ5MQfg5Hc1FT_L-jrEFdyBOzS1dbbLRJpiemdjWw5OckIRx504jnPw_JVifX2kxQaEZppy3A-YDIy95joYTGzY3G2xYSTv-NW1s8NZYWa-g6cuHHwI00zQLeLS-D" alt=""></p>
<ol start="8">
<li>
<p>Now, using the data of the articles, only those articles whose category is ‘none’ (i.e. they talk about general trends) and those whose category matches that of the given product (‘tshirt’ in this case) are selected and their data segregated. The product names and product descriptions are compared with the extracted keywords of the text of these selected articles and a parameter ‘tscore’ is calculated based on the number of matches.</p>
</li>
<li>
<p>Lastly, the final score of the products, ‘AScore’ is calculated as :<br>
<strong>AScore= (DScore+ EScore+ tscore)/3</strong></p>
</li>
</ol>
<p>All this is displayed below in a flowchart:<br>
<img src="https://lh5.googleusercontent.com/6oPu1IFG4aLM13rFUE7YosNCtZSDqMMU_mNNd3aUtk5U-qzEVu55sxnA7y6f2OH0i1lxVAu_aVJJuKhjp-_lrIBCUgCqdR3ZGk4wQj-ikK7d0fDLynnpcuuvDjZ5SspPxzJLYpid" alt=""></p>
<h1 id="future-improvements">Future Improvements</h1>
<ol>
<li>We aim to improve the speed of scraping in future builds. We have planned to utilise Selenium-Scrapy (A framework that utilises automation via Selenium and Scraping via Scrapy to improve speed) for all our scraping tasks.</li>
<li>Utilising better algorithms for Trend Classification. We have only considered 3 features for Trend Classification as of now and we hope to expand the list to include more features that carry more weight.</li>
<li>Including a better Pre-trained LSTM Network Model for Keyword Extraction.</li>
<li>We also aim to use GAN’s to build a system that can not only identify trends, but also automatically learn from these trends and design samples that are likely to succeed.</li>
</ol>
<h1 id="suggestions">Suggestions</h1>
<ol>
<li>We would love to learn more about your suggestions. We request you to add all submission as <strong>Issues</strong> on our GitHub Repo.</li>
</ol>
<h1 id="license">License</h1>
<p>MIT</p>

