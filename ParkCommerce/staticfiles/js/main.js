let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');
if (searchForm) {
    for(let i=0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function(e){
            e.preventDefault();
            let page = this.dataset.page;
            
            searchForm.innerHTML += `<input value=${page} name="page" type="hidden" />`;

            searchForm.submit();
        });
    }
}
    // $(document).ready(function() {
    //     $('.pagination').find('a').click(function(e) {
    //         e.preventDefault();
    //         var page = $(this).data('page');
    //         var url = window.location.href;
    //         var newUrl = url.replace(/page=\d+/, "page=" + page);
    //         window.location.href = newUrl;
    //     });
    // });