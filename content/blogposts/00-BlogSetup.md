title: Blog Setup
slug: blogsetup
category: Posts
date:2019-09-01
modified:2019-09-01

# Blog Setup

Start by creating a new conda env for pelican and install

    conda create -n pelican
    conda install python pip markdown
    pip install pelican

Then go to the kayghar.markdown.io folder and initiate the website

    pelican-quickstart

Then go to /content and make this md file as the first blog post.

    cd content
    mkdir blogposts journal
    cd blogposts
    touch 00-BlogSetup.md

The markdown file must include a title: line in the beginning, as well as
other optional ones:

    title: Blog Setup
    slug: blogsetup
    category: Posts
    date:2019-09-01
    modified:2019-09-01

Now, running either of the following will create all the static html files
in /output

    make html
    make publish

The question is how to automate pushing to GitHub pages.
