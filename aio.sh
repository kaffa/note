#!/bin/bash
#
# nikola 推 github
cd ~/web/note.tt4e.com/
nikola build
git add .
git commit -am 'Kaffa'
git push
