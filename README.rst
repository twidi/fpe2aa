FPE2AA - French Presendential Election 2012, Applications Aggregator (temporary name)
=====================================================================================

FPE2AA is a project to collect all "applications" available about the presidential election in France for 2012

WIP


----

Command to collect static files::

    ./manage.py collectstatic -l --noinput -i less -i bs -i "*.sh" -i "*.json*" -i "*.html"

To regenerate app.css::


    # you must avec lesscss installed
    cd source/project/static
    sh build-app.sh

