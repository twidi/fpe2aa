if (ANALYTICS_CODE) {
    $(document).ready(function(){
        $('a.app-link').click(function() {
            var link = $(this),
                app = link.data('app');
            if (!app) { return true; }
            if (typeof(_gaq) != 'undefined') {
                _gaq.push(['_trackEvent', 'Applications', 'click', app]);
            }
        });
    });
}




