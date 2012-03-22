#!/usr/bin/env bash

mkdir css/bs/
~/bin/lessc css/less/bootstrap.less css/bs/bootstrap.css
~/bin/lessc css/less/responsive.less css/bs/bootstrap-responsive.css
~/bin/lessc --compress css/less/bootstrap.less css/bs/bootstrap.min.css
~/bin/lessc --compress css/less/responsive.less css/bs/bootstrap-responsive.min.css

# edit the few lines below to not include responsive's css into final bootstrap css

cat css/bs/bootstrap.css css/bs/bootstrap-responsive.css >> css/bootstrap.css
cat css/bs/bootstrap.min.css css/bs/bootstrap-responsive.min.css >> css/bootstrap.min.css


