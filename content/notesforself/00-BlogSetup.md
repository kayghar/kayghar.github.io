title: Blog Setup
slug: blogsetup
category: Notes for Self
date:2019-09-01
modified:2019-10-14
password:zkkS]GWwZ%N(;F>q)k*3XO6?

# Blog Setup

## Conda

Start by creating a new conda env for pelican and install

    conda create -n pelican
    conda install python pip markdown
    pip install pelican

## Pelican

Then go to the kayghar.github.io folder and initiate the website

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

And we can get python's http server to server the contents of output/ on
socket 8000:

    python -m http.server -d output/

Make changes and repeat. When we're happy we should push to remote. The
question is how to automate pushing to GitHub pages.

  1. Develop on branch gh-pages.
  2. make publish, iterate.
  3. When happy, git add ., git commit, git push.
  4. When ready to Actually Push (TM), checkout branch master.

Now we need to copy contents of /output from branch gh-pages to the root
folder in branch master, git commit, and pit push. Let's write a
script that does that:

    #!/bin/bash

    commitmessage="`git log --format=%B -n 1 gh-pages`"
    git checkout gh-pages -- output/
    cp -r output/* ./
    rm -r output/
    git add .
    git commit -m "$commitmessage -- Copied to branch master."
    git push

This script is saved as deployfrombranch.sh added to gitignore. And, I
believe we are done!

## Other features

### Adding Password Protection

Using [mindcruzer's extension](https://github.com/mindcruzer/pelican-encrypt-content)
I have added password protection to certain pages. The passwords can be found
in the 1password vault.

* git clone the encrypt_content folder in the root pelican project folder.
* Add the following to your pelicanconf.py file:

        PLUGINS = ['encrypt_content']
        ENCRYPT_CONTENT = {
        'title_prefix': '[Encrypted]',
        'summary': 'This content is encrypted.'
        }

* Inside the .md source file, add the password in the preamble.

        title:mytitle
        etc
        password:mypassword

### Colour Picker

For mockup-dev, an advanced colour picker is needed. Gpick is good choice.
