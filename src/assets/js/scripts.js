document.addEventListener('DOMContentLoaded', function() {
    /** Page identifiers **/
    const ticketForm = document.getElementById('ticket_form');

    /** Scripts for Ticket page **/
    if (ticketForm) {
        const statusField = document.getElementById('id_status');
        const shopField = document.getElementById('id_shop');
        const shopFieldContainer = getNthParent(shopField, 5);

        statusField.addEventListener('change', function(e) {
            updateShopField();
        });
        updateShopField();

        function updateShopField() {
            if (statusField.value == 5) {
                shopFieldContainer.style.display = 'block';
            } else {
                shopFieldContainer.style.display = 'none';
                shopField.value = "";
            }
        };
    }
});

/** Helpers  **/
function getNthParent(el, n) {
    for (i = 0; i < n; i++) {
        if (el.parentElement){
            el = el.parentElement;
        } else {
            break;
        }
    }
    return el;
};

// Menu functionality
const header = document.querySelector('.header')

function openMenu(){
    header.classList.add('is-open')
}

function closeMenu(){
    header.classList.remove('is-open')
}

// Header functionality
const emptyBox = document.querySelector(".empty-box");

// Intersection Observer Options
const options = {
    root: null,
    threshold: 0.6,
    rootMargin: "0px 0px 0px 0px"
};

const mainObserver = new IntersectionObserver(function (entries, observer) {
    entries.forEach((entry) => {
        const windowWidth = window.innerWidth
        
        // Mobile and tablet
        if (windowWidth < 1024) {
            // If the element is leaving the viewport
            if (!entry.isIntersecting) {
            header.classList.add("is-scrolled");
            }
            // if the element appears in the viewport
            else {
            header.classList.remove("is-scrolled");
            }
        // Desktop and monitor
        } else {
            // If the element is leaving the viewport
            if (!entry.isIntersecting) {
                header.classList.add("is-scrolled", "is-open");
            }
            // if the element appears in the viewport
            else {
            header.classList.remove("is-scrolled", "is-open");
            }
        }
    });
}, options);

// Executing the observer
mainObserver.observe(emptyBox);