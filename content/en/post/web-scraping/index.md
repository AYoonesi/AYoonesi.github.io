+++
author = "Erwin"
title = "Web Scraping Series: 01 Intro"
date = "2022-10-14"
description = "Is the Iraq War to Blame for the Economic Collapse? War is difficult enough to discuss; the Iraq conflict is far more complicated. Let’s take a different path: Keynesian Economics."
tags = [
    "Web Scraping",
    "Python",
    "Articles",
    "Medium",
    "Programming", "Data Science", 
]
categories = [
    "Programming",
    "Python",
    "Articles",
]
series = ["Articles"]
+++

![What exactly is web scraping?](/post/web-scraping/intro.png "What exactly is web scraping?")

<div class="news-lead">
Data can also be obtained by scraping web pages. It turns out that fetching online pages is simple; obtaining useful structured information from them is more difficult.
</div>
<!--more-->

## Intro

Putting APIs aside, data may also be obtained through scraping web pages. It turns out that retrieving online pages is quite simple, but extrapolating useful, organized information from them is more difficult.

Let's say you're looking for information on a website. Let's talk a little bit about Milton friedman! How do you behave? You might, however, copy the data from Wikipedia and put it into your own file. But what if you need a website to provide you with a lot of information as rapidly as possible? Using a website's massive volumes of data to train a machine learning algorithm? Copying and pasting won't work in this circumstance! And at that point, web scraping will be required.

Web scraping employs intelligent automation approaches to get hundreds or even millions of data sets in less time than the tedious and time-consuming process of manually gathering data. So let's explore Web scraping in more detail and learn how to apply it to get information from other websites.

## What Is Web Scraping?

Web scraping is a computerized technique for gathering copious volumes of data from websites. The majority of this data is unstructured in HTML format and is transformed into structured data in a database or spreadsheet so that it may be used in multiple applications. To collect data from websites, web scraping may be done in a variety of methods. These include leveraging specific APIs, online services, or even writing your own code from scratch for web scraping.

You may access the structured data on many huge websites, like Google, Twitter, Facebook, StackOverflow, and others, via their APIs. This is the greatest choice, however there are alternative websites that either lack the technological sophistication or don't let users to access significant volumes of structured data. In that case, it's advisable to employ web scraping to get data from the website.

The scraper and the crawler are the two components needed for web scraping. The crawler is an artificial intelligence system that searches the internet for the specific data needed by clicking on links. On the other hand, the scraper is a unique tool designed to extract data from the website. The scraper's architecture might vary significantly depending on the difficulty and size of the project in order to efficiently and precisely extract the data.

## HTML

Pages on the web are written in HTML, in which text is (ideally) marked up into elements and their attributes:

    <html>
        <head>
            <title>A web page</title>
        </head>
    <body>
        <p id="author">Alireza Yoonesi</p>
        <p id="subject">Machine Learning</p>
    </body>
    </html>

We would be able to extract data using rules like "find the *p* element whose id is topic and return the text it contains" in a perfect world where all web pages were semantically marked up for our convenience. HTML isn't often well-formed or annotated in the real world. Thus, we will require assistance in understanding it.

The [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) package, which creates a tree out of the various components on a web page and offers a straightforward interface for accessing them, will be used to extract data from HTML. We'll be using Beautiful Soup 4.11.1 (April 8, 2022), which is the most recent version as of this writing. We’ll also be using the Requests library, which is a much nicer way of making HTTP requests than anything that’s built into Python.

Python’s built-in HTML parser is not that lenient, which means that it doesn’t always cope well with HTML that’s not perfectly formed.  For that reason, we’ll also install the html5lib parser.

<hr/>

# To Be Continued!

**You may read the full articles on my [Medium](https://medium.com/@AYoonesi/).**
# [Did The War In Iraq Create Jobs For Americans?](https://medium.com/@AYoonesi/did-the-war-in-iraq-create-jobs-for-americans-654bd03a388a)


